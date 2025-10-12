"""
Prompt Optimizer App
A CLI application for optimizing prompts using AI and prompt engineering techniques
"""

import sys
from colorama import init, Fore, Style
from prompt_engineer import PromptEngineer
from ai_optimizer import AIOptimizer

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)

def print_banner():
    """Print application banner"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{'  🤖 AI Prompt Optimizer  ':^60}")
    print(f"{Fore.CYAN}{'  Enhance your prompts with AI-powered optimization  ':^60}")
    print(f"{Fore.CYAN}{'='*60}\n")

def print_section(title: str):
    """Print a section header"""
    print(f"\n{Fore.YELLOW}▶ {title}")
    print(f"{Fore.YELLOW}{'-'*60}")

def print_analysis(analysis: dict):
    """Print prompt analysis results"""
    print_section("Prompt Analysis")
    
    print(f"\n{Fore.WHITE}Length: {analysis['length']} characters")
    print(f"Specificity: {Fore.GREEN if analysis['specificity'] in ['high', 'medium'] else Fore.RED}{analysis['specificity']}{Style.RESET_ALL}")
    
    print(f"\n{Fore.WHITE}Elements Present:")
    print(f"  {'✅' if analysis['has_role'] else '❌'} Role Definition")
    print(f"  {'✅' if analysis['has_context'] else '❌'} Context/Background")
    print(f"  {'✅' if analysis['has_examples'] else '❌'} Examples")
    print(f"  {'✅' if analysis['has_constraints'] else '❌'} Constraints")
    print(f"  {'✅' if analysis['has_format'] else '❌'} Output Format")
    
    if analysis['suggestions']:
        print(f"\n{Fore.WHITE}Suggestions for Improvement:")
        for suggestion in analysis['suggestions']:
            print(f"  {Fore.YELLOW}• {suggestion}")

def print_tips():
    """Print prompt engineering tips"""
    print_section("Prompt Engineering Tips")
    tips = PromptEngineer.get_engineering_tips()
    for tip in tips:
        print(f"  {tip}")

def get_multiline_input() -> str:
    """Get multiline input from user"""
    print(f"{Fore.CYAN}Enter your prompt (press Enter twice when done):")
    lines = []
    empty_count = 0
    
    while True:
        try:
            line = input()
            if line == "":
                empty_count += 1
                if empty_count >= 2:
                    break
            else:
                empty_count = 0
                lines.append(line)
        except EOFError:
            break
    
    return "\n".join(lines).strip()

def show_menu() -> str:
    """Show main menu and get user choice"""
    print(f"\n{Fore.CYAN}Choose an option:")
    print(f"{Fore.WHITE}1. Optimize a prompt (AI-powered)")
    print(f"{Fore.WHITE}2. Analyze a prompt (local analysis)")
    print(f"{Fore.WHITE}3. Get AI suggestions")
    print(f"{Fore.WHITE}4. View prompt engineering tips")
    print(f"{Fore.WHITE}5. Exit")
    
    choice = input(f"\n{Fore.CYAN}Your choice (1-5): {Style.RESET_ALL}").strip()
    return choice

def run_optimization_mode(ai_optimizer: AIOptimizer):
    """Run AI-powered optimization"""
    if not ai_optimizer.is_configured():
        print(f"\n{Fore.RED}❌ AI optimization requires an OpenAI API key.")
        print(f"{Fore.YELLOW}Please set your OPENAI_API_KEY in a .env file.")
        print(f"{Fore.YELLOW}Example: Copy .env.example to .env and add your API key.")
        return
    
    print_section("AI-Powered Prompt Optimization")
    prompt = get_multiline_input()
    
    if not prompt:
        print(f"{Fore.RED}No prompt entered. Returning to menu.")
        return
    
    print(f"\n{Fore.CYAN}Analyzing and optimizing your prompt...")
    
    # Analyze the prompt
    engineer = PromptEngineer()
    analysis = engineer.analyze_prompt(prompt)
    
    # Build optimization instructions
    optimization_instructions = engineer.build_optimized_prompt(prompt, analysis)
    
    # Get optimized prompt from AI
    optimized = ai_optimizer.optimize_prompt(optimization_instructions)
    
    if optimized:
        print_section("Optimized Prompt")
        print(f"\n{Fore.GREEN}{optimized}\n")
        
        # Offer to show analysis
        show_analysis = input(f"{Fore.CYAN}Show detailed analysis? (y/n): {Style.RESET_ALL}").strip().lower()
        if show_analysis == 'y':
            print_analysis(analysis)
    else:
        print(f"{Fore.RED}Failed to optimize prompt. Please check your API configuration.")

def run_analysis_mode():
    """Run local prompt analysis"""
    print_section("Prompt Analysis Mode")
    prompt = get_multiline_input()
    
    if not prompt:
        print(f"{Fore.RED}No prompt entered. Returning to menu.")
        return
    
    engineer = PromptEngineer()
    analysis = engineer.analyze_prompt(prompt)
    print_analysis(analysis)

def run_suggestions_mode(ai_optimizer: AIOptimizer):
    """Get AI suggestions for improvement"""
    if not ai_optimizer.is_configured():
        print(f"\n{Fore.RED}❌ AI suggestions require an OpenAI API key.")
        print(f"{Fore.YELLOW}Please set your OPENAI_API_KEY in a .env file.")
        return
    
    print_section("Get AI Suggestions")
    prompt = get_multiline_input()
    
    if not prompt:
        print(f"{Fore.RED}No prompt entered. Returning to menu.")
        return
    
    print(f"\n{Fore.CYAN}Getting AI suggestions...")
    suggestions = ai_optimizer.get_suggestions(prompt)
    
    if suggestions:
        print_section("AI Suggestions")
        print(f"\n{Fore.GREEN}{suggestions}\n")
    else:
        print(f"{Fore.RED}Failed to get suggestions. Please check your API configuration.")

def main():
    """Main application loop"""
    print_banner()
    
    # Initialize AI optimizer
    ai_optimizer = AIOptimizer()
    
    if not ai_optimizer.is_configured():
        print(f"{Fore.YELLOW}⚠️  Note: AI features require an OpenAI API key.")
        print(f"{Fore.YELLOW}Local analysis features are still available.\n")
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            run_optimization_mode(ai_optimizer)
        elif choice == '2':
            run_analysis_mode()
        elif choice == '3':
            run_suggestions_mode(ai_optimizer)
        elif choice == '4':
            print_tips()
        elif choice == '5':
            print(f"\n{Fore.CYAN}Thank you for using AI Prompt Optimizer! 👋\n")
            sys.exit(0)
        else:
            print(f"{Fore.RED}Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.CYAN}Exiting... Goodbye! 👋\n")
        sys.exit(0)
