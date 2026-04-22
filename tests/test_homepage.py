import pytest
from playwright.sync_api import Page, expect
from pages.homepage import Homepage


def test_pp_homepage(page: Page):
    home = Homepage(page)
    home.load()
    home.get_title()
    expect(page).to_have_title("The Prospering Place – Semi-independent Living & Children’s Home Provider")


def test_contact_us_visible(page: Page):
    home = Homepage(page)
    home.load()
    contact_us = page.get_by_text("Contact Us")
    expect(contact_us).to_be_visible()
    contact_us.click()
    page.get_by_placeholder("first name here").fill("Victor")
    page.get_by_placeholder("last name here").fill("Akerele")
    page.get_by_placeholder("Add email").fill("akerelev@yahoo.com")
    page.get_by_placeholder("How can we help you").fill(
        "I want to know more about the services offered")
    page.get_by_placeholder("Comments").fill(
        "Looking forward to hearing from you")
    page.get_by_role("button", name="Submit").click()

