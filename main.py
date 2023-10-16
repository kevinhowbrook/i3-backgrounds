#!/usr/bin/python3
import os
import requests
import random
import subprocess

from config import ACCESS_KEY

BASE_URL = "https://api.unsplash.com/photos/random"
QUERY = "space,mountains,stars,rain,ducks,hiking,fog,storms"  # Change this to your desired hashtag(s)

# Directory to save downloaded images
IMAGE_DIR = "~/shared/i3-backgrounds/images"  # Change this to your preferred directory

# Function to download an image from Unsplash
def download_image():
    # Set headers for the API request
    headers = {"Authorization": f"Client-ID {ACCESS_KEY}"}
    query = QUERY.split(",")
    query = random.choice(query)
    # Build the API request URL
    params = {
        "query": query,
        "orientation": "landscape",
        "count": 1,
        "content_filter": "high",  # Optionally, filter for high-quality content
        "w": "1920",  # Width of the image (adjust as needed)
        "fit": "max",  # Ensure the image is at least as large as specified
    }

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()[0]
        image_url = data["urls"]["full"]
        image_id = data["id"]

        # Download the image
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            image_path = os.path.expanduser(os.path.join(IMAGE_DIR, f"1.jpg"))

            with open(image_path, "wb") as f:
                f.write(image_response.content)

            return image_path

    return None

def delete_existing_images():
    for filename in os.listdir(os.path.expanduser(IMAGE_DIR)):
        if filename.endswith(".jpg"):
            file_path = os.path.join(os.path.expanduser(IMAGE_DIR), filename)
            os.remove(file_path)

# Function to set the desktop background using 'feh'
def set_background(image_path):
    subprocess.call(["feh", "--bg-fill", image_path])

delete_existing_images()

# Ensure the image directory exists
os.makedirs(os.path.expanduser(IMAGE_DIR), exist_ok=True)

# Download an image
image_path = download_image()

if image_path:
    # Set the downloaded image as the background
    set_background(image_path)
else:
    print("Failed to download an image.")
