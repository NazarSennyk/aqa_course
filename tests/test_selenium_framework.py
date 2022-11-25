from qa_automation_hw.utilities.waits import wai_util


def test_login_user_notvalid_cell_number(open_login_page):
    """
    :param open_login_page: Smoke test
    :return:
    """
    login_page = open_login_page
    login_page.open_login_window()
    dashboard_page = login_page.login('380507285915', 'Qwerty@qwerty')
    assert dashboard_page.is_logout_visible() is False, 'You are logged in with not valid credentials'


def test_login_user_notvalid_password(open_login_page):
    """
    :param open_login_page: Smoke test
    :return:
    """
    login_page = open_login_page
    login_page.open_login_window()
    dashboard_page = login_page.login('380507275915', '12345678990')
    assert dashboard_page.is_logout_visible() is False, 'You are logged in with not valid credentials'


def test_login_user_with_empty_password_field(open_login_page):
    """
       :param open_login_page: Smoke test
       :return:
       """
    login_page = open_login_page
    login_page.open_login_window()
    dashboard_page = login_page.login('380507275915', '        ')
    assert dashboard_page.is_logout_visible() is False, 'You are logged in with not valid credentials'


def test_login_user_with_empty_cellphone_field(open_login_page):
    """
       :param open_login_page: Smoke test
       :return:
       """
    login_page = open_login_page
    login_page.open_login_window()
    dashboard_page = login_page.login('            ', 'Qwerty@qwerty')
    assert dashboard_page.is_logout_visible() is False, 'You are logged in with not valid credentials'


def test_login_user(log_in_user):
    """
       :param open_login_page: Smoke test
       :return:
       """
    dashboard = log_in_user
    assert dashboard.is_logout_visible() is True, 'User is not logt-in'


def test_logout_user(open_login_page, log_in_user):
    """
       :param open_login_page: Smoke test
       :return:
       """
    dash_board_page = log_in_user
    open_login_page.logout()
    assert dash_board_page.registration_button_is_visible() is True, 'User is still logged in'


def test_dashboard_submenu_is_visible(open_login_page, log_in_user):
    """
       :param open_login_page: Regression test
       :return:
       """
    dash_board_page = log_in_user
    assert dash_board_page.dashboard_menu_item_is_visible() is True, 'No second menu item on Maine_Page'


def test_remove_order(open_login_page, log_in_user):
    """
       :param open_login_page: Smoke test
       :return:
       """
    dash_board_page = open_login_page
    dash_board_page.click_on_rod_submenu_dashboard()
    dash_board_page.click_on_fishing_rod_menu()
    dash_board_page.click_on_form_order_button()
    dash_board_page.click_on_continue_button()
    dash_board_page.click_on_shopping_cart_button()
    dash_board_page.remove_item_from_bucket()
    assert log_in_user.empty_order_bucket_is_visible() is True, 'Your bucket is not empty'


def test_click_slide_menu(open_login_page, log_in_user):
    """
       :param open_login_page: Smoke test
       :return:
       """
    dash_board_page = open_login_page
    wai_util(lambda: log_in_user.next_button_is_visible() is True, 'No next button on screen')
    dash_board_page.click_next_button()
    dash_board_page.click_next_button()
    dash_board_page.click_next_button()
    dash_board_page.click_next_button()
    dash_board_page.click_next_button()
    assert log_in_user.home_page_is_visible() is False, 'You are not on home page'


def test_add_new_order(open_login_page, log_in_user):
    """
       :param open_login_page: Smoke test
       :return:
       """
    dash_board_page = open_login_page
    wai_util(lambda: log_in_user.empty_order_bucket_is_visible() is True, '123123213')
    dash_board_page.click_on_rod_submenu_dashboard()
    dash_board_page.click_on_fishing_rod_menu()
    dash_board_page.click_on_form_order_button()
    dash_board_page.click_on_continue_button()
    assert log_in_user.not_empty_order_bucket() is True, 'Your order bucket is empty'


def test_presence_sear_filters_equipment(open_login_page, log_in_user):
    """
       :param open_login_page: Regression test
       :return:
       """
    dash_board_page = open_login_page
    dash_board_page.click_on_equipment_menu()
    dash_board_page.click_on_costumes_submenu()
    assert log_in_user.search_filter_in_equipment_is_visible() is True, 'No search menu present'


