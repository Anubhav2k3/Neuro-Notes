import os
import requests

# Use the provided GEMINI_API_KEY or fallback to the one provided
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "your api key goes here"

def generate_gemini_response(prompt):
    """
    Sends prompt to Gemini 1.5 Flash 001 API and returns the response.
    """
    model = "gemini-1.5-flash-001"
    url = f"https://generativelanguage.googleapis.com/v1/models/{model}:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        # Sending the POST request to the Gemini API
        response = requests.post(url, headers=headers, json=payload)

        # Raise an error if the status code indicates failure
        response.raise_for_status()

        # Parse the response JSON
        data = response.json()

        # Check if "candidates" exists in the response
        if "candidates" in data:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            # If no candidates are found, return the error message
            error_message = data.get('error', {}).get('message', 'Unknown error')
            return f"❌ Gemini API Error: {error_message}"
    except requests.exceptions.RequestException as e:
        # Handle network-related or HTTP errors
        return f"❌ Gemini API Error: {str(e)}"
    except Exception as e:
        # Catch any other unexpected errors
        return f"❌ Gemini API Error: {str(e)}"

def generate_summary(text):
    prompt = f"Summarize the following note:\n\n{text}"
    return generate_gemini_response(prompt)

def generate_analysis(text):
    prompt = f"Analyze the following note:\n\n{text}"
    return generate_gemini_response(prompt)

def improve_grammar(text):
    prompt = f"Improve grammar and clarity of the following note:\n\n{text}"
    return generate_gemini_response(prompt)

def translate_content(text, language_code):
    prompt = f"Translate the following note to {language_code}:\n\n{text}"
    return generate_gemini_response(prompt)
