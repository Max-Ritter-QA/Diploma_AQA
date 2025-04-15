import requests
import allure

cookie = {
            'name': 'nuid',
            'value':'81cb6107-fc92-4bd9-be60-3e7c1c47454b',
            'domain': 'aviasales.ru'
        }

class AviaApi:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    @allure.step("API запрос туда-обратно")
    def ticket_back_and_forth(self, false=None, true=None) -> int:
        params = {"search_params":{"directions":[{"origin":"MOW","destination":"OVB","date":"2025-04-29","is_origin_airport":false,"is_destination_airport":false},{"origin":"OVB","destination":"MOW","date":"2025-04-30","is_origin_airport":false,"is_destination_airport":false}],
                                   "passengers":{"adults":1,"children":0,"infants":0},"trip_class":"Y"},"client_features":{"direct_flights":true,"brand_ticket":false,"top_filters":true,"badges":false,"tour_tickets":true,"assisted":true},
                  "market_code":"ru","marker":"15468.ydall22247596093780","citizenship":"RU","currency_code":"rub","languages":{"ru":1}}

        headers = {
            'content-type': 'application/json',
            'x-client-type': 'web',
            'x-origin-cookie': self.token
        }

        path = self.base_url
        resp = requests.post(path, headers=headers,json=params,cookies=cookie)
        return resp.status_code

    @allure.step("API запрос в одну сторону")
    def ticket_back(self, false=None, true=None,) -> int:
        params = {"search_params":{"directions":[{"origin":"MOW","destination":"OVB","date":"2025-04-29","is_origin_airport":false,"is_destination_airport":false}],
                                   "passengers":{"adults":1,"children":0,"infants":0},"trip_class":"Y"},"client_features":{"direct_flights":true,"brand_ticket":false,"top_filters":true,"badges":false,"tour_tickets":true,"assisted":true},
                  "market_code":"ru","marker":"15468.ydall22247596093780","citizenship":"RU","currency_code":"rub","languages":{"ru":1}}

        headers = {
            'content-type': 'application/json',
            'x-client-type': 'web',
            'x-origin-cookie': self.token
        }
        path = self.base_url
        resp = requests.post(path, headers=headers,json=params,cookies=cookie)
        return resp.status_code

    @allure.step("API запрос 1 взрослый, 1 ребенок")
    def ticket_adult_child(self, false=None, true=None,) -> int:
        params = {"search_params":{"directions":[{"origin":"MOW","destination":"OVB","date":"2025-04-29","is_origin_airport":false,"is_destination_airport":false},{"origin":"OVB","destination":"MOW","date":"2025-04-30","is_origin_airport":false,"is_destination_airport":false}],
                                   "passengers":{"adults":1,"children":1,"infants":0},"trip_class":"Y"},"client_features":{"direct_flights":true,"brand_ticket":false,"top_filters":true,"badges":false,"tour_tickets":true,"assisted":true},
                  "market_code":"ru","marker":"15468.ydall22247596093780","citizenship":"RU","currency_code":"rub","languages":{"ru":1}}

        headers = {
            'content-type': 'application/json',
            'x-client-type': 'web',
            'x-origin-cookie': self.token
        }
        path = self.base_url
        resp = requests.post(path, headers=headers,json=params,cookies=cookie)
        return resp.status_code

    @allure.step("невалидный API запрос без пассажиров")
    def ticket_passenger_non(self, false=None, true=None,) -> int:
        params = {"search_params":{"directions":[{"origin":"MOW","destination":"OVB","date":"2025-04-29","is_origin_airport":false,"is_destination_airport":false},{"origin":"OVB","destination":"MOW","date":"2025-04-30","is_origin_airport":false,"is_destination_airport":false}],
                                   "passengers":{"adults":0,"children":0,"infants":0},"trip_class":"Y"},"client_features":{"direct_flights":true,"brand_ticket":false,"top_filters":true,"badges":false,"tour_tickets":true,"assisted":true},
                  "market_code":"ru","marker":"15468.ydall22247596093780","citizenship":"RU","currency_code":"rub","languages":{"ru":1}}

        headers = {
            'content-type': 'application/json',
            'x-client-type': 'web',
            'x-origin-cookie': self.token
        }
        path = self.base_url
        resp = requests.post(path, headers=headers,json=params,cookies=cookie)
        return resp.status_code

    @allure.step("невалидный API запрос без указания куда")
    def ticket_not_destination(self, false=None, true=None,) -> int:
        params = {"search_params": {"directions": [
            {"origin": "MOW", "destination": "", "date": "2025-04-29", "is_origin_airport": false,
             "is_destination_airport": false}],
                                    "passengers": {"adults": 1, "children": 0, "infants": 0}, "trip_class": "Y"},
                  "client_features": {"direct_flights": true, "brand_ticket": false, "top_filters": true,
                                      "badges": false, "tour_tickets": true, "assisted": true},
                  "market_code": "ru", "marker": "15468.ydall22247596093780", "citizenship": "RU",
                  "currency_code": "rub", "languages": {"ru": 1}}

        headers = {
            'content-type': 'application/json',
            'x-client-type': 'web',
            'x-origin-cookie': self.token
        }
        path = self.base_url
        resp = requests.post(path, headers=headers, json=params, cookies=cookie)
        return resp.status_code