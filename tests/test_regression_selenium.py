import pytest
from qa_automation_hw.utilities.waits import wai_util
import allure


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_dashboard_submenu_is_visible(open_login_page, log_in_user):
    dash_board_page = log_in_user
    assert dash_board_page.dashboard_menu_item_is_visible() is True, 'No second menu item on Maine_Page'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_presence_sear_filters_equipment(open_login_page, log_in_user):
    dash_board_page = open_login_page
    dash_board_page.click_on_equipment_menu()
    dash_board_page.click_on_costumes_submenu()
    assert log_in_user.search_filter_in_equipment_is_visible() is True, 'No search menu present'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_remove_order_from_bucket_through_input(open_login_page, log_in_user):
    dash_board_page = open_login_page
    dash_board_page.search_tent('палатка')
    dash_board_page.click_on_all_search_results()
    dash_board_page.click_add_order_tent_through_input()
    dash_board_page.click_on_continue_button()
    dash_board_page.click_on_shopping_cart_button()
    dash_board_page.remove_item_from_bucket()
    assert log_in_user.empty_order_bucket_is_visible() is True, 'Your order bucket is not empty'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_add_new_order_through_input(open_login_page, log_in_user):
    dash_board_page = open_login_page
    dash_board_page.search_tent('палатка')
    dash_board_page.click_on_all_search_results()
    dash_board_page.click_add_order_tent_through_input()
    dash_board_page.click_on_continue_button()
    assert log_in_user.not_empty_order_bucket() is True, 'Your order bucket is empty'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_sing_in_news_input_visible(open_login_page, log_in_user):
    dash_board_page = open_login_page
    assert log_in_user.sing_up_news_is_visible() is True, 'No Sing-up input'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_presence_of_social_network_icon_facebook(open_login_page, log_in_user):
    dash_board_page = open_login_page
    assert log_in_user.social_network_icon_is_visible() is True, 'facebook icon ist not presente in footer'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_presence_of_social_network_icon_youtube(open_login_page, log_in_user):
    dash_board_page = open_login_page
    assert log_in_user.social_network_icon_is_visible_youtube() is True, 'youtube icon is not present in footer'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_presence_of_social_network_icon_instagram(open_login_page, log_in_user):
    dash_board_page = open_login_page
    assert log_in_user.social_network_icon_is_visible_instagram() is True, 'instagram icon is not present in footer'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_presence_of_social_network_icon_issu(open_login_page, log_in_user):
    dash_board_page = open_login_page
    assert log_in_user.social_network_icon_is_visible_issu() is True, 'issu icon is not present in footer'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_winter_submenu_is_present(open_login_page, log_in_user):
    dash_board_page = open_login_page
    assert log_in_user.winter_submenu_is_present() is True, 'The winter submenu is not present'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_baits_in_winter_submenu_present(open_login_page, log_in_user):
    dash_board_page = open_login_page
    dash_board_page.click_on_winter_submenu()
    dash_board_page.click_on_winter_baits_submenu()
    assert log_in_user.bait_in_baits_submenu_is_visible() is True, 'No items in baits submenu'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_brandes_is_visible(open_login_page, log_in_user):
    dash_board_page = open_login_page
    dash_board_page.click_on_brandes_button()
    assert log_in_user.cruchevichi_icon_is_visible() is True, 'No brand icon on brand dashboard'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_presence_of_carp_submenu(open_login_page, log_in_user):
    dash_board_page = open_login_page
    assert log_in_user.carp_submenu_on_dashboard_is_visible() is True, 'Carp submenu ist not present on dashboard'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_presence_of_submenu_in_footer(open_login_page, log_in_user):
    dash_board_page = open_login_page
    assert log_in_user.submenu_in_footer_is_visible() is True, 'Submenu in footer is not present'


@allure.feature('Nazar Sennyk')
@pytest.mark.regression
def test_shopping_cart_is_visible(open_login_page, log_in_user):
    dash_board_page = open_login_page
    assert log_in_user.shoping_cart_button_is_visible() is True, 'Shopping cart missing'