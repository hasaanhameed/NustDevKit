import jwt
from fastmcp.server.auth import AccessToken, TokenVerifier

from app.core.security import decode_access_token


class GatewayTokenVerifier(TokenVerifier):
    """Validates our own JWTs so FastMCP accepts tokens issued by our OAuth flow."""

    async def verify_token(self, token: str) -> AccessToken | None:
        try:
            claims = decode_access_token(token)
        except jwt.PyJWTError:
            return None

        return AccessToken(
            token=token,
            client_id="gateway",
            scopes=[],
            expires_at=claims.get("exp"),
            subject=claims.get("sub"),
            claims=claims,
        )
