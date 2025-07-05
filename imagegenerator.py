import requests
import os

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
user_token = input("🔐 Enter your Hugging Face API token: ").strip() #please go through the README and make your own HuggingFaces API Token

headers = {"Authorization": f"Bearer {user_token}"}
def rungen(prompt): 
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:  # Success
        with open("output.png", "wb") as f:
            f.write(response.content)
            print("🗿 Image has been generated and saved as output.png")
            os.startfile("output.png")#this just opens the image immediately after it is created
    else:
        print("🥀 Error:", response.status_code)

user_prompt = input("🎨 Enter your image prompt: ")
rungen(user_prompt)
