#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py username password")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)

    try:
        response = requests.get("https://api.github.com/user", auth=auth)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        user_id = response.json().get("id")
        print(user_id)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

