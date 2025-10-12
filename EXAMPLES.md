# Usage Examples

This document provides examples of how the Prompt Optimizer improves prompts using prompt engineering techniques.

## Example 1: Basic Query to Comprehensive Prompt

### Original Prompt
```
Write about dogs
```

### Issues Identified
- Too short (16 characters)
- No role definition
- No context provided
- No examples given
- No constraints specified
- No output format specified

### Optimized Version
```
You are an expert veterinarian and animal behaviorist with 15 years of experience working with various dog breeds.

Write a comprehensive, informative guide about dogs that covers the following topics:

1. **Popular Breeds**: Describe 5-7 common dog breeds, their characteristics, temperament, and ideal living conditions
2. **Care Requirements**: 
   - Daily feeding guidelines based on size and age
   - Grooming needs for different coat types
   - Exercise requirements and activity recommendations
3. **Health and Wellness**:
   - Common health issues and preventive measures
   - Vaccination schedules
   - Signs of illness to watch for
4. **Training Fundamentals**:
   - Basic commands and how to teach them
   - Positive reinforcement techniques
   - Addressing common behavioral problems
5. **The Human-Dog Bond**:
   - Benefits of dog ownership
   - Building trust and companionship
   - Understanding dog body language

**Target Audience**: First-time dog owners
**Tone**: Friendly, informative, and encouraging
**Format**: Well-structured article with clear sections, subheadings, and bullet points
**Length**: 1000-1200 words
**Requirements**: 
- Use simple, accessible language
- Include practical, actionable advice
- Cite reliable sources when mentioning health information
- Avoid technical jargon without explanation
```

## Example 2: Code Request Enhancement

### Original Prompt
```
Create a function to sort numbers
```

### Optimized Version
```
You are an expert Python developer specializing in algorithm optimization and clean code practices.

Create a Python function that sorts a list of numbers with the following specifications:

**Function Requirements**:
1. Function name: `sort_numbers`
2. Input: A list of integers (can be positive, negative, or zero)
3. Output: A new sorted list in ascending order (do not modify the original list)
4. Handle edge cases: empty lists, single-element lists, already sorted lists

**Implementation Guidelines**:
- Use Python's built-in sorting capabilities
- Include comprehensive docstring with Google-style documentation
- Add type hints for parameters and return value
- Include input validation
- Optimize for readability over performance

**Deliverables**:
1. The function implementation
2. At least 3 test cases demonstrating:
   - Normal case with unsorted numbers
   - Edge case with empty list
   - Edge case with negative numbers

**Example Usage**:
```python
numbers = [5, 2, 9, 1, 7]
sorted_nums = sort_numbers(numbers)
print(sorted_nums)  # Output: [1, 2, 5, 7, 9]
print(numbers)      # Output: [5, 2, 9, 1, 7] (original unchanged)
```

**Code Style**: Follow PEP 8 guidelines
```

## Example 3: Content Creation Task

### Original Prompt
```
Write a blog post
```

### Optimized Version
```
You are an experienced content marketer and blogger with expertise in creating engaging, SEO-optimized content for technology audiences.

Write a blog post about the impact of artificial intelligence on modern software development.

**Content Structure**:
1. **Compelling Headline**: Create an attention-grabbing title (60-70 characters)
2. **Introduction** (150-200 words):
   - Hook the reader with a relevant statistic or question
   - Briefly outline what the post will cover
3. **Main Body** (800-1000 words):
   - Section 1: AI-powered development tools (code completion, debugging)
   - Section 2: Automated testing and quality assurance
   - Section 3: Impact on developer productivity
   - Section 4: Challenges and considerations
4. **Conclusion** (100-150 words):
   - Summarize key points
   - Include a call-to-action

**Writing Guidelines**:
- Tone: Professional yet conversational
- Target audience: Software developers and tech managers
- Reading level: Intermediate (familiar with basic tech concepts)
- Include 2-3 real-world examples or case studies
- Use subheadings for easy scanning
- Incorporate bullet points and numbered lists where appropriate

**SEO Requirements**:
- Primary keyword: "AI in software development" (use 3-5 times naturally)
- Include 2-3 related keywords: "machine learning", "developer productivity", "automated testing"
- Meta description: Write a compelling 150-160 character summary

**Constraints**:
- Total word count: 1200-1400 words
- Avoid overly technical jargon
- Keep paragraphs to 3-4 sentences maximum
- Include actionable takeaways for readers
```

## Example 4: Data Analysis Request

### Original Prompt
```
Analyze this data
```

### Optimized Version
```
You are a senior data analyst with 10 years of experience in statistical analysis and data visualization.

**Context**: I have a dataset containing customer purchase information from an e-commerce website for the past 12 months.

**Dataset Structure**:
- Columns: customer_id, purchase_date, product_category, amount_spent, customer_age, location
- Rows: Approximately 50,000 transactions
- Format: CSV file

**Analysis Requirements**:
1. **Descriptive Statistics**:
   - Calculate mean, median, and standard deviation for amount_spent
   - Identify the most and least popular product categories
   - Determine peak purchase periods (monthly and weekly patterns)

2. **Customer Segmentation**:
   - Group customers by spending behavior (low, medium, high spenders)
   - Analyze age demographics for each segment
   - Identify geographic patterns in purchasing

3. **Insights and Recommendations**:
   - Identify trends and patterns in the data
   - Highlight any anomalies or unexpected findings
   - Provide 3-5 actionable business recommendations

**Output Format**:
- Executive summary (2-3 paragraphs)
- Detailed findings organized by analysis requirement
- Visualization recommendations (describe what charts/graphs would be most effective)
- Methodology explanation (what statistical methods you would use and why)

**Constraints**:
- Focus on practical business insights
- Explain technical concepts in simple terms
- Prioritize findings with the highest business impact
- Suggest tools or approaches for implementation

**Deliverable**: A comprehensive analysis report suitable for presentation to non-technical stakeholders.
```

## Key Improvements Applied

All optimized prompts incorporate these prompt engineering principles:

1. ✅ **Role Definition**: Clear expertise and perspective
2. ✅ **Context**: Relevant background information
3. ✅ **Specificity**: Detailed requirements and expectations
4. ✅ **Structure**: Organized, easy-to-follow format
5. ✅ **Constraints**: Boundaries and limitations
6. ✅ **Output Format**: Desired structure and presentation
7. ✅ **Examples**: Concrete illustrations when helpful
8. ✅ **Quality Criteria**: Standards for evaluation

## Tips for Using the Optimizer

1. **Start Simple**: Input your basic prompt idea
2. **Review Analysis**: Check what elements are missing
3. **Apply Suggestions**: Use the optimized version as a template
4. **Customize**: Adjust the optimized prompt to your specific needs
5. **Iterate**: Run multiple variations if needed
6. **Learn**: Notice patterns in what makes prompts effective

## Common Prompt Patterns

### For Code Generation
```
You are [language] expert...
Create [specific item]...
Requirements: [bullet points]
Include: [tests/docs/examples]
```

### For Content Writing
```
You are [role] with expertise in [domain]...
Write [content type] about [topic]...
Structure: [sections]
Tone: [style]
Length: [word count]
```

### For Analysis Tasks
```
You are [analyst type]...
Context: [background]
Data: [description]
Analyze: [specific aspects]
Output: [format and depth]
```

### For Problem Solving
```
You are [expert role]...
Problem: [clear description]
Constraints: [limitations]
Approach: [methodology]
Solution should: [criteria]
```
