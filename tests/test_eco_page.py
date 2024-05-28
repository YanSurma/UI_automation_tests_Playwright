import allure
import pytest

from conftest import eco, page


@pytest.mark.smoke
@allure.feature('Smoke')
def test_add_item_sort_by_position(eco):
    eco.open_page(eco.page_url)
    eco.sort_by_option('Position')
    eco.hover_on_item_banner()
    item_price = eco.get_item_price()
    eco.click_add_to_card_button()
    eco.check_item_price(item_price)


@pytest.mark.smoke
@allure.feature('Smoke')
def test_add_item_sort_by_price(eco):
    eco.open_page(eco.page_url)
    eco.sort_by_option('price')
    eco.hover_on_item_banner()
    item_price = eco.get_item_price()
    eco.click_add_to_card_button()
    eco.check_item_price(item_price)


@pytest.mark.smoke
@allure.feature('Smoke')
def test_add_item_sort_by_product_name(eco):
    eco.open_page(eco.page_url)
    eco.sort_by_option('Product Name')
    eco.hover_on_item_banner()
    item_price = eco.get_item_price()
    eco.click_add_to_card_button()
    eco.check_item_price(item_price)
