import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-url.firebaseio.com'
})

# Define your thresholds
threshold1 = 50
threshold2 = 100

# Reference to the database
ref = db.reference('/path/to/data')

def check_thresholds(data):
    value = data['value']  # Adjust this based on your database structure
    if value >= threshold1:
        print(f"Threshold 1 reached: {value}")
        # Perform actions when threshold 1 is reached
    if value >= threshold2:
        print(f"Threshold 2 reached: {value}")
        # Perform actions when threshold 2 is reached

def listen_for_changes(event):
    if event.event_type == 'put':
        data = event.data
        check_thresholds(data)

# Listen for changes in the database
ref.listen(listen_for_changes)
