"""
AI Integration Module
Handles communication with AI API (OpenAI)
"""

import os
from typing import Optional
from openai import OpenAI
from dotenv import load_dotenv

class AIOptimizer:
    """
    Handles AI-powered prompt optimization using OpenAI API
    """
    
    def __init__(self):
        """
        Initialize the AI optimizer with API credentials
        """
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = os.getenv('OPENAI_MODEL', 'gpt-5-mini')
        
        if not self.api_key or self.api_key == 'your_api_key_here':
            self.client = None
        else:
            self.client = OpenAI(api_key=self.api_key)
    
    def is_configured(self) -> bool:
        """
        Check if the AI optimizer is properly configured
        """
        return self.client is not None
    
    def optimize_prompt(self, optimization_instructions: str) -> Optional[str]:
        """
        Use AI to optimize the prompt based on the given instructions
        """
        if not self.is_configured():
            return None
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in prompt engineering and optimization. Your responses should be clear, well-structured prompts that follow best practices."
                    },
                    {
                        "role": "user",
                        "content": optimization_instructions
                    }
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            print(f"Error calling API: {str(e)}")
            return None
    
    def get_suggestions(self, prompt: str) -> Optional[str]:
        """
        Get specific suggestions for improving a prompt
        """
        if not self.is_configured():
            return None
        
        suggestion_prompt = f"""Analyze this prompt and provide 3-5 specific, actionable suggestions to improve it using prompt engineering techniques:

"{prompt}"

Format your response as a numbered list with brief explanations."""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a prompt engineering expert who provides concise, actionable advice."
                    },
                    {
                        "role": "user",
                        "content": suggestion_prompt
                    }
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            print(f"Error calling API: {str(e)}")
            return None
