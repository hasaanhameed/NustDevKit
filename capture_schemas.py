import requests
from bs4 import BeautifulSoup
import urllib3
import json
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE = 'https://lms.nust.edu.pk/portal'
USER_ID = 162154

# ── Auth ──────────────────────────────────────────────────────────────────────

session = requests.Session()
session.verify = False

login_page = session.get(f'{BASE}/login/index.php')
soup = BeautifulSoup(login_page.text, 'html.parser')
logintoken = soup.find('input', {'name': 'logintoken'})['value']

session.post(f'{BASE}/login/index.php', data={
    'username': 'hhameed.bscs23seecs',
    'password': 'vukedrec',
    'logintoken': logintoken,
})

dashboard = session.get(f'{BASE}/my/')
soup = BeautifulSoup(dashboard.text, 'html.parser')
sesskey = soup.find('input', {'name': 'sesskey'})['value']
print(f'Authenticated. sesskey: {sesskey[:10]}...\n')


# ── Helpers ───────────────────────────────────────────────────────────────────

def strip_blobs(obj):
    """Remove base64 courseimage fields — not useful for schemas."""
    if isinstance(obj, dict):
        return {k: strip_blobs(v) for k, v in obj.items() if k != 'courseimage'}
    if isinstance(obj, list):
        return [strip_blobs(i) for i in obj]
    return obj


def ajax(methodname, args):
    r = session.post(
        f'{BASE}/lib/ajax/service.php?sesskey={sesskey}&info={methodname}',
        json=[{'index': 0, 'methodname': methodname, 'args': args}]
    )
    data = r.json()
    if isinstance(data, list) and data[0].get('error') == False:
        return True, strip_blobs(data[0].get('data'))
    err = data[0].get('exception', {}) if isinstance(data, list) else {}
    return False, f"{err.get('errorcode', '?')}: {err.get('message', '')}"


# ── Step 1: Collect real IDs ──────────────────────────────────────────────────

print('=== Collecting IDs ===')

ok, enrolled = ajax('core_course_get_enrolled_courses_by_timeline_classification', {
    'offset': 0, 'limit': 50, 'classification': 'all', 'sort': 'fullname'
})
courses = enrolled.get('courses', []) if ok else []
course_ids = [c['id'] for c in courses]
COURSE_ID = course_ids[0] if course_ids else 61084
print(f'Enrolled courses: {len(course_ids)} → using COURSE_ID={COURSE_ID}')

ok2, cal = ajax('core_calendar_get_action_events_by_timesort', {
    'limitnum': 50, 'timesortfrom': 0
})
events = cal.get('events', []) if ok2 else []
COURSE_IDS_WITH_EVENTS = list({e['course']['id'] for e in events if e.get('course')})
FIRST_EVENT_COURSE = COURSE_IDS_WITH_EVENTS[0] if COURSE_IDS_WITH_EVENTS else COURSE_ID
print(f'Calendar course IDs: {COURSE_IDS_WITH_EVENTS[:5]}')

print()

# ── Step 2: Capture schemas ───────────────────────────────────────────────────

print('=== Capturing endpoint schemas ===\n')

results = []

def capture(methodname, args, note=None):
    ok, response = ajax(methodname, args)
    status = '✅' if ok else '❌'
    label = note or methodname
    print(f'{status} {label}')
    if not ok:
        print(f'   Error: {response}')
    results.append({
        'method': methodname,
        'note': note,
        'request': args,
        'success': ok,
        'response': response if ok else None,
        'error': response if not ok else None,
    })


# 1. Recent courses
capture('core_course_get_recent_courses', {'limit': 10})

# 2. Enrolled courses by timeline
capture(
    'core_course_get_enrolled_courses_by_timeline_classification',
    {'offset': 0, 'limit': 50, 'classification': 'all', 'sort': 'fullname'},
)

# 3. Calendar events by timesort (global)
capture(
    'core_calendar_get_action_events_by_timesort',
    {'limitnum': 20, 'timesortfrom': 0},
)

# 5. Calendar events per course
capture(
    'core_calendar_get_action_events_by_course',
    {'courseid': FIRST_EVENT_COURSE},
    note=f'core_calendar_get_action_events_by_course (course {FIRST_EVENT_COURSE})',
)

# 6. User by field
capture(
    'core_user_get_users_by_field',
    {'field': 'id', 'values': [str(USER_ID)]},
)

# 7. User preferences
capture('core_user_get_user_preferences', {'userid': USER_ID})

# 8. Popup notifications
capture('message_popup_get_popup_notifications', {
    'useridto': str(USER_ID),
    'limit': 20,
    'offset': 0,
})


# ── Step 3: Save ──────────────────────────────────────────────────────────────

out = {
    'meta': {
        'user_id': USER_ID,
        'course_id_used': COURSE_ID,
        'all_course_ids': course_ids,
    },
    'endpoints': results,
}

with open('endpoint_schemas.json', 'w') as f:
    json.dump(out, f, indent=2)

ok_count = sum(1 for r in results if r['success'])
print(f'\n=== Done: {ok_count}/{len(results)} succeeded ===')
print('Saved to endpoint_schemas.json')
