from selenium.webdriver.common.by import By
from qa_automation_hw.utilities.web_ui.base_page import BasePage


class DashBoardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __logout_button = (By.XPATH, "//a[text() = 'Вихід']")
    __registration_button = (By.XPATH, '//*[contains(text(), "Реєстрація")]/ancestor::li')
    __rod_submenu_on_dashboard = (By.XPATH, '//i[@class="icon icon-menu_item_2"]')
    __presence_of_order = (By.XPATH, '//a[@name= "goods-link" and @class= "novisited"]')
    __input_location = (By.XPATH, '//input[@class="search-text-default"]')
    __empty_order_bucket = (By.XPATH, '//span[@class="cart-count" and   contains(text(), "0")]')
    __not_empty_order_bucket = (By.XPATH, '//span[@class="cart-count" and   contains(text(), "1")]')
    __search_filters_in_equipment = (By.XPATH, '//div[@class="filter" and @name="menu_sort_view"]')
    __tent_all_items = (By.XPATH, '//*[contains(text(), "палатка") and @class="b-search-results-request"]')
    __input_sing_up_news = (By.XPATH, '//input[@pattern="^(|.*@.*\..*)$"]')
    __icon_social_network_facebook = (By.XPATH, '//i[@class="icon icon-facebook"]')
    __icon_social_network_youtube = (By.XPATH, '//i[@class="icon icon-youtube"]')
    __icon_social_network_instagram = (By.XPATH, '//i[@class="icon icon-instagram"]')
    __icon_social_network_issu = (By.XPATH, '//i[@class="icon icon-issu"]')
    __winter_submenu_on_dashboard = (By.XPATH, '//i[@class="icon icon-menu_item_6"]')
    __bait_in_winter_submenu = (By.XPATH, '//*[contains(text(), "Прикормки") and @href="https://www.flagman.kiev.ua/pricormki/c168802/10650=4045/"]')
    __bait_item_in_baits_submenu = (By.XPATH, '//*[contains(text(), "Прикормка") and @href="https://www.flagman.kiev.ua/rybolovnaya-prikormka/c168803/10650=4045/"]')
    __next_slide_button = (By.XPATH, '//button[@class="slick-next slick-arrow"]')
    __kruchevichi_brand_icon = (By.XPATH, '//img[@src="https://i.flagman.kiev.ua/producers/0/238.png"]')
    __carp_submenu_on_dashboard = (By.XPATH, '//i[@class="icon icon-menu_item_4"]')
    __submenu_in_footer = (By.XPATH, '//div[@class="active-tab-content js-tab-content"]')
    __shopping_cart_button = (By.XPATH, '//i[@class="icon icon-goods_cart"]')

    def is_logout_visible(self):
        return self._is_visible(self.__logout_button)

    def registration_button_is_visible(self):
        return self._is_visible(self.__registration_button)

    def dashboard_menu_item_is_visible(self):
        return self._is_visible(self.__rod_submenu_on_dashboard)

    def order_item_visible(self):
        return self._is_visible(self.__presence_of_order)

    def empty_order_bucket_is_visible(self):
        return self._is_visible(self.__empty_order_bucket)

    def home_page_is_visible(self):
        return self._is_visible(self.__input_location)

    def search_filter_in_equipment_is_visible(self):
        return self._is_visible(self.__search_filters_in_equipment)

    def not_empty_order_bucket(self):
        return self._is_visible(self.__not_empty_order_bucket)

    def tent_all_items_is_visible(self):
        return self._is_visible(self.__tent_all_items)

    def sing_up_news_is_visible(self):
        return self._is_visible(self.__input_sing_up_news)

    def social_network_icon_is_visible(self):
        return self._is_visible(self.__icon_social_network_facebook)

    def social_network_icon_is_visible_youtube(self):
        return self._is_visible(self.__icon_social_network_youtube)

    def social_network_icon_is_visible_instagram(self):
        return self._is_visible(self.__icon_social_network_instagram)

    def social_network_icon_is_visible_issu(self):
        return self._is_visible(self.__icon_social_network_issu)

    def winter_submenu_is_present(self):
        return self._is_visible(self.__winter_submenu_on_dashboard)

    def bait_in_baits_submenu_is_visible(self):
        return self._is_visible(self.__bait_item_in_baits_submenu)

    def next_button_is_visible(self):
        return self._is_visible(self.__next_slide_button)

    def cruchevichi_icon_is_visible(self):
        return self._is_visible(self.__kruchevichi_brand_icon)

    def carp_submenu_on_dashboard_is_visible(self):
        return self._is_visible(self.__carp_submenu_on_dashboard)

    def submenu_in_footer_is_visible(self):
        return self._is_visible(self.__submenu_in_footer)

    def shoping_cart_button_is_visible(self):
        return self._is_visible(self.__shopping_cart_button)