# Advanced JavaScript Examples

This directory contains advanced JavaScript examples demonstrating network access and API integration patterns for the AI Prompt Optimizer.

## Overview

The `advanced-examples.js` file showcases how to:
- Make network requests to AI APIs (Google Gemini)
- Fetch external resources and best practices
- Process prompts in batches with network calls
- Integrate with multiple AI services
- Implement real-time synchronization patterns

## Prerequisites

### Node.js Setup

1. Install Node.js (v14 or higher)
2. Install dependencies:
   ```bash
   npm install
   ```

### Configuration

The examples use the same `.env` configuration as the Python version:

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-pro
```

## Running the Examples

### Run all examples:
```bash
node advanced-examples.js
```

Or use npm:
```bash
npm test
```

### Make the script executable:
```bash
chmod +x advanced-examples.js
./advanced-examples.js
```

## Network Access Features

### Example 1: API-Based Prompt Optimization
Demonstrates making HTTP requests to the Google Gemini API to optimize prompts using AI.

**Network requirements:**
- Outbound HTTPS access to `generativelanguage.googleapis.com`
- Valid API key for authentication

### Example 2: Fetching Best Practices
Shows how to fetch prompt engineering tips and best practices from external resources.

**Network requirements:**
- HTTP/HTTPS access for external resources
- Optional: Access to knowledge bases and documentation sites

### Example 3: Batch Processing
Processes multiple prompts with network requests, demonstrating efficient batch operations.

**Network requirements:**
- Sustained network connectivity
- Rate limiting awareness

### Example 4: Network Synchronization
Illustrates real-time collaboration and data synchronization patterns.

**Network requirements:**
- WebSocket or polling capabilities
- Real-time data transmission

### Example 5: Multi-Service Integration
Shows integration patterns with multiple AI service providers.

**Network requirements:**
- Access to multiple API endpoints
- Support for different authentication methods

## Network Configuration

### Firewall Rules
Ensure the following outbound connections are allowed:
- `generativelanguage.googleapis.com` (port 443) - Google Gemini API
- Other AI service endpoints as needed

### Proxy Configuration
If behind a corporate proxy, configure Node.js to use it:

```bash
# Set proxy environment variables
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
```

Or in your code:
```javascript
const fetch = require('node-fetch');
const HttpsProxyAgent = require('https-proxy-agent');

const agent = new HttpsProxyAgent(process.env.HTTPS_PROXY);
fetch(url, { agent });
```

## Security Considerations

1. **API Keys**: Never commit API keys to version control
2. **HTTPS Only**: Always use HTTPS for API communication
3. **Rate Limiting**: Implement appropriate rate limiting for API calls
4. **Error Handling**: Handle network errors gracefully
5. **Timeouts**: Set reasonable timeouts for network requests

## Troubleshooting

### Network Access Issues

**Problem**: "Network request failed" or "ECONNREFUSED"
**Solution**: 
- Check your internet connection
- Verify firewall settings allow outbound HTTPS
- Ensure API endpoints are accessible

**Problem**: "API key invalid" or "401 Unauthorized"
**Solution**:
- Verify your API key in `.env` file
- Check that the API key is active and has proper permissions
- Ensure you're using the correct API endpoint

**Problem**: "Module not found"
**Solution**:
- Run `npm install` to install dependencies
- Check that `package.json` is present

### Dependencies

**Problem**: `node-fetch` errors
**Solution**:
- Ensure Node.js version 14 or higher
- For Node.js 18+, you can use native `fetch` (remove `require('node-fetch')`)

## Integration with Python Version

The JavaScript examples complement the Python implementation and can be used:

1. **Standalone**: Run independently for JavaScript/Node.js environments
2. **Hybrid**: Call JavaScript functions from Python using subprocess
3. **Microservices**: Deploy as separate services that communicate via APIs

Example Python integration:
```python
import subprocess
import json

def run_js_optimizer(prompt):
    result = subprocess.run(
        ['node', 'advanced-examples.js', prompt],
        capture_output=True,
        text=True
    )
    return result.stdout
```

## API Reference

### optimizePromptWithAPI(originalPrompt)
Optimizes a prompt using the Gemini API.
- **Parameters**: `originalPrompt` (string) - The prompt to optimize
- **Returns**: Promise<string> - The optimized prompt
- **Network**: Yes - Makes API call to Gemini

### fetchPromptEngineeringTips()
Fetches prompt engineering best practices.
- **Returns**: Promise<Array> - List of tips
- **Network**: Optional - Can fetch from external sources

### batchOptimizePrompts(prompts)
Processes multiple prompts in batch.
- **Parameters**: `prompts` (Array<string>) - Array of prompts
- **Returns**: Promise<Array> - Analysis results
- **Network**: Yes - Makes multiple API calls

### analyzePromptLocally(prompt)
Analyzes a prompt without network access.
- **Parameters**: `prompt` (string) - The prompt to analyze
- **Returns**: Object - Analysis results
- **Network**: No - Local processing only

## Contributing

When adding new examples:
1. Document network requirements
2. Include error handling for network failures
3. Add configuration options for endpoints
4. Update this README with new examples

## License

MIT License - Same as the main project

## Related Documentation

- [Main README](README.md) - Project overview
- [EXAMPLES.md](EXAMPLES.md) - Python examples
- [QUICKSTART.md](QUICKSTART.md) - Getting started guide
