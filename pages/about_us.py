import pytest
from playwright.sync_api import Page, expect

class aboutUs():

    def __init__(self, page: Page):
        self = self.page
        self.url = "https://theprosperingplace.co.uk/"

    def load(self):
        self.page.goto(self.url):

    def open_about_us_page(self):
        about_us = self.page.locator("menu-item-225").get_by_role("link", name="About")

    def get_aboutus_title(self):
        about_title = self.page.title()
        return(about_title)