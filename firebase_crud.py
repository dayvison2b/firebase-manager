import firebase_admin
from firebase_admin import credentials, firestore

#Credenciais
cred = credentials.Certificate('firebase_sdk.json')

firebase_admin.initialize_app(cred)
db = firestore.client()


# Ref para a coleção
users_ref = db.collection("users")

# Consultar documentos na coleção
def select(collection):
    docs = collection.stream()
    
    for doc in docs:
        print(f"ID do documento: {doc.id}")
        print(f"Dados: {doc.to_dict()}")
    
# Dados a serem adicionados
def insert(collection, data: dict):
    # Adicionar o documento à coleção
    doc_ref = collection.add(data)
    doc_reference, doc_id = doc_ref
    print("Documento adicionado com id:", doc_id)

def update(collection, document_id, data: dict):
    doc_ref = collection.document(document_id)
    
    doc_ref.update(data)
    print("Document updated!")

def delete(collection, document_id):
    doc_ref = collection.document(document_id)
    
    doc_ref.delete()
    print("Document deleted!")

data = {
        "display_name": "Paty",
        "email": "patricia.cabral@qwst.co",
        "password": "123456"
    }

select(users_ref)
#delete(users_ref, "0Yh18F07JW0shAXDkWZR")
