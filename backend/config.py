from decouple import config

class Settings:
    # Supabase Configuration
    SUPABASE_URL: str = config("SUPABASE_URL", default="")
    SUPABASE_ANON_KEY: str = config("SUPABASE_ANON_KEY", default="")
    SUPABASE_SERVICE_ROLE_KEY: str = config("SUPABASE_SERVICE_ROLE_KEY", default="")
    SUPABASE_JWT_SECRET: str = config("SUPABASE_JWT_SECRET", default="")

    # Google Gemini API
    GOOGLE_API_KEY: str = config("GOOGLE_API_KEY", default="")

    # Application Settings
    DEBUG: bool = config("DEBUG", default=True, cast=bool)
    CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

settings = Settings()
