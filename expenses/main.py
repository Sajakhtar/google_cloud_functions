import firebase_admin
from firebase_admin import firestore

# Access environment variables    
from dotenv import load_dotenv
load_dotenv()
import os
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS") # os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

# initialize Firebase App
firebase_admin.initialize_app()


# Set database
db = firestore.client()

# cloud function
def set_expense(request):

    from datetime import datetime
    import random

    try:
        # create a new document in the expenses collection
        ref = db.collection('expenses').document()

        # set document data
        ref.set({'createdAt': datetime.now(), 'expense': random.randint(1,200)})

        # status code for OK
        return 'OK', 200

    except Exception as e:
        # status code for Bad Request
        return e, 400


