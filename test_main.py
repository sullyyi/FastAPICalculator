"""
Integration Tests for main.py
Tests all FastAPI endpoints for correct behavior and error handling.
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestHomeEndpoint:
    """Test suite for home endpoint"""
    
    def test_home_endpoint_returns_200(self):
        """Test home endpoint returns status 200"""
        response = client.get("/")
        assert response.status_code == 200
    
    def test_home_endpoint_returns_html(self):
        """Test home endpoint returns HTML content"""
        response = client.get("/")
        assert "text/html" in response.headers["content-type"]
        assert "FastAPI Calculator" in response.text
    
    def test_home_endpoint_has_calculator_ui(self):
        """Test home endpoint contains calculator UI elements"""
        response = client.get("/")
        assert "calculate()" in response.text
        assert "First Number" in response.text
        assert "Operation" in response.text


class TestHealthCheckEndpoint:
    """Test suite for health check endpoint"""
    
    def test_health_check_returns_200(self):
        """Test health check returns status 200"""
        response = client.get("/health")
        assert response.status_code == 200
    
    def test_health_check_returns_healthy_status(self):
        """Test health check returns healthy status"""
        response = client.get("/health")
        data = response.json()
        assert data["status"] == "healthy"


class TestAdditionEndpoint:
    """Test suite for addition endpoint"""
    
    def test_add_two_positive_numbers(self):
        """Test adding two positive numbers"""
        response = client.post(
            "/calculate/add",
            json={"a": 5, "b": 3}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 8
        assert data["operation"] == "add"
    
    def test_add_with_floats(self):
        """Test adding floating point numbers"""
        response = client.post(
            "/calculate/add",
            json={"a": 2.5, "b": 3.5}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 6.0
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        response = client.post(
            "/calculate/add",
            json={"a": -5, "b": -3}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == -8


class TestSubtractionEndpoint:
    """Test suite for subtraction endpoint"""
    
    def test_subtract_two_positive_numbers(self):
        """Test subtracting two positive numbers"""
        response = client.post(
            "/calculate/subtract",
            json={"a": 10, "b": 3}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 7
        assert data["operation"] == "subtract"
    
    def test_subtract_with_floats(self):
        """Test subtracting floating point numbers"""
        response = client.post(
            "/calculate/subtract",
            json={"a": 10.5, "b": 2.5}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 8.0
    
    def test_subtract_resulting_in_negative(self):
        """Test subtraction resulting in negative number"""
        response = client.post(
            "/calculate/subtract",
            json={"a": 3, "b": 10}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == -7


class TestMultiplicationEndpoint:
    """Test suite for multiplication endpoint"""
    
    def test_multiply_two_positive_numbers(self):
        """Test multiplying two positive numbers"""
        response = client.post(
            "/calculate/multiply",
            json={"a": 4, "b": 5}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 20
        assert data["operation"] == "multiply"
    
    def test_multiply_with_floats(self):
        """Test multiplying floating point numbers"""
        response = client.post(
            "/calculate/multiply",
            json={"a": 2.5, "b": 4.0}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 10.0
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        response = client.post(
            "/calculate/multiply",
            json={"a": 100, "b": 0}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 0


class TestDivisionEndpoint:
    """Test suite for division endpoint"""
    
    def test_divide_two_positive_numbers(self):
        """Test dividing two positive numbers"""
        response = client.post(
            "/calculate/divide",
            json={"a": 10, "b": 2}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 5
        assert data["operation"] == "divide"
    
    def test_divide_with_floats(self):
        """Test dividing floating point numbers"""
        response = client.post(
            "/calculate/divide",
            json={"a": 10.0, "b": 2.5}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 4.0
    
    def test_divide_by_zero_returns_error(self):
        """Test dividing by zero returns error"""
        response = client.post(
            "/calculate/divide",
            json={"a": 10, "b": 0}
        )
        assert response.status_code == 400
        data = response.json()
        assert "Cannot divide by zero" in data["detail"]
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number"""
        response = client.post(
            "/calculate/divide",
            json={"a": 0, "b": 5}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 0


class TestPowerEndpoint:
    """Test suite for power endpoint"""
    
    def test_power_positive_base_and_exponent(self):
        """Test raising positive number to positive power"""
        response = client.post(
            "/calculate/power",
            json={"a": 2, "b": 3}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 8
        assert data["operation"] == "power"
    
    def test_power_zero_exponent(self):
        """Test raising number to power of zero"""
        response = client.post(
            "/calculate/power",
            json={"a": 5, "b": 0}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 1
    
    def test_power_negative_exponent(self):
        """Test raising number to negative power"""
        response = client.post(
            "/calculate/power",
            json={"a": 2, "b": -1}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 0.5
    
    def test_power_negative_base_even_exponent(self):
        """Test raising negative number to even power"""
        response = client.post(
            "/calculate/power",
            json={"a": -2, "b": 2}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 4


class TestErrorHandling:
    """Test suite for error handling"""
    
    def test_invalid_json_returns_error(self):
        """Test invalid JSON returns error"""
        response = client.post(
            "/calculate/add",
            json={"invalid": "data"}
        )
        assert response.status_code == 422  # Validation error
    
    def test_missing_parameters_returns_error(self):
        """Test missing parameters returns error"""
        response = client.post(
            "/calculate/add",
            json={"a": 5}
        )
        assert response.status_code == 422
    
    def test_string_instead_of_number_returns_error(self):
        """Test string instead of number returns validation error"""
        response = client.post(
            "/calculate/add",
            json={"a": "five", "b": "three"}
        )
        assert response.status_code == 422


class TestResponseFormat:
    """Test suite for response format"""
    
    def test_response_has_required_fields(self):
        """Test response has required fields"""
        response = client.post(
            "/calculate/add",
            json={"a": 5, "b": 3}
        )
        data = response.json()
        assert "result" in data
        assert "operation" in data
        assert len(data) == 2
    
    def test_response_content_type(self):
        """Test response has correct content type"""
        response = client.post(
            "/calculate/add",
            json={"a": 5, "b": 3}
        )
        assert "application/json" in response.headers["content-type"]
