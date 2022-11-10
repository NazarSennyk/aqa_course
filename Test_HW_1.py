import time
import pytest
import selenium
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
"""
# Тест ранився на Хромі

wwww.flagman.kiev.ua

XPATH:

1. //*[@id='search-text']
2. //i[@class='icon icon-header_compare']
3. //i[@title='Особистий кабінет']
4. //input[@id='search-text']
5. //input[@pattern='^(|.*@.*\..*)$']
6. //a[@href="#enter"]                                             # log in button
7. //input[@class='custom-field-error input-field phone-number']   # field with cell number enter
8. //input[@class='custom-field-error input-field password']       # field with passwor on log in
9. //button[@name="signin-continue"]                               # button enter profile
10. //a[@href='https://my.flagman.kiev.ua/signout/']               # log out button
11. //i[@class='icon icon-menu_item_7']
12. //button[@name='subscribe']
13. //span[@class='main-menu_image']/ancestor::ul[@class='main-menu']
14. //button[@name='subscribe']/parent::*
15. //button[@name='subscribe']/preceding-sibling::*
16. //button[@name='subscribe' and @type='submit']
17. //img[@src='https://i.flagman.kiev.ua/design/up_btn.png']
18. //div[@class='lp-article_image' and @style='background-image: url(https://i.flagman.kiev.ua/articles/0/363.jpg)']
19. //span[@class='main-menu_image']/ancestor::ul
20. //img[@src='https://i.flagman.kiev.ua/design/flagman_logo.png']/ancestor::div[@class='main-logo icon']
21. //i[@class='icon icon-goods_cart']/ancestor::a[@class='icon header-cart full-cart']
22. //div[@class='subscribe-teleg_post']
23. //div[@class='subscribe-viber_post']
24. //i[@class='icon icon-flagmangoogleplay']
25. //div[@class='subscribe-viber_post']/parent::*
26. //article[@class='lp-article stub']/ancestor::div[@class='row']/ancestor::section
27. //li[@id='slick-slide02']
28. //a[@href='https://www.flagman.kiev.ua/promotions/']/ancestor::div[@class='col-md-7']
29. //i[@class='icon icon-facebook']
30. //*[contains(text(), 'Контакти')]/ancestor::div[@class='header-top']

CSS:

1. div.subscribe-viber_post
2. div.subscribe-teleg_post
3. i.icon-header_phone
4. i.icon.icon-menu_item_8
5. #meta_referrer
6. a > i.icon.icon-header_man
7. input[id='search-text']
8. i[class^='icon icon-menu_item_1']
9. i[class$='item_1']
10. div[class*='slide-next']
11. ul.slick-dots
12. div[style='background-image: url(https://i.flagman.kiev.ua/articles/0/365.jpg)']
13. div.black-fon
14. script:first-child
15. div[style='background-color: rgb(0, 0, 0); opacity: 0.7; width: 100%; position: fixed; z-index: 50; top: 0px; left: 0px; visibility: hidden;']

"""


def test_login_chrome():
    """
    Function for auto-log in into web resource
    """
    driver_chrome = Chrome('chromedriver.exe')
    driver_chrome.maximize_window()
    driver_chrome.get('https://www.flagman.kiev.ua/')
    login = '380507275915'
    password = 'Qwerty@qwerty'
    login_button_locator = '//a[@href="#enter"]'
    login_button_element = driver_chrome.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    cell_numb_locator = "//input[@class='custom-field-error input-field phone-number']"
    cell_numb_element = driver_chrome.find_element(By.XPATH, cell_numb_locator)
    cell_numb_element.clear()
    cell_numb_element.send_keys(login)
    time.sleep(3)
    password_locator = "//input[@class='custom-field-error input-field password']"
    password_element = driver_chrome.find_element(By.XPATH, password_locator)
    password_element.clear()
    password_element.send_keys(password)
    time.sleep(3)
    enter_button_locator = '//button[@name="signin-continue"]'
    enter_button_element = driver_chrome.find_element(By.XPATH, enter_button_locator)
    enter_button_element.click()
    time.sleep(5)
    logout_button_locator = "//a[text() = 'Вихід']"
    logout_button_element = driver_chrome.find_element(By.XPATH, logout_button_locator)
    verify_logout = logout_button_element.is_displayed()
    assert verify_logout is True




