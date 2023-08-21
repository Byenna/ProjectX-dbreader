import time
import requests
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate('test-12-12-12-firebase-adminsdk-d0rcs-be2e6eb263.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-12-12-12-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Firebase Realtime Database reference
ref = db.reference('/page_loads')

# Define your thresholds
page_load_threshold = 0  # in seconds
server_response_threshold = 200  # in milliseconds

def measure_page_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    return end_time - start_time

def measure_server_response_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def main():
    url = 'https://google.com'  # Replace with your target URL

    while True:
        page_load_time = measure_page_load_time(url)
        server_response_time = measure_server_response_time(url)

        data = {
            'timestamp': int(time.time()),
            'page_load_time': page_load_time,
            'server_response_time': server_response_time,
            'url': url
        }
        ref.push(data)

        if page_load_time > page_load_threshold:
            print("Page load time threshold met - page load time:", page_load_time)
        if server_response_time > server_response_threshold:
            print("Server response time threshold met - server response time:", server_response_time)

        time.sleep(60)  # Wait for 1 minute before measuring again

if __name__ == "__main__":
    main()