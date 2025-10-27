# Web Application Setup Guide

This guide explains how to run the AI Prompt Optimizer as a web application with FastAPI backend and React frontend.

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn
- Google Gemini API key (optional, for AI features)

## Backend Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API key (optional):**
   ```bash
   cp .env.example .env
   # Edit .env and add your Google Gemini API key
   ```

3. **Start the FastAPI backend:**
   ```bash
   cd backend
   uvicorn api:app --host 0.0.0.0 --port 8001 --reload
   ```
   
   Or from the project root:
   ```bash
   uvicorn backend.api:app --host 0.0.0.0 --port 8001 --reload
   ```

   The API will be available at `http://localhost:8001`
   - API documentation: `http://localhost:8001/docs`
   - Alternative API docs: `http://localhost:8001/redoc`

## Frontend Setup

1. **Install frontend dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start the React development server:**
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173`

## Running Both Together

You can run both backend and frontend simultaneously in different terminal windows:

**Terminal 1 - Backend:**
```bash
uvicorn backend.api:app --host 0.0.0.0 --port 8001 --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend && npm run dev
```

Then open your browser to `http://localhost:5173`

## Features

The web application provides the same features as the CLI:

1. **Optimize** - AI-powered full prompt optimization
2. **Analyze** - Local analysis without API (no key required)
3. **Suggestions** - Get AI suggestions for improvement
4. **Tips** - View prompt engineering best practices

## API Endpoints

- `GET /` - API information
- `GET /health` - Health check and AI configuration status
- `POST /analyze` - Analyze a prompt (no API key required)
- `POST /optimize` - Optimize a prompt with AI (requires API key)
- `POST /suggestions` - Get AI suggestions (requires API key)
- `GET /tips` - Get prompt engineering tips

## Building for Production

### Backend
The FastAPI backend is ready for production deployment. You can use:
- Docker
- WSGI server like gunicorn with uvicorn workers
- Cloud platforms (AWS, GCP, Azure, Heroku, etc.)

### Frontend
Build the React frontend for production:
```bash
cd frontend
npm run build
```

The production-ready files will be in `frontend/dist/`

You can serve them with any static file server or integrate with your backend.

## Troubleshooting

### CORS Issues
If you encounter CORS errors, ensure:
1. Backend is running on port 8001
2. Frontend is running on port 5173
3. The CORS middleware in `backend/api.py` includes your frontend URL

### API Key Issues
- The Analyze and Tips features work without an API key
- Optimize and Suggestions require a valid Google Gemini API key
- Check the health status indicator in the UI to see if AI is configured

### Port Conflicts
If ports 8001 or 5173 are in use:
- Backend: Change the port in the uvicorn command
- Frontend: Change the port in `vite.config.js`
- Update CORS settings in `backend/api.py` to match new ports
- Update `API_BASE_URL` in `frontend/src/App.jsx` if backend port changes
