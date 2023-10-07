import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

#Credenciais
cred = credentials.Certificate('firebase_sdk.json')

firebase_admin.initialize_app(cred)

# List of user data to sign up
users_to_create = [
    {
        "email": "teste1@gmail.com",
        "password": "123456",
        "display_name": "Teste",
    },
    {
        "email": "teste2@gmail.com",
        "password": "123456",
        "display_name": "Teste2",
    },
    # Add more users here as needed
]

# Function to create users
def create_users(users):
    for user_data in users:
        try:
            user = auth.create_user(
                email=user_data["email"],
                password=user_data["password"],
                display_name=user_data["display_name"]
            )
            print(f"User {user.uid} created successfully")
        except Exception as e:
            print(f"Error creating user: {e}")

# Call the function to create users
create_users(users_to_create)