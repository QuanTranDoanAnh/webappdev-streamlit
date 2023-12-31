from main import calculate_sum
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def test_user_interface():
    driver_path = r"D:\chrome-win64\chrome.exe"
    service = Service(executable_path=driver_path)
    options = Options()
    options.add_argument("--headless=new") # To not open a real chrome window
    
    with webdriver.Chrome(options=options, service=service) as driver:
        url = "http://localhost:8501"
        driver.get(url)
        time.sleep(5)
        html = driver.page_source
        assert "Add numbers" in html
        assert "First number" in html
        assert "Second number" in html
        
def test_logic():
    assert calculate_sum(1, 1) == 2
    assert calculate_sum(1, -1) == 0
    assert calculate_sum(1, 9) == 10

if __name__ == "__main__":
    test_logic()
    test_user_interface()