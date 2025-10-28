"""
FastAPI Backend for AI Prompt Optimizer
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_engineer import PromptEngineer
from ai_optimizer import AIOptimizer

app = FastAPI(
    title="AI Prompt Optimizer API",
    description="API for optimizing prompts using AI and prompt engineering techniques",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://127.0.0.1:5173", "http://127.0.0.1:3000"],  # Vite default port and common React dev ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
prompt_engineer = PromptEngineer()
ai_optimizer = AIOptimizer()

# Request/Response Models
class PromptRequest(BaseModel):
    prompt: str

class AnalysisResponse(BaseModel):
    length: int
    specificity: str
    has_role: bool
    has_context: bool
    has_examples: bool
    has_constraints: bool
    has_format: bool
    suggestions: list[str]

class OptimizedPromptResponse(BaseModel):
    optimized_prompt: str
    analysis: AnalysisResponse

class SuggestionsResponse(BaseModel):
    suggestions: str

class TipsResponse(BaseModel):
    tips: list[str]

class HealthResponse(BaseModel):
    status: str
    ai_configured: bool

# API Endpoints
@app.get("/", response_model=dict)
async def root():
    """Root endpoint"""
    return {
        "message": "AI Prompt Optimizer API",
        "version": "1.0.0",
        "endpoints": {
            "/health": "Health check",
            "/analyze": "Analyze a prompt",
            "/optimize": "Optimize a prompt with AI",
            "/suggestions": "Get AI suggestions",
            "/tips": "Get prompt engineering tips"
        }
    }

@app.get("/health", response_model=HealthResponse)
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "ai_configured": ai_optimizer.is_configured()
    }

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_prompt(request: PromptRequest):
    """
    Analyze a prompt and provide feedback
    """
    if not request.prompt or not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    
    analysis = prompt_engineer.analyze_prompt(request.prompt)
    return analysis

@app.post("/optimize", response_model=OptimizedPromptResponse)
async def optimize_prompt(request: PromptRequest):
    """
    Optimize a prompt using AI
    """
    if not request.prompt or not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    
    if not ai_optimizer.is_configured():
        raise HTTPException(
            status_code=503,
            detail="AI optimization is not available. Please configure GEMINI_API_KEY."
        )
    
    # Analyze the prompt
    analysis = prompt_engineer.analyze_prompt(request.prompt)
    
    # Build optimization instructions
    optimization_instructions = prompt_engineer.build_optimized_prompt(request.prompt, analysis)
    
    # Get optimized prompt from AI
    optimized = ai_optimizer.optimize_prompt(optimization_instructions)
    
    if not optimized:
        raise HTTPException(status_code=500, detail="Failed to optimize prompt")
    
    return {
        "optimized_prompt": optimized,
        "analysis": analysis
    }

@app.post("/suggestions", response_model=SuggestionsResponse)
async def get_suggestions(request: PromptRequest):
    """
    Get AI-powered suggestions for improving a prompt
    """
    if not request.prompt or not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    
    if not ai_optimizer.is_configured():
        raise HTTPException(
            status_code=503,
            detail="AI suggestions are not available. Please configure GEMINI_API_KEY."
        )
    
    suggestions = ai_optimizer.get_suggestions(request.prompt)
    
    if not suggestions:
        raise HTTPException(status_code=500, detail="Failed to get suggestions")
    
    return {"suggestions": suggestions}

@app.get("/tips", response_model=TipsResponse)
async def get_tips():
    """
    Get prompt engineering tips
    """
    tips = prompt_engineer.get_engineering_tips()
    return {"tips": tips}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
