#!/usr/bin/env python3
"""
AXIS Browser Automation Tool
Full Chrome automation with Selenium - bypasses bot detection
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

class AXISBrowser:
    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-gpu')
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)
        print(f"Browser started: {self.driver.current_url}")
    
    def go(self, url):
        self.driver.get(url)
        time.sleep(2)
        return self
    
    def click(self, selector, by=By.XPATH):
        elem = self.wait.until(EC.element_to_be_clickable((by, selector)))
        elem.click()
        time.sleep(1)
        return self
    
    def type(self, selector, text, by=By.XPATH):
        elem = self.driver.find_element(by, selector)
        elem.clear()
        elem.send_keys(text)
        return self
    
    def press(self, key):
        from selenium.webdriver.common.keys import Keys
        self.driver.switch_to.active_element.send_keys(getattr(Keys, key))
        return self
    
    def wait_for(self, seconds):
        time.sleep(seconds)
        return self
    
    def get_text(self, selector, by=By.XPATH):
        try:
            return self.driver.find_element(by, selector).text
        except:
            return None
    
    def get_all_text(self):
        return self.driver.find_element(By.TAG_NAME, 'body').text
    
    def screenshot(self, name="screenshot"):
        self.driver.save_screenshot(f"{name}.png")
        return self
    
    def execute(self, js):
        self.driver.execute_script(js)
        return self
    
    def close(self):
        self.driver.quit()

# Quick functions
def quick_scrape(url):
    """Quick scrape with full browser"""
    browser = AXISBrowser()
    browser.go(url)
    text = browser.get_all_text()
    browser.close()
    return text

def login_and_do(url, actions):
    """Login and perform actions"""
    browser = AXISBrowser()
    browser.go(url)
    
    for action in actions:
        if action['type'] == 'click':
            browser.click(action['selector'])
        elif action['type'] == 'type':
            browser.type(action['selector'], action['text'])
        elif action['type'] == 'wait':
            browser.wait_for(action['seconds'])
    
    result = browser.get_all_text()
    browser.close()
    return result

if __name__ == '__main__':
    # Test
    b = AXISBrowser()
    b.go('https://higgsfield.ai')
    print(f"Title: {b.driver.title}")
    b.screenshot('test')
    print(f"Saved screenshot to test.png")
    b.close()
