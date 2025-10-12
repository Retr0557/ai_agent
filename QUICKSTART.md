# Quick Start Guide

Get started with the AI Prompt Optimizer in 3 minutes!

## Installation (2 minutes)

```bash
# 1. Clone the repository
git clone https://github.com/Retr0557/ai_agent.git
cd ai_agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Set up API key for AI features
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Try It Out (1 minute)

### Option 1: Run the Demo
```bash
python demo.py
```
This shows the capabilities without requiring any input.

### Option 2: Run Tests
```bash
python test_optimizer.py
```
Validates that everything is working correctly.

### Option 3: Interactive Mode
```bash
python main.py
```
Choose from the menu:
- **Option 2** (Analyze) - Works without API key
- **Option 4** (Tips) - See best practices
- **Option 1** (Optimize) - Requires API key

## Your First Prompt Optimization

1. Run: `python main.py`
2. Select option **2** (Analyze a prompt)
3. Enter a simple prompt like: "Write about dogs"
4. Press Enter twice to submit
5. See the analysis and suggestions!

## Example Session

```
$ python main.py

============================================================
                   🤖 AI Prompt Optimizer                    
     Enhance your prompts with AI-powered optimization      
============================================================

⚠️  Note: AI features require an OpenAI API key.
Local analysis features are still available.

Choose an option:
1. Optimize a prompt (AI-powered)
2. Analyze a prompt (local analysis)
3. Get AI suggestions
4. View prompt engineering tips
5. Exit

Your choice (1-5): 2

▶ Prompt Analysis Mode
----------------------------------------------------------------------
Enter your prompt (press Enter twice when done):
Write about dogs


▶ Prompt Analysis
----------------------------------------------------------------------

Length: 16 characters
Specificity: very low

Elements Present:
  ❌ Role Definition
  ✅ Context/Background
  ❌ Examples
  ❌ Constraints
  ❌ Output Format

Suggestions for Improvement:
  • Prompt is too short. Add more details.
  • Add a role definition to guide the AI's perspective.
  • Consider adding examples to clarify expectations.
  • Add constraints or requirements to focus the response.
  • Specify the desired output format.
```

## What's Next?

- 📚 Read [EXAMPLES.md](EXAMPLES.md) for detailed before/after comparisons
- 📖 Check [README.md](README.md) for full documentation
- 🤖 Set up your OpenAI API key to use AI-powered optimization
- 🎯 Start improving your prompts!

## Getting an OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Add it to your `.env` file:
   ```
   OPENAI_API_KEY=sk-your-key-here
   OPENAI_MODEL=gpt-4o-mini
   ```

## Troubleshooting

**Problem**: "Module not found" error
**Solution**: Run `pip install -r requirements.txt`

**Problem**: AI features don't work
**Solution**: Check that your `.env` file has a valid API key

**Problem**: Can't find .env file
**Solution**: Copy `.env.example` to `.env`: `cp .env.example .env`

## Features You Can Use Without API Key

- ✅ Prompt analysis
- ✅ Element detection
- ✅ Improvement suggestions
- ✅ Prompt engineering tips
- ✅ Demo and tests

## Features That Require API Key

- 🔑 AI-powered optimization
- 🔑 AI suggestions
- 🔑 Full prompt rewriting

---

**Ready to optimize your prompts? Run `python main.py` now!** 🚀