def test_search_tent_in_input(open_login_page, log_in_user):
    """
       :param open_login_page: Smoke test
       :return:
       """
    dash_board_page = open_login_page
    dash_board_page.search_tent('палатка')
    dash_board_page.click_on_all_search_results()
    assert log_in_user.tent_all_items_is_visible() is True, 'No search result'


def test_remove_order_from_bucket_through_input(open_login_page, log_in_user):
    """
       :param open_login_page: Regression test
       :return:
       """
    dash_board_page = open_login_page
    dash_board_page.search_tent('палатка')
    dash_board_page.click_on_all_search_results()
    dash_board_page.click_add_order_tent_through_input()
    dash_board_page.click_on_continue_button()
    dash_board_page.click_on_shopping_cart_button()
    dash_board_page.remove_item_from_bucket()
    assert log_in_user.empty_order_bucket_is_visible() is True, 'Your order bucket is not empty'


def test_add_new_order_through_input(open_login_page, log_in_user):
    """
       :param open_login_page: Regression test
       :return:
       """
    dash_board_page = open_login_page
    dash_board_page.search_tent('палатка')
    dash_board_page.click_on_all_search_results()
    dash_board_page.click_add_order_tent_through_input()
    dash_board_page.click_on_continue_button()
    assert log_in_user.not_empty_order_bucket() is True, 'Your order bucket is empty'


def test_sing_in_news_input_visible(open_login_page, log_in_user):
    """
       :param open_login_page: Regression test
       :return:
       """
    dash_board_page = open_login_page
    assert log_in_user.sing_up_news_is_visible() is True, 'No Sing-up input'


def test_presence_of_social_network_icon_facebook(open_login_page, log_in_user):
    """
           :param open_login_page: Regression test
           :return:
           """
    dash_board_page = open_login_page
    assert log_in_user.social_network_icon_is_visible() is True, 'facebook icon ist not presente in footer'


def test_presence_of_social_network_icon_youtube(open_login_page, log_in_user):
    """
           :param open_login_page: Regression test
           :return:
           """
    dash_board_page = open_login_page
    assert log_in_user.social_network_icon_is_visible_youtube() is True, 'youtube icon is not present in footer'


def test_presence_of_social_network_icon_instagram(open_login_page, log_in_user):
    """
           :param open_login_page: Regression test
           :return:
           """
    dash_board_page = open_login_page
    assert log_in_user.social_network_icon_is_visible_instagram() is True, 'instagram icon is not present in footer'


def test_presence_of_social_network_icon_issu(open_login_page, log_in_user):
    """
           :param open_login_page: Regression test
           :return:
           """
    dash_board_page = open_login_page
    assert log_in_user.social_network_icon_is_visible_issu() is True, 'issu icon is not present in footer'


def test_winter_submenu_is_present(open_login_page, log_in_user):
    """
           :param open_login_page: Regression test
           :return:
           """
    dash_board_page = open_login_page
    assert log_in_user.winter_submenu_is_present() is True, 'The winter submenu is not present'


def test_baits_in_winter_submenu_present(open_login_page, log_in_user):
    """
           :param open_login_page: Regression test
           :return:
           """
    dash_board_page = open_login_page
    dash_board_page.click_on_winter_submenu()
    dash_board_page.click_on_winter_baits_submenu()
    assert log_in_user.bait_in_baits_submenu_is_visible() is True, 'No items in baits submenu'


def test_brandes_is_visible(open_login_page, log_in_user):
    """
           :param open_login_page: Regression test
           :return:
           """
    dash_board_page = open_login_page
    dash_board_page.click_on_brandes_button()
    assert log_in_user.cruchevichi_icon_is_visible() is True, 'No brand icon on brand dashboard'


def test_presence_of_carp_submenu(open_login_page, log_in_user):
    """
           :param open_login_page: Regression test
           :return:
           """
    dash_board_page = open_login_page
    assert log_in_user.carp_submenu_on_dashboard_is_visible() is True, 'Carp submenu ist not present on dashboard'


def test_presence_of_submenu_in_footer(open_login_page, log_in_user):
    """
           :param open_login_page: Regression test
           :return:
           """
    dash_board_page = open_login_page
    assert log_in_user.submenu_in_footer_is_visible() is True, 'Submenu in footer is not present'


def test_shopping_cart_is_visible(open_login_page, log_in_user):
    """
           :param open_login_page: Regression test
           :return:
           """
    dash_board_page = open_login_page
    assert log_in_user.shoping_cart_button_is_visible() is True, 'Shopping cart missing'