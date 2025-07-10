import json
import logging
import os
from django.conf import settings
from google import genai
from google.genai import types


class AIService:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
    
    def summarize_note(self, text: str) -> str:
        """Summarize the content of a note"""
        try:
            prompt = f"Please summarize the following note content concisely while maintaining key points:\n\n{text}"
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            return response.text or "Unable to generate summary"
        except Exception as e:
            logging.error(f"Error summarizing note: {e}")
            return f"Error: Unable to summarize note - {str(e)}"
    
    def improve_grammar(self, text: str) -> str:
        """Improve grammar and readability of the note"""
        try:
            prompt = f"Please improve the grammar, spelling, and overall readability of the following text while maintaining its original meaning and tone:\n\n{text}"
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            return response.text or "Unable to improve grammar"
        except Exception as e:
            logging.error(f"Error improving grammar: {e}")
            return f"Error: Unable to improve grammar - {str(e)}"
    
    def translate_to_hindi(self, text: str) -> str:
        """Translate the note content to Hindi"""
        try:
            prompt = f"Please translate the following text to Hindi accurately while maintaining the context and meaning:\n\n{text}"
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            return response.text or "Unable to translate to Hindi"
        except Exception as e:
            logging.error(f"Error translating to Hindi: {e}")
            return f"Error: Unable to translate - {str(e)}"
    
    def analyze_content(self, text: str) -> str:
        """Analyze the content and provide insights"""
        try:
            prompt = f"""Please analyze the following note content and provide insights including:
            1. Key themes and topics
            2. Tone and writing style
            3. Suggested improvements or areas to expand
            4. Overall assessment
            
            Content to analyze:
            {text}"""
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            return response.text or "Unable to analyze content"
        except Exception as e:
            logging.error(f"Error analyzing content: {e}")
            return f"Error: Unable to analyze content - {str(e)}"


# Global instance
ai_service = AIService()
