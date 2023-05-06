from firebase_admin import firestore_async, firestore
from utils.firebase_init import init_firebase

init_firebase()

# Get a reference to the Firestore database
db = firestore.client()

# Get collection documents using collection name


def get_collection_docs(collection_name):
    ref = db.collection(collection_name)
    docs = ref.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
    return docs

# Get document data using collection name and document name


async def get_doc_data(collection_name, doc_name):
    try:
        ref = db.collection(collection_name).document(doc_name)
        doc = ref.stream()
        print(f'{doc.id} => {doc.to_dict()}')
        return doc
    except Exception as e:
        print(f'Error getting document: {e}')
        return None

# Update document data using collection name, document reference, and data


async def update_doc_data(collection_name, doc_ref, data):
    try:
        ref = db.collection(collection_name).document(doc_ref)
        ref.set(data)
        print(f'{doc_ref} => {data}')
        return True
    except Exception as e:
        print(f'Error updating document: {e}')
        return False

# Delete document data using collection name and document reference


async def delete_doc_data(collection_name, doc_ref):
    try:
        ref = db.collection(collection_name).document(doc_ref)
        ref.delete()
        print(f'{doc_ref} => deleted')
        return True
    except Exception as e:
        print(f'Error deleting document: {e}')
        return False

# Add document data using collection name and data


async def add_doc_data(collection_name, data):
    try:
        ref = db.collection(collection_name).document()
        ref.set(data)
        print(f'{ref.id} => {data}')
        return True
    except Exception as e:
        print(f'Error adding document: {e}')
        return False
