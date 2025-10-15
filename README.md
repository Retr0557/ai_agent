# 🤖 AI Prompt Optimizer

An intelligent prompt optimization tool that uses AI and prompt engineering techniques to transform basic prompts into highly effective, well-structured prompts.

## ✨ Features

- **AI-Powered Optimization**: Uses Google's Gemini AI models to intelligently optimize prompts
- **Comprehensive Analysis**: Analyzes prompts for key elements like role definition, context, examples, and constraints
- **Prompt Engineering Techniques**: Applies industry-standard prompt engineering best practices:
  - Role-based prompting
  - Context enhancement
  - Task decomposition
  - Chain-of-thought prompting
  - Few-shot examples
  - Output format specification
  - Constraint definition
- **Interactive CLI**: User-friendly command-line interface with colored output
- **Local Analysis Mode**: Works without API key for basic analysis
- **AI Suggestions**: Get specific, actionable improvement suggestions

## 🚀 Quick Start

> **📖 New to this project? Check out [QUICKSTART.md](QUICKSTART.md) for a 3-minute guided setup!**

### Automated Setup (Recommended)

Use the helper script for easy setup:
```bash
./setup.sh
```

Or use specific commands:
```bash
./setup.sh install  # Install dependencies
./setup.sh setup    # Create .env file
./setup.sh demo     # Run demo
./setup.sh test     # Run tests
./setup.sh run      # Run the app
```

### Manual Setup

#### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (optional, but required for AI features)

#### Installation

1. Clone the repository:
```bash
git clone https://github.com/Retr0557/ai_agent.git
cd ai_agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure API key (optional):
```bash
cp .env.example .env
# Edit .env and add your Google Gemini API key
```

### Usage

**Interactive Mode:**
```bash
python main.py
```

Follow the interactive menu to:
1. **Optimize a prompt** - AI-powered full optimization
2. **Analyze a prompt** - Local analysis without API
3. **Get AI suggestions** - Specific improvement recommendations
4. **View tips** - Learn prompt engineering best practices

**Demo Mode:**
```bash
python demo.py
```

**Run Tests:**
```bash
python test_optimizer.py
```

## 📝 Example

**Original Prompt:**
```
Write about dogs
```

**Optimized Prompt:**
```
You are an expert veterinarian and animal behaviorist with 15 years of experience. 
Write a comprehensive, informative article about dogs that covers:

1. Different breeds and their characteristics
2. Basic care requirements (feeding, grooming, exercise)
3. Common health issues and prevention
4. Training fundamentals and behavioral insights
5. The human-dog bond and its benefits

Target Audience: First-time dog owners
Tone: Friendly, informative, and encouraging
Format: Well-structured article with clear sections and bullet points where appropriate
Length: 800-1000 words

Please ensure the content is accurate, practical, and accessible to beginners.
```

## 🎯 Prompt Engineering Techniques

The app implements these key techniques:

1. **Role Definition** - Establish expertise and perspective
2. **Context Provision** - Add relevant background information
3. **Specificity** - Clear, detailed requirements
4. **Structure** - Organized, step-by-step instructions
5. **Constraints** - Boundaries and requirements
6. **Format Specification** - Desired output structure
7. **Examples** - Few-shot learning when applicable
8. **Quality Criteria** - Standards for output

## 🛠️ Configuration

### Environment Variables

Create a `.env` file with:
```
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-pro
```

Supported models:
- `gemini-pro` (default, recommended)
- `gemini-1.5-pro`
- `gemini-1.5-flash`

## 📁 Project Structure

```
ai_agent/
├── main.py              # Main application entry point
├── prompt_engineer.py   # Prompt engineering logic and analysis
├── ai_optimizer.py      # AI integration module
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment configuration
├── .gitignore          # Git ignore patterns
└── README.md           # Documentation
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Links

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## 💡 Tips for Best Results

- Be specific about what you want
- Provide context and background
- Define the role or perspective
- Specify output format and constraints
- Include examples when possible
- Use the analysis feature to understand gaps in your prompts
