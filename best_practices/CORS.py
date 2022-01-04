"""
        Cross Origin Resource Sharing is used when
                API is axchenging data with different domain
                before accessing the web browser.

        This situation is common for backend/frontend
                scenario. If handed unproperly or void will 
                lead to security issues.
"""

# Add to project dependencies
""" django-cors-headers"""

# Add to project settings
INSTALLED_APPS = [
    ...
    'corsheaders' # New
    ...
]

MIDDLEWARE = [
    ...
    'django.contrib,sessions.middleware.SessionMidlware',
    "corsheaders.middleware.CorsMiddleware",  # New
    'django.middleware.common.CommonMidleware',
    ...
]

# New
CORS_ORIGIN_WHITELIST = (
    # Backand domain
    'http://localhost:8000',
    # Frontend domain
    'http://localhost:3000',
)
