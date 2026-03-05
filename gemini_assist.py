import os
from google import genai
from google.genai import types
from PIL import Image

# Initialize the Gemini client
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

# Tools

def fact(topic):
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = ["Give me a fact about ", topic])
    return(response.text)
def joke(topic):
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = ["Tell me a joke about ", topic])
    return(response.text)
def weather(location):
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = ["What is the current weather in ", location])
    return(response.text)
def news(topic):
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = ["What are the latest news about ", topic])
    return(response.text)
def advice(topic):
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = ["Give me some advice about ", topic])
    return(response.text)

# Usage

def use_input(user_input):
    if not user_input.startswith("/"):
        response = client.models.generate_content(model = "gemini-2.5-flash", contents = user_input)
        return(response.text)
    
    parts = user_input.split()
    prompt = parts[0].lower()
    
    if prompt == "/fact":
        return fact(" ".join(parts[1:]))
    elif prompt == "/joke":
        return joke(" ".join(parts[1:]))
    elif prompt == "/weather":
        return weather(" ".join(parts[1:]))
    elif prompt == "/news":
        return news(" ".join(parts[1:]))
    elif prompt == "/advice":
        return advice(" ".join(parts[1:]))
    else: 
        return "Bad command"

# Image query
def image_query(image_path):
    # Load image and analyze using Gemini
    
    img = Image.open(image_path)
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = ["Describe the content of the following image: ", img])
    return(response.text)
    
# Image creation

def create_image(prompt):
    response = client.models.generate_images(
        model = "imagen-4.0-generate-001", 
        prompt = prompt
    )
    image = response.generated_images[0].images
    
    with open("image.png", "wb") as f:
        f.write(image)

    print("Image saved as image.png")
    
def main():
    while True:
        print ("Options: ")
        print ("1 - chat/command")
        print ("2 - image query")
        print ("3 - create image")
        print ("4 - exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            user_input = input("Enter your command or chat message: ")
            response = use_input(user_input)
            print("Response: ", response)
        elif choice == "2":
            image_path = input("Enter the path to the image: ")
            response = image_query(image_path)
            print("Image Analysis: ", response)
        elif choice == "3":
            prompt = input("Enter a prompt for image creation: ")
            create_image(prompt)
        elif choice == "4":
            break
        else:
            print("Bad choice")
            
main()            
