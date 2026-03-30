# FastAPI Calculator Application

A modern, fully-tested FastAPI web application that provides a user-friendly calculator with REST API endpoints and comprehensive test coverage.

## Features

- **REST API Endpoints** for arithmetic operations (add, subtract, multiply, divide, power)
- **Interactive Web UI** with modern, responsive design
- **Comprehensive Testing**:
  - Unit tests for all operations
  - Integration tests for all API endpoints
  - End-to-end tests using Playwright
- **Logging** throughout the application for operations tracking and error reporting
- **GitHub Actions CI/CD** for automated testing on every push
- **Professional Code Quality** with proper error handling and validation

## Project Structure

```
fastapi-calculator/
├── main.py                 # FastAPI application with endpoints
├── operations.py           # Core arithmetic operations
├── test_operations.py      # Unit tests for operations
├── test_main.py           # Integration tests for API endpoints
├── test_e2e.py            # End-to-end tests with Playwright
├── requirements.txt       # Python dependencies
├── pytest.ini            # Pytest configuration
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI/CD workflow
└── README.md             # This file
```

## Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd fastapi-calculator
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers** (for E2E tests)
```bash
playwright install
```

## Running the Application

### Start the FastAPI Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The application will be available at `http://localhost:8000`

### Run with Python directly

```bash
python main.py
```

## Testing

### Run All Tests

```bash
pytest -v
```

### Run Unit Tests Only

```bash
pytest test_operations.py -v
```

### Run Integration Tests Only

```bash
pytest test_main.py -v
```

### Run End-to-End Tests Only

```bash
pytest test_e2e.py -v
```

### Run Tests with Coverage

```bash
pip install pytest-cov
pytest --cov=. --cov-report=html
```

## API Endpoints

### Home Page
- **GET** `/` - Returns the calculator web interface

### Health Check
- **GET** `/health` - Returns server health status

### Addition
- **POST** `/calculate/add`
- Request: `{"a": 5, "b": 3}`
- Response: `{"result": 8, "operation": "add"}`

### Subtraction
- **POST** `/calculate/subtract`
- Request: `{"a": 10, "b": 3}`
- Response: `{"result": 7, "operation": "subtract"}`

### Multiplication
- **POST** `/calculate/multiply`
- Request: `{"a": 4, "b": 5}`
- Response: `{"result": 20, "operation": "multiply"}`

### Division
- **POST** `/calculate/divide`
- Request: `{"a": 10, "b": 2}`
- Response: `{"result": 5.0, "operation": "divide"}`
- Error (divide by zero): `{"detail": "Cannot divide by zero"}`

### Power
- **POST** `/calculate/power`
- Request: `{"a": 2, "b": 3}`
- Response: `{"result": 8, "operation": "power"}`

## Test Coverage

### Unit Tests (test_operations.py)
- Addition: 5 tests (positive, negative, mixed, floats, zero)
- Subtraction: 5 tests
- Multiplication: 6 tests
- Division: 7 tests (including divide by zero)
- Power: 7 tests
- Edge cases: 3 tests
- **Total: 33 unit tests**

### Integration Tests (test_main.py)
- Home endpoint: 3 tests
- Health check: 2 tests
- Addition endpoint: 3 tests
- Subtraction endpoint: 3 tests
- Multiplication endpoint: 3 tests
- Division endpoint: 4 tests
- Power endpoint: 4 tests
- Error handling: 3 tests
- Response format: 2 tests
- **Total: 27 integration tests**

### End-to-End Tests (test_e2e.py)
- Page load: 1 test
- UI elements: 1 test
- Add operation: 1 test
- Subtract operation: 1 test
- Multiply operation: 1 test
- Divide operation: 1 test
- Power operation: 1 test
- Divide by zero error: 1 test
- Floating point: 1 test
- Negative numbers: 1 test
- Enter key: 1 test
- **Total: 11 end-to-end tests**

**Grand Total: 71 Tests**

## Logging

The application uses Python's standard `logging` module configured at the INFO level. Logs capture:
- Application startup events
- All calculation operations
- API endpoint requests
- Error conditions
- Division by zero attempts

Example log output:
```
2026-03-30 19:00:00,123 - main - INFO - FastAPI Calculator Application started
2026-03-30 19:00:15,456 - operations - INFO - Addition: 5 + 3 = 8
2026-03-30 19:00:20,789 - main - INFO - Addition calculated: 5 + 3 = 8
```

## GitHub Actions CI/CD

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that:
1. Runs on every push to main or develop branches
2. Runs on pull requests
3. Executes all unit tests
4. Executes all integration tests
5. Starts the FastAPI server and runs E2E tests
6. Uploads test results as artifacts
7. Provides detailed test reports

## Continuous Improvement

To keep this project well-maintained:
1. Run tests before each commit
2. Review GitHub Actions results
3. Keep dependencies updated
4. Add new tests for new features
5. Monitor and improve code coverage

## Development

### Running Tests During Development

Use pytest watch for continuous testing:
```bash
pip install pytest-watch
ptw -- -v
```

### Code Quality

The project follows Python best practices:
- Type hints for function arguments and returns
- Comprehensive docstrings
- Proper error handling
- Logging throughout
- Clean code structure

## Troubleshooting

### E2E Tests Fail Locally
- Ensure the FastAPI server is running on port 8000
- Playwright browsers might need updating: `playwright install --with-deps`

### Import Errors
- Verify virtual environment is activated
- Run `pip install -r requirements.txt` again

### Port Already in Use
- Change the port in `main.py` or use: `lsof -i :8000` to find and kill the process

## License

This project is part of the NJIT IS601004 course on Python for Web API Development.

## Learning Outcomes

This project addresses the following course learning outcomes:
- **CLO7**: Apply professional terminology and concepts related to web systems development
- **CLO10**: Create, Consume and Test REST APIs using Python

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Playwright Documentation](https://playwright.dev/python/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
