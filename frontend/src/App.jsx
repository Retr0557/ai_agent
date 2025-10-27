import { useState } from 'react'
import './App.css'

const API_BASE_URL = 'http://localhost:8001'

function App() {
  const [activeTab, setActiveTab] = useState('optimize')
  const [prompt, setPrompt] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [tips, setTips] = useState([])
  const [healthStatus, setHealthStatus] = useState(null)

  // Fetch health status on mount
  useState(() => {
    fetchHealth()
  }, [])

  const fetchHealth = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/health`)
      const data = await response.json()
      setHealthStatus(data)
    } catch (err) {
      console.error('Health check failed:', err)
    }
  }

  const handleAnalyze = async () => {
    if (!prompt.trim()) {
      setError('Please enter a prompt')
      return
    }

    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch(`${API_BASE_URL}/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      })

      if (!response.ok) {
        throw new Error('Failed to analyze prompt')
      }

      const data = await response.json()
      setResult({ type: 'analysis', data })
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleOptimize = async () => {
    if (!prompt.trim()) {
      setError('Please enter a prompt')
      return
    }

    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch(`${API_BASE_URL}/optimize`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Failed to optimize prompt')
      }

      const data = await response.json()
      setResult({ type: 'optimize', data })
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleGetSuggestions = async () => {
    if (!prompt.trim()) {
      setError('Please enter a prompt')
      return
    }

    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch(`${API_BASE_URL}/suggestions`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Failed to get suggestions')
      }

      const data = await response.json()
      setResult({ type: 'suggestions', data })
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleGetTips = async () => {
    setLoading(true)
    setError(null)

    try {
      const response = await fetch(`${API_BASE_URL}/tips`)

      if (!response.ok) {
        throw new Error('Failed to get tips')
      }

      const data = await response.json()
      setTips(data.tips)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const renderAnalysis = (analysis) => {
    return (
      <div className="analysis-result">
        <h3>📊 Prompt Analysis</h3>
        <div className="analysis-stats">
          <div className="stat">
            <span className="label">Length:</span>
            <span className="value">{analysis.length} characters</span>
          </div>
          <div className="stat">
            <span className="label">Specificity:</span>
            <span className={`value specificity-${analysis.specificity.replace(' ', '-')}`}>
              {analysis.specificity}
            </span>
          </div>
        </div>
        <div className="analysis-elements">
          <h4>Elements Present:</h4>
          <ul>
            <li className={analysis.has_role ? 'present' : 'missing'}>
              {analysis.has_role ? '✅' : '❌'} Role Definition
            </li>
            <li className={analysis.has_context ? 'present' : 'missing'}>
              {analysis.has_context ? '✅' : '❌'} Context/Background
            </li>
            <li className={analysis.has_examples ? 'present' : 'missing'}>
              {analysis.has_examples ? '✅' : '❌'} Examples
            </li>
            <li className={analysis.has_constraints ? 'present' : 'missing'}>
              {analysis.has_constraints ? '✅' : '❌'} Constraints
            </li>
            <li className={analysis.has_format ? 'present' : 'missing'}>
              {analysis.has_format ? '✅' : '❌'} Output Format
            </li>
          </ul>
        </div>
        {analysis.suggestions && analysis.suggestions.length > 0 && (
          <div className="suggestions">
            <h4>💡 Suggestions for Improvement:</h4>
            <ul>
              {analysis.suggestions.map((suggestion, index) => (
                <li key={index}>{suggestion}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    )
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>🤖 AI Prompt Optimizer</h1>
        <p>Enhance your prompts with AI-powered optimization</p>
        {healthStatus && (
          <div className={`health-status ${healthStatus.ai_configured ? 'configured' : 'not-configured'}`}>
            {healthStatus.ai_configured ? '✅' : '⚠️'} AI {healthStatus.ai_configured ? 'Configured' : 'Not Configured'}
          </div>
        )}
      </header>

      <div className="main-content">
        <div className="tabs">
          <button
            className={`tab ${activeTab === 'optimize' ? 'active' : ''}`}
            onClick={() => setActiveTab('optimize')}
          >
            Optimize
          </button>
          <button
            className={`tab ${activeTab === 'analyze' ? 'active' : ''}`}
            onClick={() => setActiveTab('analyze')}
          >
            Analyze
          </button>
          <button
            className={`tab ${activeTab === 'suggestions' ? 'active' : ''}`}
            onClick={() => setActiveTab('suggestions')}
          >
            Suggestions
          </button>
          <button
            className={`tab ${activeTab === 'tips' ? 'active' : ''}`}
            onClick={() => setActiveTab('tips')}
          >
            Tips
          </button>
        </div>

        <div className="content-area">
          {activeTab !== 'tips' && (
            <div className="input-section">
              <label htmlFor="prompt-input">Enter your prompt:</label>
              <textarea
                id="prompt-input"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                placeholder="e.g., Write about dogs..."
                rows={6}
              />
              <div className="action-buttons">
                {activeTab === 'optimize' && (
                  <button onClick={handleOptimize} disabled={loading} className="primary-button">
                    {loading ? 'Optimizing...' : '✨ Optimize Prompt'}
                  </button>
                )}
                {activeTab === 'analyze' && (
                  <button onClick={handleAnalyze} disabled={loading} className="primary-button">
                    {loading ? 'Analyzing...' : '🔍 Analyze Prompt'}
                  </button>
                )}
                {activeTab === 'suggestions' && (
                  <button onClick={handleGetSuggestions} disabled={loading} className="primary-button">
                    {loading ? 'Getting Suggestions...' : '💡 Get Suggestions'}
                  </button>
                )}
              </div>
            </div>
          )}

          {activeTab === 'tips' && (
            <div className="tips-section">
              <button onClick={handleGetTips} disabled={loading} className="primary-button">
                {loading ? 'Loading...' : '📚 Load Tips'}
              </button>
              {tips.length > 0 && (
                <div className="tips-list">
                  <h3>Prompt Engineering Tips</h3>
                  <ul>
                    {tips.map((tip, index) => (
                      <li key={index}>{tip}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}

          {error && (
            <div className="error-message">
              ❌ {error}
            </div>
          )}

          {result && (
            <div className="result-section">
              {result.type === 'analysis' && renderAnalysis(result.data)}
              
              {result.type === 'optimize' && (
                <div className="optimize-result">
                  <h3>✨ Optimized Prompt</h3>
                  <div className="optimized-prompt">
                    {result.data.optimized_prompt}
                  </div>
                  {renderAnalysis(result.data.analysis)}
                </div>
              )}
              
              {result.type === 'suggestions' && (
                <div className="suggestions-result">
                  <h3>💡 AI Suggestions</h3>
                  <div className="suggestions-content">
                    {result.data.suggestions}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default App
