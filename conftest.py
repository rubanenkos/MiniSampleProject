"""
This is a fixtures module
"""
from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def browser():
    """
    Setup for Chrome driver
    """
    # To run locally with the real browser
    # driver = webdriver.Chrome(executable_path="./chromedriver")

    # To run using selenoid
    capabilities = {
        "browserName": "firefox",
        "version": "79.0",
        "enableVNC": True,
        "enableVideo": False,
        "platform": "LINUX"
    }

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=capabilities
    )

    yield driver
    driver.quit()
