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
from operations import add, subtract, multiply, divide, power, logarithm, gcd, lcm

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
                max-width: 450px;
            }
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 30px;
            }
            .info-box {
                background-color: #e3f2fd;
                border-left: 4px solid #667eea;
                padding: 12px;
                margin-bottom: 20px;
                border-radius: 4px;
                font-size: 13px;
                color: #1976d2;
                display: none;
            }
            .info-box.show {
                display: block;
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
            .label-help {
                font-size: 12px;
                color: #999;
                font-weight: normal;
                margin-left: 5px;
            }
            input {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
                box-sizing: border-box;
                transition: border-color 0.3s;
            }
            input:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
            }
            select {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
                box-sizing: border-box;
                transition: border-color 0.3s;
            }
            select:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
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
            button:active {
                transform: scale(0.98);
            }
            .result {
                margin-top: 20px;
                padding: 15px;
                background-color: #f0f0f0;
                border-radius: 5px;
                text-align: center;
                display: none;
                border-left: 4px solid #4caf50;
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
                border-left: 4px solid #d32f2f;
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
                <label for="operation">Operation:
                    <span class="label-help" id="helpText"></span>
                </label>
                <select id="operation" onchange="updateLabels()">
                    <option value="add">Add (+)</option>
                    <option value="subtract">Subtract (-)</option>
                    <option value="multiply">Multiply (*)</option>
                    <option value="divide">Divide (/)</option>
                    <option value="power">Power (^)</option>
                    <option value="logarithm">Logarithm (logₓ)</option>
                    <option value="gcd">GCD - Greatest Common Divisor</option>
                    <option value="lcm">LCM - Least Common Multiple</option>
                </select>
            </div>

            <div id="infoBox" class="info-box"></div>
            
            <div class="input-group">
                <label for="num1" id="label1">First Number:</label>
                <input type="number" id="num1" step="0.01" placeholder="Enter first number">
            </div>
            
            <div class="input-group">
                <label for="num2" id="label2">Second Number:</label>
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
            // Operation information and validation
            const operationInfo = {
                'add': {
                    label1: 'First Number:',
                    label2: 'Second Number:',
                    help: '',
                    info: '',
                    validate: () => true
                },
                'subtract': {
                    label1: 'First Number (a):',
                    label2: 'Second Number (b):',
                    help: '',
                    info: '',
                    validate: () => true
                },
                'multiply': {
                    label1: 'First Number:',
                    label2: 'Second Number:',
                    help: '',
                    info: '',
                    validate: () => true
                },
                'divide': {
                    label1: 'Numerator:',
                    label2: 'Denominator:',
                    help: '(cannot be 0)',
                    info: '',
                    validate: (num2) => num2 !== 0 ? true : false
                },
                'power': {
                    label1: 'Base:',
                    label2: 'Exponent:',
                    help: '',
                    info: '',
                    validate: () => true
                },
                'logarithm': {
                    label1: 'Argument:',
                    label2: 'Base:',
                    help: '(both > 0, base ≠ 1)',
                    info: 'ⓘ Logarithm requires positive argument and base (not equal to 1).',
                    validate: (num1, num2) => num1 > 0 && num2 > 0 && num2 !== 1
                },
                'gcd': {
                    label1: 'First Integer:',
                    label2: 'Second Integer:',
                    help: '(positive integers)',
                    info: 'ⓘ GCD requires positive integers only.',
                    validate: (num1, num2) => Number.isInteger(num1) && Number.isInteger(num2) && num1 > 0 && num2 > 0
                },
                'lcm': {
                    label1: 'First Integer:',
                    label2: 'Second Integer:',
                    help: '(positive integers)',
                    info: 'ⓘ LCM requires positive integers only.',
                    validate: (num1, num2) => Number.isInteger(num1) && Number.isInteger(num2) && num1 > 0 && num2 > 0
                }
            };

            function updateLabels() {
                const operation = document.getElementById('operation').value;
                const info = operationInfo[operation];
                
                document.getElementById('label1').textContent = info.label1;
                document.getElementById('label2').textContent = info.label2;
                document.getElementById('helpText').textContent = info.help;
                
                const infoBox = document.getElementById('infoBox');
                if (info.info) {
                    infoBox.textContent = info.info;
                    infoBox.classList.add('show');
                } else {
                    infoBox.classList.remove('show');
                }
                
                // Clear previous results
                document.getElementById('error').classList.remove('show');
                document.getElementById('result').classList.remove('show');
            }

            async function calculate() {
                const num1 = parseFloat(document.getElementById('num1').value);
                const num2 = parseFloat(document.getElementById('num2').value);
                const operation = document.getElementById('operation').value;
                
                const errorDiv = document.getElementById('error');
                const resultDiv = document.getElementById('result');
                const info = operationInfo[operation];
                
                errorDiv.classList.remove('show');
                resultDiv.classList.remove('show');
                
                // Basic validation
                if (isNaN(num1) || isNaN(num2)) {
                    errorDiv.textContent = '⚠ Please enter valid numbers';
                    errorDiv.classList.add('show');
                    return;
                }
                
                // Custom validation
                if (!info.validate(num1, num2)) {
                    let msg = 'Invalid input: ';
                    switch(operation) {
                        case 'divide':
                            msg += 'Cannot divide by zero';
                            break;
                        case 'logarithm':
                            msg += 'Argument must be > 0, base must be > 0 and ≠ 1';
                            break;
                        case 'gcd':
                        case 'lcm':
                            msg += 'Both values must be positive integers';
                            break;
                        default:
                            msg += 'Invalid input for this operation';
                    }
                    errorDiv.textContent = '⚠ ' + msg;
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
                        errorDiv.textContent = '⚠ ' + (data.detail || 'Calculation failed');
                        errorDiv.classList.add('show');
                        return;
                    }
                    
                    document.getElementById('resultValue').textContent = data.result;
                    resultDiv.classList.add('show');
                } catch (error) {
                    errorDiv.textContent = '⚠ Error: ' + error.message;
                    errorDiv.classList.add('show');
                }
            }
            
            // Allow Enter key to trigger calculation
            document.getElementById('num2').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') calculate();
            });
            
            // Initialize labels on page load
            updateLabels();
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


@app.post("/calculate/logarithm", response_model=CalculationResponse)
async def calculate_logarithm(request: CalculationRequest):
    """Calculate logarithm: a is the argument, b is the base"""
    try:
        result = logarithm(request.a, request.b)
        logger.info(f"Logarithm calculated: log_{request.b}({request.a}) = {result}")
        return CalculationResponse(result=result, operation="logarithm")
    except ValueError as e:
        logger.error(f"Logarithm error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error in logarithm operation: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/calculate/gcd", response_model=CalculationResponse)
async def calculate_gcd(request: CalculationRequest):
    """Calculate greatest common divisor"""
    try:
        result = gcd(request.a, request.b)
        logger.info(f"GCD calculated: gcd({request.a}, {request.b}) = {result}")
        return CalculationResponse(result=result, operation="gcd")
    except ValueError as e:
        logger.error(f"GCD error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error in gcd operation: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/calculate/lcm", response_model=CalculationResponse)
async def calculate_lcm(request: CalculationRequest):
    """Calculate least common multiple"""
    try:
        result = lcm(request.a, request.b)
        logger.info(f"LCM calculated: lcm({request.a}, {request.b}) = {result}")
        return CalculationResponse(result=result, operation="lcm")
    except ValueError as e:
        logger.error(f"LCM error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error in lcm operation: {str(e)}")
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
