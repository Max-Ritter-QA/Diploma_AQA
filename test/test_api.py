from page.page_api import AviaApi
import allure

def test_tickets_back_forth(api_client: AviaApi):
    result = api_client.ticket_back_and_forth()
    with allure.step("Проверить, что что код запроса 200"):
        assert result == 200


def test_tickets_back(api_client: AviaApi):
    result = api_client.ticket_back()
    with allure.step("Проверить, что что код запроса 200"):
        assert result == 200

def test_adult_child(api_client: AviaApi):
    result = api_client.ticket_adult_child()
    with allure.step("Проверить, что что код запроса 200"):
        assert result == 200


def test_passenger_non(api_client: AviaApi):
    result = api_client.ticket_passenger_non()
    with allure.step("Проверить, что что код запроса 400"):
        assert result == 400

def test_not_destination(api_client: AviaApi):
    result = api_client.ticket_not_destination()
    with allure.step("Проверить, что что код запроса 400"):
        assert result == 400