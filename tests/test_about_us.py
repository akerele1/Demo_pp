import pytest
from pages.about_us import aboutUs
from playwright.sync_api import Page

def test_about_us(page: Page):
    about = aboutUs(page)
    about.open_url()
    about.open_about_us_page()
    print(about.get_aboutus_title())
    

