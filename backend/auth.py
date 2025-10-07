from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from config import settings

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify Supabase JWT token"""
    token = credentials.credentials

    if not settings.SUPABASE_JWT_SECRET:
        raise HTTPException(status_code=500, detail="JWT secret not configured")

    try:
        # Decode the JWT token
        payload = jwt.decode(
            token,
            settings.SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            audience="authenticated"
        )

        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Authentication failed: {str(e)}")

# Dependency function to get current user
async def get_current_user(token_data: dict = Depends(verify_token)):
    return {
        "user_id": token_data.get("sub"),
        "email": token_data.get("email"),
        "role": token_data.get("role", "authenticated")
    }
