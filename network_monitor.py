import time
import requests

websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.cisco.com"
]

def check_website(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        end_time = time.time()

        response_time = round((end_time - start_time) * 1000, 2)

        if response.status_code == 200:
            print(f"[UP] {url} | Response Time: {response_time} ms")
        else:
            print(f"[WARNING] {url} returned status {response.status_code}")

    except requests.exceptions.RequestException:
        print(f"[DOWN] {url} is not reachable")


def monitor():
    print("Starting Network Monitoring...\n")

    while True:
        for site in websites:
            check_website(site)
        print("\nChecking again in 10 seconds...\n")
        time.sleep(10)


if __name__ == "__main__":
    monitor()
