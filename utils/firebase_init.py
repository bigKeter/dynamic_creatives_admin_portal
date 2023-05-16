from dotenv import load_dotenv
from firebase_admin import credentials, initialize_app
import os

# Load the Firebase environment variables from the .env file
load_dotenv()


def init_firebase():
    try:  # Check if the Firebase Admin SDK has already been initialized
        # Create a credentials object using the Firebase environment variables
        cred = credentials.Certificate({
            "type": os.getenv("FIREBASE_TYPE"),
            "project_id": os.getenv("FIREBASE_PROJECT_ID"),
            "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
            "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
            "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
            "client_id": os.getenv("FIREBASE_CLIENT_ID"),
            "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
            "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
            "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL")
        })

        # Initialize the Firebase Admin SDK with the credentials object
        initialize_app(cred)
    except ValueError:
        # Firebase has already been initialized
        pass