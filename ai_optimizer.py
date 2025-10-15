"""
AI Integration Module
Handles communication with AI API (Google Gemini)
"""

import os
from typing import Optional
import google.generativeai as genai
from dotenv import load_dotenv

class AIOptimizer:
    """
    Handles AI-powered prompt optimization using Google Gemini API
    """
    
    def __init__(self):
        """
        Initialize the AI optimizer with API credentials
        """
        load_dotenv()
        self.api_key = os.getenv('GEMINI_API_KEY')
        self.model_name = os.getenv('GEMINI_MODEL', 'gemini-pro')
        
        if not self.api_key or self.api_key == 'your_api_key_here':
            self.model = None
        else:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
    
    def is_configured(self) -> bool:
        """
        Check if the AI optimizer is properly configured
        """
        return self.model is not None
    
    def optimize_prompt(self, optimization_instructions: str) -> Optional[str]:
        """
        Use AI to optimize the prompt based on the given instructions
        """
        if not self.is_configured():
            return None
        
        try:
            # Combine system instruction with user prompt for Gemini
            full_prompt = f"""You are an expert in prompt engineering and optimization. Your responses should be clear, well-structured prompts that follow best practices.

{optimization_instructions}"""
            
            response = self.model.generate_content(full_prompt)
            
            return response.text.strip()
        
        except Exception as e:
            print(f"Error calling API: {str(e)}")
            return None
    
    def get_suggestions(self, prompt: str) -> Optional[str]:
        """
        Get specific suggestions for improving a prompt
        """
        if not self.is_configured():
            return None
        
        suggestion_prompt = f"""You are a prompt engineering expert who provides concise, actionable advice.

Analyze this prompt and provide 3-5 specific, actionable suggestions to improve it using prompt engineering techniques:

"{prompt}"

Format your response as a numbered list with brief explanations."""
        
        try:
            response = self.model.generate_content(suggestion_prompt)
            
            return response.text.strip()
        
        except Exception as e:
            print(f"Error calling API: {str(e)}")
            return None
