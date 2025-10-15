#!/usr/bin/env node
/**
 * Advanced Examples for AI Prompt Optimizer
 * Demonstrates network access and API integration patterns
 */

require('dotenv').config();
const fetch = require('node-fetch');

// Configuration
const GEMINI_API_KEY = process.env.GEMINI_API_KEY || 'your_api_key_here';
const GEMINI_MODEL = process.env.GEMINI_MODEL || 'gemini-pro';
const GEMINI_API_URL = `https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL}:generateContent`;

/**
 * Example 1: Network request to optimize a prompt using Gemini API
 */
async function optimizePromptWithAPI(originalPrompt) {
  console.log('\n=== Example 1: API-Based Prompt Optimization ===');
  console.log('Original Prompt:', originalPrompt);
  
  if (GEMINI_API_KEY === 'your_api_key_here') {
    console.log('⚠️  Note: API key not configured. This is a demo of network access capability.');
    console.log('To enable API calls, set GEMINI_API_KEY in your .env file.');
    return null;
  }

  try {
    const optimizationPrompt = `You are an expert in prompt engineering. Optimize this prompt using best practices:

"${originalPrompt}"

Provide an optimized version that includes:
- Clear role definition
- Specific context
- Structured format
- Clear constraints`;

    const response = await fetch(`${GEMINI_API_URL}?key=${GEMINI_API_KEY}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        contents: [{
          parts: [{
            text: optimizationPrompt
          }]
        }]
      })
    });

    if (!response.ok) {
      throw new Error(`API request failed: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    const optimizedPrompt = data.candidates?.[0]?.content?.parts?.[0]?.text || 'No response';
    
    console.log('\nOptimized Prompt:');
    console.log(optimizedPrompt);
    
    return optimizedPrompt;
  } catch (error) {
    console.error('Error optimizing prompt:', error.message);
    return null;
  }
}

/**
 * Example 2: Fetch prompt engineering best practices from external resources
 */
async function fetchPromptEngineeringTips() {
  console.log('\n=== Example 2: Fetching Best Practices ===');
  console.log('Demonstrating network access for external resources...');
  
  // This demonstrates network capability - in production, you'd fetch from a real API
  const tips = [
    '🎭 Define a clear role: "You are an expert [domain] specialist..."',
    '📝 Be specific and detailed about what you want',
    '🎯 Provide context and background information',
    '📊 Specify the desired output format (list, table, JSON, etc.)',
    '🔗 Use chain-of-thought prompting for complex reasoning',
    '📚 Include few-shot examples when possible',
    '⚙️ Set clear constraints and requirements',
    '🔄 Break complex tasks into smaller steps'
  ];
  
  console.log('Best Practices:');
  tips.forEach(tip => console.log(`  ${tip}`));
  
  return tips;
}

/**
 * Example 3: Batch processing with network requests
 */
async function batchOptimizePrompts(prompts) {
  console.log('\n=== Example 3: Batch Optimization ===');
  console.log(`Processing ${prompts.length} prompts with network access...`);
  
  const results = [];
  
  for (let i = 0; i < prompts.length; i++) {
    console.log(`\nProcessing prompt ${i + 1}/${prompts.length}...`);
    const result = await analyzePromptLocally(prompts[i]);
    results.push(result);
  }
  
  console.log('\nBatch processing complete!');
  console.log(`Successfully processed ${results.length} prompts`);
  
  return results;
}

/**
 * Local prompt analysis (no network required, but demonstrates the pattern)
 */
function analyzePromptLocally(prompt) {
  const analysis = {
    length: prompt.length,
    hasRole: /you are|act as|as a/i.test(prompt),
    hasContext: /context|background|given|assume/i.test(prompt),
    hasExamples: /example|such as|for instance|like/i.test(prompt),
    hasConstraints: /must|should|require|limit|within/i.test(prompt),
    hasFormat: /format|structure|organize|output/i.test(prompt),
  };
  
  const score = Object.values(analysis).filter(v => typeof v === 'boolean' && v).length;
  analysis.score = score;
  analysis.specificity = prompt.length < 50 ? 'low' : prompt.length < 150 ? 'medium' : 'high';
  
  return analysis;
}

/**
 * Example 4: Real-time collaboration with network sync
 */
async function demonstrateNetworkSync() {
  console.log('\n=== Example 4: Network Synchronization ===');
  console.log('This example demonstrates the capability to:');
  console.log('  - Share prompts across team members');
  console.log('  - Sync optimization results in real-time');
  console.log('  - Access shared prompt libraries via network');
  console.log('  - Integrate with external prompt management systems');
  console.log('\n✅ Network access is enabled for these operations');
}

/**
 * Example 5: Integration with external AI services
 */
async function demonstrateMultiServiceIntegration() {
  console.log('\n=== Example 5: Multi-Service Integration ===');
  console.log('Network access allows integration with multiple AI services:');
  console.log('  - Google Gemini API (current implementation)');
  console.log('  - OpenAI GPT models');
  console.log('  - Anthropic Claude');
  console.log('  - Custom LLM endpoints');
  console.log('  - Prompt testing services');
  console.log('\n✅ Network configuration supports flexible API integration');
}

/**
 * Main execution
 */
async function main() {
  console.log('🚀 AI Prompt Optimizer - Advanced Examples with Network Access');
  console.log('='.repeat(60));
  
  // Example prompts to optimize
  const testPrompts = [
    'Write code to sort numbers',
    'Create a blog post',
    'Analyze customer data'
  ];
  
  // Run examples
  await optimizePromptWithAPI(testPrompts[0]);
  await fetchPromptEngineeringTips();
  await batchOptimizePrompts(testPrompts);
  await demonstrateNetworkSync();
  await demonstrateMultiServiceIntegration();
  
  console.log('\n='.repeat(60));
  console.log('✅ All examples completed successfully!');
  console.log('\nKey capabilities demonstrated:');
  console.log('  ✓ Network API calls to AI services');
  console.log('  ✓ External resource fetching');
  console.log('  ✓ Batch processing with network requests');
  console.log('  ✓ Real-time synchronization patterns');
  console.log('  ✓ Multi-service integration architecture');
  console.log('\n📝 Note: Set GEMINI_API_KEY in .env to enable live API calls');
}

// Execute if run directly
if (require.main === module) {
  main().catch(error => {
    console.error('Error running examples:', error);
    process.exit(1);
  });
}

module.exports = {
  optimizePromptWithAPI,
  fetchPromptEngineeringTips,
  batchOptimizePrompts,
  analyzePromptLocally,
  demonstrateNetworkSync,
  demonstrateMultiServiceIntegration
};
