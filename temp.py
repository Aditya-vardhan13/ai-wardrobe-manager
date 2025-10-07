import google.generativeai as genai
import os

# Set your Gemini API key
# You can get this from: https://makersuite.google.com/app/apikey
# Set it as an environment variable: export GOOGLE_API_KEY="your-api-key-here"
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("Please set your GOOGLE_API_KEY environment variable")
    print("You can get an API key from: https://makersuite.google.com/app/apikey")
    exit(1)

# Configure the API
genai.configure(api_key=API_KEY)

# Create the model
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# Make the API call
response = model.generate_content("what is the capital of India?")

print(response.text)
