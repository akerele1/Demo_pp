import pytest
from playwright.sync_api import Page
from pages.blossom_page import blossomPage


def test_blossom_abode(page: Page):
    ba = blossomPage(page)
    ba.load()
    print (ba.get_title())
    ba.open_services()
    page.get_by_role
                    ("link", name="What we offer", exact=True).click()
