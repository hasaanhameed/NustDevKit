"""Auth request/response schemas."""
from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(..., description="NUST LMS username", examples=["johndoe.bscs23seecs"])
    password: str = Field(..., description="NUST LMS password")


class TokenResponse(BaseModel):
    access_token: str = Field(..., description="Gateway-issued JWT bearer token")
    token_type: str = Field(default="bearer")
