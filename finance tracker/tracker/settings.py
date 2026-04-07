DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'finance_db',  # Replace with your DB name
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb://localhost:27017',  # Or your Atlas connection string
        },
    }
}

# Add your app to INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'tracker',
    'rest_framework',  # for APIs
    'crispy_forms',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

