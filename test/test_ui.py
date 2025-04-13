import allure
import pytest
from page.page_ui import Aviasales

departure = "Москва"
arrival = "Новосибирск"

def test_sortie(browser):
    page = Aviasales(browser)
    page.go()
    result = page.origin(departure)

    with allure.step("Проверить, что указаны данные вылета"):
        with allure.step("Поле откуда должно быть " + departure):
            assert result == departure

def test_arrival_by_air(browser):
    page = Aviasales(browser)
    page.go()
    result = page.destination(arrival)

    with allure.step("Проверить, что указаны данные прилета"):
        with allure.step("Поле куда должно быть " + arrival):
             assert result == arrival

def test_celebrate_there(browser):
    page = Aviasales(browser)
    page.go()
    result = page.celebrate_there()

    with allure.step("Проверить, что указана дата вылета"):
        with allure.step("Дата вылета должна быть 29 апреля, вт"):
             assert result == "29 апреля, вт"


def test_celebrate_back(browser):
    page = Aviasales(browser)
    page.go()
    result = page.celebrate_back()

    with allure.step("Проверить, что указана дата прилета"):
        with allure.step("Дата прилета должна быть 30 апреля, ср"):
            assert result == "30 апреля, ср"



def test_servise(browser):
    page = Aviasales(browser)
    page.go()
    result = page.service_class()

    with allure.step("Проверить, что класс обслуживания - Бизнес"):
        assert result == "Бизнес"
