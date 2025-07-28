import requests
import json

# FastAPI server URL
BASE_URL = "http://127.0.0.1:8000"

# Test payload for the /ask endpoint
payload = {
    "username": "john123",
    "question": "Can you explain what verbs are?"
}

def test_ask_endpoint():
    url = f"{BASE_URL}/ask"
    headers = {"Content-Type": "application/json"}

    print(f"Sending request to {url}...")
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("\nAI Response:")
        print(response.json().get("answer"))
    else:
        print(f"\nError {response.status_code}: {response.text}")

if __name__ == "__main__":
    test_ask_endpoint()
