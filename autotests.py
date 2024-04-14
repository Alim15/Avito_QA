# import pytest

# def setup_module(module):
#     #init_something()
#     pass

# def teardown_module(module):
#     #teardown_something()
#     pass

# def test_upper():
#     assert 'foo'.upper() == 'FOO'
    
# def test_isupper():
#     assert 'FOO'.isupper()
    
# def test_failed_upper():
#     assert 'foo'.upper() == 'FOo'

import os
import pytest
from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

def test_waterscreenshot(browser):
    page = browser.new_page()
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    water_counter = page.locator('#water-counter')
    water_counter.screenshot(path=os.path.join('output', 'water_counter.png'))

def test_co2screenshot(browser):
    page = browser.new_page()
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    co2_counter = page.locator('#co2-counter')
    co2_counter.screenshot(path=os.path.join('output', 'co2_counter.png'))

def test_energyscreenshot(browser):
    page = browser.new_page()
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    energy_counter = page.locator('#energy-counter')
    energy_counter.screenshot(path=os.path.join('output', 'energy_counter.png'))
