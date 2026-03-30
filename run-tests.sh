#!/bin/bash

# FastAPI Calculator - Test Runner

echo "🧪 FastAPI Calculator - Test Suite"
echo "=================================="
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -q fastapi uvicorn pydantic jinja2 pytest pytest-asyncio httpx python-multipart

# Run unit tests
echo ""
echo "✅ Running Unit Tests (test_operations.py)..."
python -m pytest test_operations.py -v --tb=short

# Run integration tests
echo ""
echo "✅ Running Integration Tests (test_main.py)..."
python -m pytest test_main.py -v --tb=short

# Summary
echo ""
echo "=================================="
echo "✨ Test suite complete!"
echo ""
echo "To start the server:"
echo "  source venv/bin/activate"
echo "  uvicorn main:app --reload --port 8000"
echo ""
echo "Open browser to: http://localhost:8000"
