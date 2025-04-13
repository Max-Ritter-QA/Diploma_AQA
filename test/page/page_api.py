import requests

class AviaApi:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get_tickets(self, false=None, true=None,) -> int:
        params = {"search_params":{"directions":[{"origin":"MOW","destination":"OVB","date":"2025-04-29","is_origin_airport":false,"is_destination_airport":false},{"origin":"OVB","destination":"MOW","date":"2025-04-30","is_origin_airport":false,"is_destination_airport":false}],
                                   "passengers":{"adults":4,"children":0,"infants":0},"trip_class":"Y"},"client_features":{"direct_flights":true,"brand_ticket":false,"top_filters":true,"badges":false,"tour_tickets":true,"assisted":true},
                  "market_code":"ru","marker":"15468.ydall22247596093780","citizenship":"RU","currency_code":"rub","languages":{"ru":1}}
        headrs = {
            'content-type':'application/json',
            'x-client-type': 'web',
            'x-origin-cookie':'auid=MzhaeWdXBvdHc3FwcnJOAg==; nuid=cad7befa-5ab7-4a67-96ca-a4d9b1960688; email=maxritterr%40gmail.com; know_english=false; uxs_uid=7eb35b90-b95f-11ef-980f-8524cb45befd; _yoid=d09e0082-bd0a-479c-9782-8f5534dea54d; carrotquest_device_guid=874cc4c4-8c90-4d51-bfd2-9b06099d2407; carrotquest_uid=1864235335890764183; carrotquest_auth_token=user.1864235335890764183.29973-d9e118c419c052de7f78078232.edb3a72cd4e6655bf79cfb4115057fd1c8ae8100adaea617; currency=RUB; _gcl_au=1.1.617951099.1741890103; currency=rub; marker=15468.ydall22247596093780; domain_sid=sWTqpz7IhVXzMsduGQBrH%3A1744484920637; _ym_uid=1733756669779563475; _ym_d=1744496926; tmr_lvid=e1586268e3727c3f169d3843c0f95f7f; tmr_lvidTS=1733756668836; cookies_policy=%7B%22accepted%22%3Atrue%2C%22technical%22%3Atrue%2C%22marketing%22%3Atrue%7D; uncheck_hotel_cookie=true; _yosid=43f14f78-7db3-49cf-842e-eda523ba0378; _clck=r291dm%7C2%7Cfv1%7C0%7C1815; _sp_ses.dc27=*; _awt=4268148ea0375335626395033093105a3b6b43e3-6386a27b5663323abb4322726465136c66536653; _ym_visorc=b; _ym_isad=2; tmr_detect=0%7C1744570283864; _clsk=1edo4ur%7C1744571433456%7C5%7C0%7Cq.clarity.ms%2Fcollect; _sp_id.dc27=657cb331-38d8-4ba9-aa24-655c53ca908a.1733756667.32.1744571456.1744500831.8c0eb906-005f-4e16-a414-615ef1d7ba81.7c8273e1-aef8-4b9b-9ab5-eb514d77b2e4.0692d115-6f73-4835-9e98-2ed040d7cc7b.1744570277775.73'
        }
        path = self.base_url
        cookie = {
            'name': 'nuid',
            'value':'81cb6107-fc92-4bd9-be60-3e7c1c47454b',
            'domain': 'aviasales.ru'
        }
        resp = requests.post(path, headers=headrs,json=params,cookies=cookie)
        # return resp.json()
        return resp.status_code