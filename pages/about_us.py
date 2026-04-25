import pytest
from playwright.sync_api import Page, expect

class aboutUs():

    def __init__(self, page: Page):
        self = self.page
        self.url = "https://theprosperingplace.co.uk/"

    def open_url (self):
        self.page.goto(self.url)

    def get_aboutus_title(self):
        print()

    def open_about_us_page(self):
        about
