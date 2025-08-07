# config/settings.py

import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
    GITHUB_WEBHOOK_SECRET = os.getenv('GITHUB_WEBHOOK_SECRET', 'your_webhook_secret')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key')
    FIREBASE_CONFIG = {
        'apiKey': os.getenv('FIREBASE_API_KEY', 'your_firebase_api_key'),
        'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN', 'your_firebase_auth_domain'),
        'databaseURL': os.getenv('FIREBASE_DATABASE_URL', 'your_firebase_database_url'),
        'projectId': os.getenv('FIREBASE_PROJECT_ID', 'your_firebase_project_id'),
        'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET', 'your_firebase_storage_bucket'),
        'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID', 'your_firebase_messaging_sender_id'),
        'appId': os.getenv('FIREBASE_APP_ID', 'your_firebase_app_id'),
    }