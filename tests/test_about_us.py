import pytest
from pages.about_us import aboutUs
from playwright.sync_api import Page

def test_about_us(page: Page):
    about =aboutUs(page)
    #open url
    about.open_url