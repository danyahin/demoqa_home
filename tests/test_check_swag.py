from pages.swag_labs import SwagLabs
from selenium.common.exceptions import NoSuchElementException


def test_check_swag_1(browser):
    sauce_base = SwagLabs(browser)
    sauce_base.visit()
    assert sauce_base.exist_icon()


def test_check_swag_2(browser):
    sauce_base = SwagLabs(browser)
    sauce_base.visit()
    try:
        sauce_base.find_element('#user-name')
    except NoSuchElementException:
        return False
    return True


def test_check_swag_3(browser):
    sauce_base = SwagLabs(browser)
    sauce_base.visit()
    try:
        sauce_base.find_element('#password')
    except NoSuchElementException:
        return False
    return True
