#!/bin/bash/python3
import requests
import csv

def fetch_and_print_posts():
    """Fetch posts and print the status code + their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If successful, parse JSON
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save id, title, body into posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Prepare list of dictionaries
        posts_list = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
            }
            for post in data
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_list)
