#!/usr/bin/env python3
"""
Demo script for Prompt Optimizer
Shows the capabilities without requiring interactive input
"""

from colorama import init, Fore, Style
from prompt_engineer import PromptEngineer

# Initialize colorama
init(autoreset=True)

def print_header(text):
    """Print a formatted header"""
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}{text:^70}")
    print(f"{Fore.CYAN}{'='*70}\n")

def print_section(title):
    """Print a section title"""
    print(f"\n{Fore.YELLOW}▶ {title}")
    print(f"{Fore.YELLOW}{'-'*70}")

def demo_analysis(prompt):
    """Demonstrate prompt analysis"""
    engineer = PromptEngineer()
    
    print(f"\n{Fore.WHITE}Original Prompt:")
    print(f"{Fore.GREEN}  \"{prompt}\"\n")
    
    analysis = engineer.analyze_prompt(prompt)
    
    print(f"{Fore.WHITE}Analysis Results:")
    print(f"  • Length: {analysis['length']} characters")
    print(f"  • Specificity: {Fore.CYAN}{analysis['specificity']}{Style.RESET_ALL}")
    
    print(f"\n{Fore.WHITE}  Elements Present:")
    print(f"    {'✅' if analysis['has_role'] else '❌'} Role Definition")
    print(f"    {'✅' if analysis['has_context'] else '❌'} Context/Background")
    print(f"    {'✅' if analysis['has_examples'] else '❌'} Examples")
    print(f"    {'✅' if analysis['has_constraints'] else '❌'} Constraints")
    print(f"    {'✅' if analysis['has_format'] else '❌'} Output Format")
    
    if analysis['suggestions']:
        print(f"\n{Fore.WHITE}  Improvement Suggestions:")
        for suggestion in analysis['suggestions']:
            print(f"    {Fore.YELLOW}• {suggestion}")
    
    return analysis

def main():
    """Run demonstration"""
    print_header("🤖 Prompt Optimizer - Demo")
    
    print(f"{Fore.WHITE}This demo shows how the Prompt Optimizer analyzes and improves prompts")
    print(f"{Fore.WHITE}using prompt engineering techniques.\n")
    
    # Demo 1: Poor prompt
    print_section("Demo 1: Analyzing a Basic Prompt")
    demo_analysis("Write about dogs")
    
    # Demo 2: Better prompt
    print_section("Demo 2: Analyzing an Improved Prompt")
    demo_analysis("""You are an expert veterinarian. Write a comprehensive guide about dog care 
that includes nutrition requirements, exercise needs, and common health issues. 
Format the output as a structured article with clear sections.""")
    
    # Demo 3: Show tips
    print_section("Demo 3: Prompt Engineering Best Practices")
    engineer = PromptEngineer()
    tips = engineer.get_engineering_tips()
    
    print(f"\n{Fore.WHITE}Top 10 Prompt Engineering Tips:\n")
    for i, tip in enumerate(tips, 1):
        print(f"{Fore.CYAN}{i:2d}. {tip}")
    
    # Demo 4: Comparison
    print_section("Demo 4: Before and After Comparison")
    
    prompts = [
        ("Basic", "Create a function to sort numbers"),
        ("Optimized", """You are an expert Python developer. Create a function named 'sort_numbers' that:
- Takes a list of integers as input
- Returns a new sorted list in ascending order
- Handles edge cases (empty lists, single elements)
- Includes type hints and docstrings
- Provides example usage

Format: Include the function implementation followed by 3 test cases.""")
    ]
    
    for label, prompt in prompts:
        print(f"\n{Fore.CYAN}{label} Prompt:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  \"{prompt[:80]}{'...' if len(prompt) > 80 else ''}\"")
        
        analysis = PromptEngineer().analyze_prompt(prompt)
        print(f"\n{Fore.WHITE}  Quick Stats:")
        print(f"    Length: {analysis['length']} chars | Specificity: {analysis['specificity']}")
        print(f"    Elements: {sum([analysis['has_role'], analysis['has_context'], analysis['has_examples'], analysis['has_constraints'], analysis['has_format']])}/5")
    
    # Conclusion
    print_header("Summary")
    print(f"{Fore.GREEN}✅ The Prompt Optimizer helps you:")
    print(f"{Fore.WHITE}  1. Analyze your prompts for key elements")
    print(f"{Fore.WHITE}  2. Identify missing components")
    print(f"{Fore.WHITE}  3. Get specific improvement suggestions")
    print(f"{Fore.WHITE}  4. Apply prompt engineering best practices")
    print(f"{Fore.WHITE}  5. Generate better AI responses")
    
    print(f"\n{Fore.CYAN}To use the full interactive version:")
    print(f"{Fore.WHITE}  python main.py")
    
    print(f"\n{Fore.CYAN}To run tests:")
    print(f"{Fore.WHITE}  python test_optimizer.py")
    
    print(f"\n{Fore.CYAN}For more examples:")
    print(f"{Fore.WHITE}  See EXAMPLES.md for detailed before/after comparisons\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.CYAN}Demo interrupted. Goodbye! 👋\n")
