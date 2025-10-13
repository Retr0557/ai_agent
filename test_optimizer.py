"""
Test script for prompt optimizer functionality
"""

from prompt_engineer import PromptEngineer
from ai_optimizer import AIOptimizer

def test_prompt_analysis():
    """Test the prompt analysis functionality"""
    print("="*60)
    print("Testing Prompt Analysis")
    print("="*60)
    
    engineer = PromptEngineer()
    
    # Test with a simple prompt
    test_prompt = "Write about dogs"
    print(f"\nTest Prompt: '{test_prompt}'")
    
    analysis = engineer.analyze_prompt(test_prompt)
    
    print(f"\nAnalysis Results:")
    print(f"  Length: {analysis['length']}")
    print(f"  Specificity: {analysis['specificity']}")
    print(f"  Has Role: {analysis['has_role']}")
    print(f"  Has Context: {analysis['has_context']}")
    print(f"  Has Examples: {analysis['has_examples']}")
    print(f"  Has Constraints: {analysis['has_constraints']}")
    print(f"  Has Format: {analysis['has_format']}")
    
    print(f"\n  Suggestions ({len(analysis['suggestions'])}):")
    for suggestion in analysis['suggestions']:
        print(f"    - {suggestion}")
    
    # Test with a better prompt
    print("\n" + "="*60)
    test_prompt2 = """You are an expert veterinarian. Write a comprehensive guide about dog care that includes:
1. Nutrition requirements
2. Exercise needs
3. Common health issues

Format the output as a structured article with clear sections."""
    
    print(f"\nTest Prompt 2: '{test_prompt2[:50]}...'")
    
    analysis2 = engineer.analyze_prompt(test_prompt2)
    
    print(f"\nAnalysis Results:")
    print(f"  Length: {analysis2['length']}")
    print(f"  Specificity: {analysis2['specificity']}")
    print(f"  Has Role: {analysis2['has_role']}")
    print(f"  Has Context: {analysis2['has_context']}")
    print(f"  Has Examples: {analysis2['has_examples']}")
    print(f"  Has Constraints: {analysis2['has_constraints']}")
    print(f"  Has Format: {analysis2['has_format']}")
    
    print(f"\n  Suggestions ({len(analysis2['suggestions'])}):")
    if analysis2['suggestions']:
        for suggestion in analysis2['suggestions']:
            print(f"    - {suggestion}")
    else:
        print("    - None (prompt is well-structured)")
    
    return True

def test_prompt_engineering_tips():
    """Test getting prompt engineering tips"""
    print("\n" + "="*60)
    print("Testing Prompt Engineering Tips")
    print("="*60)
    
    tips = PromptEngineer.get_engineering_tips()
    print(f"\nTotal tips: {len(tips)}")
    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")
    
    return True

def test_ai_optimizer_configuration():
    """Test AI optimizer configuration"""
    print("\n" + "="*60)
    print("Testing AI Optimizer Configuration")
    print("="*60)
    
    optimizer = AIOptimizer()
    is_configured = optimizer.is_configured()
    
    print(f"\nAI Optimizer configured: {is_configured}")
    if not is_configured:
        print("Note: This is expected if no API key is set in .env file")
        print("AI features will not work without an API key, but local analysis will.")
    
    return True

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("🤖 Prompt Optimizer - Test Suite")
    print("="*60 + "\n")
    
    tests = [
        ("Prompt Analysis", test_prompt_analysis),
        ("Prompt Engineering Tips", test_prompt_engineering_tips),
        ("AI Optimizer Configuration", test_ai_optimizer_configuration)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
                print(f"\n✅ {test_name}: PASSED")
            else:
                failed += 1
                print(f"\n❌ {test_name}: FAILED")
        except Exception as e:
            failed += 1
            print(f"\n❌ {test_name}: FAILED with error: {str(e)}")
    
    print("\n" + "="*60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
