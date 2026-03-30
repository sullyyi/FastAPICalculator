"""
FastAPI Calculator Application
Main application module with REST API endpoints for arithmetic operations.
"""

import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Union
import os

# Import operations
from operations import add, subtract, multiply, divide, power

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(title="Calculator API", version="1.0.0")

logger.info("FastAPI Calculator Application started")


class CalculationRequest(BaseModel):
    """Pydantic model for calculation requests"""
    a: Union[int, float]
    b: Union[int, float]


class CalculationResponse(BaseModel):
    """Pydantic model for calculation responses"""
    result: Union[int, float]
    operation: str


@app.get("/", response_class=HTMLResponse)
async def get_home():
    """Serve the home page with calculator interface"""
    logger.info("Home page requested")
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI Calculator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
                width: 100%;
                max-width: 400px;
            }
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 30px;
            }
            .input-group {
                margin-bottom: 15px;
            }
            label {
                display: block;
                margin-bottom: 5px;
                color: #555;
                font-weight: bold;
            }
            input {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
                box-sizing: border-box;
            }
            select {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
                box-sizing: border-box;
            }
            button {
                width: 100%;
                padding: 12px;
                background-color: #667eea;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            button:hover {
                background-color: #764ba2;
            }
            .result {
                margin-top: 20px;
                padding: 15px;
                background-color: #f0f0f0;
                border-radius: 5px;
                text-align: center;
                display: none;
            }
            .result.show {
                display: block;
            }
            .error {
                color: #d32f2f;
                margin-top: 10px;
                padding: 10px;
                background-color: #ffebee;
                border-radius: 5px;
                display: none;
            }
            .error.show {
                display: block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧮 FastAPI Calculator</h1>
            <div class="input-group">
                <label for="num1">First Number:</label>
                <input type="number" id="num1" step="0.01" placeholder="Enter first number">
            </div>
            <div class="input-group">
                <label for="operation">Operation:</label>
                <select id="operation">
                    <option value="add">Add (+)</option>
                    <option value="subtract">Subtract (-)</option>
                    <option value="multiply">Multiply (*)</option>
                    <option value="divide">Divide (/)</option>
                    <option value="power">Power (^)</option>
                </select>
            </div>
            <div class="input-group">
                <label for="num2">Second Number:</label>
                <input type="number" id="num2" step="0.01" placeholder="Enter second number">
            </div>
            <button onclick="calculate()">Calculate</button>
            <div id="error" class="error"></div>
            <div id="result" class="result">
                <h3>Result:</h3>
                <p id="resultValue" style="font-size: 24px; color: #667eea; font-weight: bold;"></p>
            </div>
        </div>

        <script>
            async function calculate() {
                const num1 = parseFloat(document.getElementById('num1').value);
                const num2 = parseFloat(document.getElementById('num2').value);
                const operation = document.getElementById('operation').value;
                
                const errorDiv = document.getElementById('error');
                const resultDiv = document.getElementById('result');
                
                errorDiv.classList.remove('show');
                resultDiv.classList.remove('show');
                
                if (isNaN(num1) || isNaN(num2)) {
                    errorDiv.textContent = 'Please enter valid numbers';
                    errorDiv.classList.add('show');
                    return;
                }
                
                try {
                    const response = await fetch(`/calculate/${operation}`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ a: num1, b: num2 })
                    });
                    
                    const data = await response.json();
                    
                    if (!response.ok) {
                        errorDiv.textContent = data.detail || 'Calculation failed';
                        errorDiv.classList.add('show');
                        return;
                    }
                    
                    document.getElementById('resultValue').textContent = data.result;
                    resultDiv.classList.add('show');
                } catch (error) {
                    errorDiv.textContent = 'Error: ' + error.message;
                    errorDiv.classList.add('show');
                }
            }
            
            // Allow Enter key to trigger calculation
            document.getElementById('num2').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') calculate();
            });
        </script>
    </body>
    </html>
    """


@app.post("/calculate/add", response_model=CalculationResponse)
async def calculate_add(request: CalculationRequest):
    """Add two numbers"""
    try:
        result = add(request.a, request.b)
        logger.info(f"Addition calculated: {request.a} + {request.b} = {result}")
        return CalculationResponse(result=result, operation="add")
    except Exception as e:
        logger.error(f"Error in add operation: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/calculate/subtract", response_model=CalculationResponse)
async def calculate_subtract(request: CalculationRequest):
    """Subtract two numbers"""
    try:
        result = subtract(request.a, request.b)
        logger.info(f"Subtraction calculated: {request.a} - {request.b} = {result}")
        return CalculationResponse(result=result, operation="subtract")
    except Exception as e:
        logger.error(f"Error in subtract operation: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/calculate/multiply", response_model=CalculationResponse)
async def calculate_multiply(request: CalculationRequest):
    """Multiply two numbers"""
    try:
        result = multiply(request.a, request.b)
        logger.info(f"Multiplication calculated: {request.a} * {request.b} = {result}")
        return CalculationResponse(result=result, operation="multiply")
    except Exception as e:
        logger.error(f"Error in multiply operation: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/calculate/divide", response_model=CalculationResponse)
async def calculate_divide(request: CalculationRequest):
    """Divide two numbers"""
    try:
        result = divide(request.a, request.b)
        logger.info(f"Division calculated: {request.a} / {request.b} = {result}")
        return CalculationResponse(result=result, operation="divide")
    except ValueError as e:
        logger.error(f"Division error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error in divide operation: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/calculate/power", response_model=CalculationResponse)
async def calculate_power(request: CalculationRequest):
    """Raise a number to a power"""
    try:
        result = power(request.a, request.b)
        logger.info(f"Power calculated: {request.a} ^ {request.b} = {result}")
        return CalculationResponse(result=result, operation="power")
    except Exception as e:
        logger.error(f"Error in power operation: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    logger.info("Health check requested")
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Uvicorn server")
    uvicorn.run(app, host="0.0.0.0", port=8000)
