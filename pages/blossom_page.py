import pytest
from playwright.sync_api import Page, expect

class blossomPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://theprosperingplace.co.uk/product/blossom/'

    def load(self):
        self.page.goto(self.url)

    def get_title(self):
        return self.page.title()

    def open_services(self):
        services = self.page.locator("#menu-item-1399").get_by_role("link", name="Services")
        expect(services).to_be_visible()
        services.click()
