from page.page_api import AviaApi

def test_get_tickets():
    api=AviaApi("https://tickets-api.aviasales.ru/search/v2/start")
    result = api.get_tickets()
    assert result == 200