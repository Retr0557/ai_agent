"""
Prompt Engineering Module
Contains strategies and techniques for optimizing prompts
"""

class PromptEngineer:
    """
    Applies various prompt engineering techniques to optimize user prompts
    """
    
    @staticmethod
    def analyze_prompt(prompt: str) -> dict:
        """
        Analyze the given prompt and identify areas for improvement
        """
        analysis = {
            'length': len(prompt),
            'has_context': False,
            'has_role': False,
            'has_examples': False,
            'has_constraints': False,
            'has_format': False,
            'specificity': 'low',
            'suggestions': []
        }
        
        # Check for context indicators
        context_keywords = ['context:', 'background:', 'about', 'regarding']
        analysis['has_context'] = any(kw in prompt.lower() for kw in context_keywords)
        
        # Check for role definition
        role_keywords = ['you are', 'act as', 'as a', 'you\'re a']
        analysis['has_role'] = any(kw in prompt.lower() for kw in role_keywords)
        
        # Check for examples
        example_keywords = ['example', 'for instance', 'such as', 'like']
        analysis['has_examples'] = any(kw in prompt.lower() for kw in example_keywords)
        
        # Check for constraints
        constraint_keywords = ['must', 'should', 'don\'t', 'avoid', 'limit', 'maximum', 'minimum']
        analysis['has_constraints'] = any(kw in prompt.lower() for kw in constraint_keywords)
        
        # Check for format requirements
        format_keywords = ['format:', 'output:', 'structure:', 'in the form of']
        analysis['has_format'] = any(kw in prompt.lower() for kw in format_keywords)
        
        # Assess specificity
        if len(prompt) < 20:
            analysis['specificity'] = 'very low'
            analysis['suggestions'].append("Prompt is too short. Add more details.")
        elif len(prompt) < 50:
            analysis['specificity'] = 'low'
            analysis['suggestions'].append("Consider adding more context and specificity.")
        elif len(prompt) < 150:
            analysis['specificity'] = 'medium'
        else:
            analysis['specificity'] = 'high'
        
        # Generate suggestions
        if not analysis['has_role']:
            analysis['suggestions'].append("Add a role definition to guide the AI's perspective.")
        if not analysis['has_context']:
            analysis['suggestions'].append("Provide context or background information.")
        if not analysis['has_examples']:
            analysis['suggestions'].append("Consider adding examples to clarify expectations.")
        if not analysis['has_constraints']:
            analysis['suggestions'].append("Add constraints or requirements to focus the response.")
        if not analysis['has_format']:
            analysis['suggestions'].append("Specify the desired output format.")
        
        return analysis
    
    @staticmethod
    def build_optimized_prompt(prompt: str, analysis: dict) -> str:
        """
        Build an optimized version of the prompt using prompt engineering techniques
        """
        optimization_instructions = """You are an expert in prompt engineering. Your task is to optimize the user's prompt using these techniques:

1. **Role-Based Prompting**: Add a clear role definition (e.g., "You are an expert...")
2. **Context Enhancement**: Add relevant context and background information
3. **Clarity & Specificity**: Make the request clear and specific
4. **Task Decomposition**: Break complex tasks into clear steps if needed
5. **Constraints**: Add appropriate constraints and requirements
6. **Output Format**: Specify the desired format and structure
7. **Few-Shot Examples**: Add examples when helpful
8. **Chain-of-Thought**: Encourage step-by-step reasoning for complex tasks

Original prompt: "{original_prompt}"

Analysis:
- Specificity Level: {specificity}
- Has Role: {has_role}
- Has Context: {has_context}
- Has Examples: {has_examples}
- Has Constraints: {has_constraints}
- Has Format: {has_format}

Suggestions for improvement:
{suggestions}

Generate an optimized version of this prompt that incorporates the missing elements and follows best practices in prompt engineering. The optimized prompt should be clear, specific, and structured to get the best possible response from an AI model.

Return ONLY the optimized prompt, without any explanation or additional text."""
        
        return optimization_instructions.format(
            original_prompt=prompt,
            specificity=analysis['specificity'],
            has_role=analysis['has_role'],
            has_context=analysis['has_context'],
            has_examples=analysis['has_examples'],
            has_constraints=analysis['has_constraints'],
            has_format=analysis['has_format'],
            suggestions='\n'.join(f"- {s}" for s in analysis['suggestions']) if analysis['suggestions'] else "- None"
        )
    
    @staticmethod
    def get_engineering_tips() -> list:
        """
        Return a list of prompt engineering tips
        """
        return [
            "🎭 Define a clear role: 'You are an expert [domain] specialist...'",
            "📝 Be specific and detailed about what you want",
            "🎯 Provide context and background information",
            "📊 Specify the desired output format (list, table, JSON, etc.)",
            "🔗 Use chain-of-thought prompting for complex reasoning",
            "📚 Include few-shot examples when possible",
            "⚙️ Set clear constraints and requirements",
            "🔄 Break complex tasks into smaller steps",
            "💡 Use delimiters to clearly separate sections",
            "✅ Specify quality criteria for the output"
        ]
