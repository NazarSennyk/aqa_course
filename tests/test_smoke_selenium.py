# import pytest
from utilities.waits import wai_util
import allure


@allure.feature('Nazar Sennyk')
@pytest.mark.smoke
def test_login_user_notvalid_cell_number(open_login_page):
    login_page = open_login_page
    login_page.open_login_window()
    dashboard_page = login_page.login('380507285915', 'Qwerty@qwerty')
    assert dashboard_page.is_logout_visible() is False, 'You are logged in with not valid credentials'


@allure.feature('Nazar Sennyk')
@pytest.mark.smoke
def test_login_user_notvalid_password(open_login_page):
    login_page = open_login_page
    login_page.open_login_window()
    dashboard_page = login_page.login('380507275915', '12345678990')
    assert dashboard_page.is_logout_visible() is False, 'You are logged in with not valid credentials'


@allure.feature('Nazar Sennyk')
@pytest.mark.smoke
def test_login_user_with_empty_password_field(open_login_page):
    login_page = open_login_page
    login_page.open_login_window()
    dashboard_page = login_page.login('380507275915', '        ')
    assert dashboard_page.is_logout_visible() is False, 'You are logged in with not valid credentials'


@allure.feature('Nazar Sennyk')
@pytest.mark.smoke
def test_login_user_with_empty_cellphone_field(open_login_page):
    login_page = open_login_page
    login_page.open_login_window()
    dashboard_page = login_page.login('            ', 'Qwerty@qwerty')
    assert dashboard_page.is_logout_visible() is False, 'You are logged in with not valid credentials'


@allure.feature('Nazar Sennyk')
@pytest.mark.smoke
def test_login_user(log_in_user):
    dashboard = log_in_user
    assert dashboard.is_logout_visible() is True, 'User is not logt-in'
    raise Exception


@allure.feature('Nazar Sennyk')
@pytest.mark.smoke
def test_logout_user(open_login_page, log_in_user):
    dash_board_page = log_in_user
    open_login_page.logout()
    assert dash_board_page.registration_button_is_visible() is True, 'User is still logged in'
    raise Exception


@allure.feature('Nazar Sennyk')
@pytest.mark.smoke
def test_remove_order(open_login_page, log_in_user):
    dash_board_page = open_login_page
    dash_board_page.click_on_rod_submenu_dashboard()
    dash_board_page.click_on_fishing_rod_menu()
    dash_board_page.click_on_form_order_button()
    dash_board_page.click_on_continue_button()
    dash_board_page.click_on_shopping_cart_button()
    dash_board_page.remove_item_from_bucket()
    assert log_in_user.empty_order_bucket_is_visible() is True, 'Your bucket is not empty'


@allure.feature('Nazar Sennyk')
@pytest.mark.smoke
def test_add_new_order(open_login_page, log_in_user):
    dash_board_page = open_login_page
    wai_util(lambda: log_in_user.empty_order_bucket_is_visible() is True, '123123213')
    dash_board_page.click_on_rod_submenu_dashboard()
    dash_board_page.click_on_fishing_rod_menu()
    dash_board_page.click_on_form_order_button()
    dash_board_page.click_on_continue_button()
    assert log_in_user.not_empty_order_bucket() is True, 'Your order bucket is empty'


@allure.feature('Nazar Sennyk')
@pytest.mark.smoke
def test_search_tent_in_input(open_login_page, log_in_user):
    dash_board_page = open_login_page
    dash_board_page.search_tent('палатка')
    dash_board_page.click_on_all_search_results()
    assert log_in_user.tent_all_items_is_visible() is True, 'No search result'


