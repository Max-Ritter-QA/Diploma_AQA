import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Aviasales:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.aviasales.ru/"
        self.__driver = driver

    @allure.step("Перейти на главную страницу Aviasales")
    def go(self):
        self.__driver.get(self.__url)
        my_cookie = {
             'name': 'cookies_policy',
             'value': '%7B%22accepted%22%3Atrue%2C%22technical%22%3Atrue%2C%22marketing%22%3Atrue%7D',
             'domain': '.aviasales.ru'
        }
        self.__driver.add_cookie(my_cookie)

    @allure.step("Заполнение поля откуда - {departure}")
    def origin(self, departure: str) ->str:
        (WebDriverWait(self.__driver, 5).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, "#avia_form_origin-input"))))

        (self.__driver.find_element(By.CSS_SELECTOR, "#avia_form_origin-input").clear())
        (WebDriverWait(self.__driver, 5).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, "#avia_form_origin-input"))))

        (self.__driver.find_element(By.CSS_SELECTOR, "#avia_form_origin-input").send_keys(departure))
        result = self.__driver.find_element(By.CSS_SELECTOR, "#avia_form_origin-input").get_attribute("value")
        return result

    @allure.step("Заполнение поля куда - {arrival}")
    def destination(self, arrival: str) ->str:
        (WebDriverWait(self.__driver, 5).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, "#avia_form_destination-input"))))

        (self.__driver.find_element(By.CSS_SELECTOR, "#avia_form_destination-input").clear())

        (self.__driver.find_element(By.CSS_SELECTOR, "#avia_form_destination-input").send_keys(arrival))

        result = self.__driver.find_element(By.CSS_SELECTOR, "#avia_form_destination-input").get_attribute("value")
        return result

    @allure.step("Выбор даты вылета")
    def celebrate_there(self)->str:
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, '[data-test-id="start-date-field"]'))))

        (self.__driver.find_element(By.CSS_SELECTOR, '[data-test-id="start-date-field"]').click())

        (WebDriverWait(self.__driver, 5).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, '[data-test-id ="date-29.04.2025"]')))).click()

        result = (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, '[data-test-id="start-date-value"]')))).text

        return result

    @allure.step("Выбор даты прилета")
    def celebrate_back(self)->str:
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, '[data-test-id="end-date-field"]'))))

        (self.__driver.find_element(By.CSS_SELECTOR, '[data-test-id="end-date-field"]').click())


        (WebDriverWait(self.__driver, 5).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, '[data-test-id ="date-30.04.2025"]')))).click()

        result = (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, '[data-test-id="end-date-value"]')))).text

        return result

    @allure.step("Выбор класса обслуживания")
    def service_class(self)->str:
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 CSS_SELECTOR, '[data-test-id="passengers-field"]'))))

        (self.__driver.find_element(By.CSS_SELECTOR, '[data-test-id="passengers-field"]').click())

        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class, "s__OThdRwx3Czvo9QCpLx_2") and text()="Бизнес"]'))))

        (self.__driver.find_element(By.XPATH, '//span[contains(@class, "s__OThdRwx3Czvo9QCpLx_2") and text()="Бизнес"]').click())


        result = (WebDriverWait(self.__driver, 10).
                  until(EC.visibility_of_element_located((By.
                                                          CSS_SELECTOR, '[data-test-id="trip-class"]')))).text
        return result
