from selenium.webdriver.support.wait import WebDriverWait
from qa_automation_course.page_objects.dashboardpage import DashBoardPage
from qa_automation_course.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By
from qa_automation_course.utilities.web_ui.decorator_mark_steps import auto_step


@auto_step
class LoginPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(driver)
        self._wait = WebDriverWait(self.__driver, 10)

    __cell_numb_locator = (By.XPATH, "//input[@class='custom-field-error input-field phone-number']")
    __password_locator = (By.XPATH, "//input[@class='custom-field-error input-field password']")
    __enter_button_locator = (By.XPATH, '//button[@name="signin-continue"]')
    __logout_button = (By.XPATH, "//a[text() = 'Вихід']")
    __rod_submenu_on_dashboard = (By.XPATH, '//i[@class="icon icon-menu_item_2"]')
    __fishing_rod_menu = (By.XPATH, '//a[@class= "podmenu-title" and @href= "https://www.flagman.kiev.ua/spinningovie-udilischa/c201224/"]')
    __rod_in_fishing_rod_menu = (By.XPATH, '//img[@alt="Cпінінговe вудлище Azura X-Game X76ULS Soft Solid TZ 2.29м 0.6-5г"]')
    __form_order_button = (By.XPATH, '//i[@onmousedown="try { rrApi.addToBasket(255998) } catch(e) {}"]')
    __shopping_cart_button = (By.XPATH, '//i[@class="icon icon-goods_cart"]')
    __presence_of_order = (By.XPATH, '//a[@name= "goods-link" and @class= "novisited"]')
    __continue_shopping_button = (By.XPATH, '//*[contains(text(), "Продовжити покупки")]')
    __remove_item_from_order_bucket = (By.XPATH, '//i[@class="icon icon-delete_row delete-column"]')
    __order_pop_up = (By.XPATH, '//h1')
    __next_slide_button = (By.XPATH, '//button[@class="slick-next slick-arrow"]')
    __equipment_menu = (By.XPATH, '//i[@class="icon icon-menu_item_9"]')
    __costumes_submenu_equipment = (By.XPATH, '//*[contains(text(), "Костюми")]')
    __input_location = (By.XPATH, '//input[@id="search-text"]')
    __all_tent_search_results = (By.XPATH, '//span[@class="show-results-title"]')
    __add_new_order_input = (By.XPATH, '//i[@onmousedown="try { rrApi.addToBasket(169969) } catch(e) {}"]')
    __bait_in_winter_submenu = (By.XPATH, '//*[contains(text(), "Прикормки") and @href="https://www.flagman.kiev.ua/pricormki/c168802/10650=4045/"]')
    __winter_submenu_on_dashboard = (By.XPATH, '//i[@class="icon icon-menu_item_6"]')
    __brands_button = (By.XPATH, '//a[@href="https://www.flagman.kiev.ua/brands/"]')
    __aid_button = (By.XPATH, '//a[@class="active-link"]')
    __tips_menu = (By.XPATH, '//*[contains(text(), "Як я можу побачити свій розмір знижки?")]')

    def set_cell_number(self, cell_number: str):
        self._send_keys(self.__cell_numb_locator, cell_number)
        return self

    def set_password(self, password: str):
        self._send_keys(self.__password_locator, password)
        return self

    def click_login(self):
        self._click(self.__enter_button_locator)

    def login(self, cell_number: str, password: str):
        self.set_cell_number(cell_number).set_password(password).click_login()
        return DashBoardPage(self.__driver)

    def logout(self):
        self._click(self.__logout_button)

    def click_on_rod_submenu_dashboard(self):
        self._click(self.__rod_submenu_on_dashboard)

    def click_on_fishing_rod_menu(self):
        self._click(self.__fishing_rod_menu)

    def click_on_rod_in_rod_menu(self):
        self._click(self.__rod_in_fishing_rod_menu)

    def click_on_form_order_button(self):
        self._click(self.__form_order_button)

    def click_on_shopping_cart_button(self):
        self._click(self.__shopping_cart_button)

    def click_on_continue_button(self):
        self._click(self.__continue_shopping_button)

    def click_next_button(self):
        self._click(self.__next_slide_button)

    def remove_item_from_bucket(self):
        self._click(self.__remove_item_from_order_bucket)

    def click_on_equipment_menu(self):
        self._click(self.__equipment_menu)

    def click_on_costumes_submenu(self):
        self._click(self.__costumes_submenu_equipment)

    def search_tent(self, value):
        self._send_keys(self.__input_location, value)
        return self

    def click_on_all_search_results(self):
        self._click(self.__all_tent_search_results)

    def click_add_order_tent_through_input(self):
        self._click(self.__add_new_order_input)

    def click_on_winter_submenu(self):
        self._click(self.__winter_submenu_on_dashboard)

    def click_on_winter_baits_submenu(self):
        self._click(self.__bait_in_winter_submenu)

    def click_on_brandes_button(self):
        self._click(self.__brands_button)

    def click_on_aid_button(self):
        self._click(self.__aid_button)

