"""
End-to-End Tests using Playwright
Tests user interactions with the calculator through the web browser.
"""

import pytest
import asyncio
from playwright.async_api import async_playwright


@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
async def test_calculator_page_loads():
    """Test that calculator page loads successfully"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/", wait_until="domcontentloaded")
        
        title = await page.title()
        assert "FastAPI Calculator" in title
        
        await browser.close()


@pytest.mark.asyncio
async def test_calculator_ui_elements_present():
    """Test that all calculator UI elements are present"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/", wait_until="domcontentloaded")
        
        # Check for input fields
        num1_input = await page.locator("#num1")
        num2_input = await page.locator("#num2")
        operation_select = await page.locator("#operation")
        calculate_button = await page.locator("button")
        
        assert await num1_input.count() > 0
        assert await num2_input.count() > 0
        assert await operation_select.count() > 0
        assert await calculate_button.count() > 0
        
        await browser.close()


@pytest.mark.asyncio
async def test_add_operation():
    """Test addition operation through UI"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/", wait_until="domcontentloaded")
        
        # Fill in the form
        await page.locator("#num1").fill("10")
        await page.locator("#num2").fill("5")
        await page.locator("#operation").select_option("add")
        
        # Click calculate
        await page.locator("button").click()
        
        # Wait for result and verify
        result_div = page.locator("#resultValue")
        await result_div.wait_for()
        result_text = await result_div.text_content()
        assert "15" in result_text
        
        await browser.close()


@pytest.mark.asyncio
async def test_subtract_operation():
    """Test subtraction operation through UI"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/", wait_until="domcontentloaded")
        
        # Fill in the form
        await page.locator("#num1").fill("20")
        await page.locator("#num2").fill("8")
        await page.locator("#operation").select_option("subtract")
        
        # Click calculate
        await page.locator("button").click()
        
        # Wait for result and verify
        result_div = page.locator("#resultValue")
        await result_div.wait_for()
        result_text = await result_div.text_content()
        assert "12" in result_text
        
        await browser.close()


@pytest.mark.asyncio
async def test_multiply_operation():
    """Test multiplication operation through UI"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/", wait_until="domcontentloaded")
        
        # Fill in the form
        await page.locator("#num1").fill("7")
        await page.locator("#num2").fill("6")
        await page.locator("#operation").select_option("multiply")
        
        # Click calculate
        await page.locator("button").click()
        
        # Wait for result and verify
        result_div = page.locator("#resultValue")
        await result_div.wait_for()
        result_text = await result_div.text_content()
        assert "42" in result_text
        
        await browser.close()


@pytest.mark.asyncio
async def test_divide_operation():
    """Test division operation through UI"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/", wait_until="domcontentloaded")
        
        # Fill in the form
        await page.locator("#num1").fill("24")
        await page.locator("#num2").fill("4")
        await page.locator("#operation").select_option("divide")
        
        # Click calculate
        await page.locator("button").click()
        
        # Wait for result and verify
        result_div = page.locator("#resultValue")
        await result_div.wait_for()
        result_text = await result_div.text_content()
        assert "6" in result_text
        
        await browser.close()


@pytest.mark.asyncio
async def test_power_operation():
    """Test power operation through UI"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/", wait_until="domcontentloaded")
        
        # Fill in the form
        await page.locator("#num1").fill("2")
        await page.locator("#num2").fill("10")
        await page.locator("#operation").select_option("power")
        
        # Click calculate
        await page.locator("button").click()
        
        # Wait for result and verify
        result_div = page.locator("#resultValue")
        await result_div.wait_for()
        result_text = await result_div.text_content()
        assert "1024" in result_text
        
        await browser.close()


@pytest.mark.asyncio
async def test_divide_by_zero_error():
    """Test error handling for division by zero"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/", wait_until="domcontentloaded")
        
        # Fill in the form
        await page.locator("#num1").fill("10")
        await page.locator("#num2").fill("0")
        await page.locator("#operation").select_option("divide")
        
        # Click calculate
        await page.locator("button").click()
        
        # Wait for error and verify
        error_div = page.locator("#error")
        await error_div.wait_for()
        error_text = await error_div.text_content()
        assert "Cannot divide by zero" in error_text or "Error" in error_text
        
        await browser.close()


@pytest.mark.asyncio
async def test_floating_point_calculation():
    """Test floating point number calculations"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/", wait_until="domcontentloaded")
        
        # Fill in the form with floats
        await page.locator("#num1").fill("3.5")
        await page.locator("#num2").fill("2.5")
        await page.locator("#operation").select_option("add")
        
        # Click calculate
        await page.locator("button").click()
        
        # Wait for result and verify
        result_div = page.locator("#resultValue")
        await result_div.wait_for()
        result_text = await result_div.text_content()
        assert "6" in result_text
        
        await browser.close()


@pytest.mark.asyncio
async def test_negative_numbers():
    """Test calculations with negative numbers"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/", wait_until="domcontentloaded")
        
        # Fill in the form with negative numbers
        await page.locator("#num1").fill("-5")
        await page.locator("#num2").fill("3")
        await page.locator("#operation").select_option("add")
        
        # Click calculate
        await page.locator("button").click()
        
        # Wait for result and verify
        result_div = page.locator("#resultValue")
        await result_div.wait_for()
        result_text = await result_div.text_content()
        assert "-2" in result_text
        
        await browser.close()


@pytest.mark.asyncio
async def test_enter_key_triggers_calculation():
    """Test that Enter key triggers calculation"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/", wait_until="domcontentloaded")
        
        # Fill in the form
        await page.locator("#num1").fill("12")
        await page.locator("#num2").fill("4")
        
        # Press Enter
        await page.locator("#num2").press("Enter")
        
        # Wait for result and verify
        result_div = page.locator("#resultValue")
        await result_div.wait_for()
        result_text = await result_div.text_content()
        assert "16" in result_text  # 12 + 4 (add is default)
        
        await browser.close()
