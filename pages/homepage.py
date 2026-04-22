import pytest
from playwright.sync_api import Page, expect

class Homepage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://theprosperingplace.co.uk/'

    def load(self):
        self.page.goto(self.url)

    def get_title(self):
        return self.page.title()
