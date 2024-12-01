import requests
import json

def get_median_sale_prices(state:str, city:str) -> dict: 
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'RF_BROWSER_ID=5oPAg_gMQJCTBiuMm-bIyQ; RF_BROWSER_ID_GREAT_FIRST_VISIT_TIMESTAMP=2024-11-30T20%3A03%3A51.406521; RF_BID_UPDATED=1; _gcl_au=1.1.1665821269.1733025835; _scor_uid=10b5a57e86a74f72913db614e23fe892; __pdst=54964b8c47c6455d984c162891c42984; _fbp=fb.1.1733025835577.137341044353495583; _pin_unauth=dWlkPU1tVTJOalppTkRVdE5EUXhZUzAwTlRBeExUaGlaalF0TWpNeE5XSTNNVEJtTXpZeg; FEED_COUNT=%5B%22%22%2C%22f%22%5D; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.1710391891.1733025839; RF_VISITED=true; _tt_enable_cookie=1; _ttp=JddiY0W8fPUaWE8QRKLKD9e1FN-.tt.1; RF_TRAFFIC_SEGMENT=non-organic; searchMode=1; usprivacy=1---; audS=t; unifiedLastSearch=name%3DAustin%26subName%3DAustin%252C%2520TX%252C%2520USA%26url%3D%252Fcity%252F30818%252FTX%252FAustin%26id%3D2_30818%26type%3D2%26unifiedSearchType%3D2%26isSavedSearch%3D%26countryCode%3DUS; sortOrder=1; sortOption=special_blend; RF_LAST_NAV=0; RF_MARKET=austin; tude-rvn-rel-Mdd5C=1.4.0; cw-test-20241121-viewable-refresh=control; cw-test-20241121-intersection-observer=test; _sharedid=ff8edf49-abf0-4621-80f9-a9eb304c50d5; _sharedid_cst=VyxHLMwsHQ%3D%3D; pbjs_fabrickId=%7B%22fabrickId%22%3A%22E1%3APdaiJT_oj62K-r1xfDgWr0U8WGf5Fb1MTZ96miPB9YUjyeO7_hj1rcBhPqJfKZ_2WqjfuifTr55PGpW-YFu_sidUi8q-yN4YnfrRYjFNlYV3moBmlkzUBC0HgdsL_ouH%22%7D; pbjs_fabrickId_cst=VyxHLMwsHQ%3D%3D; __gads=ID=f36eae07214ccc9a:T=1733026512:RT=1733026512:S=ALNI_MbuSsgggXypUOx0iIPEef8gfdusYQ; __gpi=UID=00000faa700c92a2:T=1733026512:RT=1733026512:S=ALNI_MbwyhmTveHjktoIwaTFRqNRvv6m1w; __eoi=ID=ef5eae4c7e154a55:T=1733026512:RT=1733026512:S=AA-AfjZAm6RqHk7pcXBPW4A6zc57; cto_bidid=-GzBQ19iZzVIQ2FJYzhJd1U1ckF6a0MwQzdyJTJGMmZEWlFqRnZvVmV1dHpYcEY0bXBORVNnZE15TSUyRjh6bElKTnFNJTJGaklEWDRGR1hyZzVCS1E5VlQza1JsVDZWZyUzRCUzRA; _cc_id=d9141a401b3e931daf4b8432edaf7771; panoramaId_expiry=1733631313380; panoramaId=baf8270e3338bc847ff386b4ee60185ca02ca0337bf1607432aa68cb5da40b72; panoramaIdType=panoDevice; cto_bundle=p0K4q19La2J5SU9KS1VETHdLaHhiZVdNWlpSNzZJM0gwUWJLTUN6RjhsTlM2aSUyRmxacmx0cFhTbkNSR28zVyUyRmRNNUZZaG5FWHBsYXE2cmsyRnVQUFNocUZ4M2ZMTmptMWtqMVE1SkJoQ3lyUDRUVEZKJTJGT3NFTWw1N1lGamtPWmM5ZlNTQQ; _ga_P8GPVZXD5S=GS1.1.1733026507.1.0.1733026563.0.0.0; userPreferences=parcels%3Dtrue%26schools%3Dfalse%26mapStyle%3Ds%26statistics%3Dtrue%26agcTooltip%3Dfalse%26agentReset%3Dfalse%26ldpRegister%3Dfalse%26afCard%3D2%26schoolType%3D0%26viewedSwipeableHomeCardsDate%3D1733026569599; OptanonAlertBoxClosed=2024-12-01T04:16:10.896Z; _rdt_uuid=1733025834913.b27bf3e8-aebb-49f7-bff4-ca9881d30d78; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Dec+01+2024+09%3A16%3A11+GMT%2B0500+(Pakistan+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6c703972-c4b2-4cce-acc6-8ef783de4084&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=PK%3BPB; _uetsid=486b4310af9911efb2a20729f40120bd; _uetvid=486b7630af9911ef814c01313a107459; RF_CORVAIR_LAST_VERSION=551.1.0; RF_BROWSER_CAPABILITIES=%7B%22screen-size%22%3A3%2C%22events-touch%22%3Afalse%2C%22ios-app-store%22%3Afalse%2C%22google-play-store%22%3Afalse%2C%22ios-web-view%22%3Afalse%2C%22android-web-view%22%3Afalse%7D; _ga_928P0PZ00X=GS1.1.1733025834.1.1.1733026582.41.0.0; _ga=GA1.2.745046164.1733025835; aws-waf-token=21c35ecf-ad57-4df9-9fb3-8c88c7a92288:BQoAmlUeIWYAAAAA:LkuiLR7CLZf0YAn45CP6KFUFbU+RPTnTfGQbdRIZRAOfp7IOz1KQ6pTteBaP2jk4wxyc1DCRaEKmxIRk0cs4UtTxM3LisM2esNGLpQNuyxNowjE/cEhh0huoE9fzo5JjHuIrNU+N3Dux7PdFC4tuYuH7Q5GTcn2R+u88KEkfjGOl1IDCYats6cDKW2Yybc0NTvB6CIWgOHwip9eqiDTGsoCmP8aCE8B1hVlz20pwsqci+1T2RCpYLLbu5D8qIX57/w==; _dd_s=rum=0&expire=1733027539913',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }



    params = {
        'location': f'{city}, {state}',
    }

    response = requests.get(
        'https://www.redfin.com/stingray/do/location-autocomplete',
        params=params,
        headers=headers,
    )

    try:
        code = json.loads(response.text.split("&&")[1])['payload']['regionViews']['__root'][0]['__atts'][0]['tableId']
    
    except:
        print("Could not find city code. Please check input city and state.")
        return {}

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'RF_BROWSER_ID=5oPAg_gMQJCTBiuMm-bIyQ; RF_BROWSER_ID_GREAT_FIRST_VISIT_TIMESTAMP=2024-11-30T20%3A03%3A51.406521; RF_BID_UPDATED=1; _gcl_au=1.1.1665821269.1733025835; _scor_uid=10b5a57e86a74f72913db614e23fe892; __pdst=54964b8c47c6455d984c162891c42984; _fbp=fb.1.1733025835577.137341044353495583; _pin_unauth=dWlkPU1tVTJOalppTkRVdE5EUXhZUzAwTlRBeExUaGlaalF0TWpNeE5XSTNNVEJtTXpZeg; FEED_COUNT=%5B%22%22%2C%22f%22%5D; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.1710391891.1733025839; RF_VISITED=true; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Dec+01+2024+09%3A06%3A40+GMT%2B0500+(Pakistan+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6c703972-c4b2-4cce-acc6-8ef783de4084&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.redfin.com%2Fcity%2F30818%2FTX%2FAustin%2Fhousing-market&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1; _rdt_uuid=1733025834913.b27bf3e8-aebb-49f7-bff4-ca9881d30d78; _uetsid=486b4310af9911efb2a20729f40120bd; _uetvid=486b7630af9911ef814c01313a107459; _ga_928P0PZ00X=GS1.1.1733025834.1.1.1733026000.59.0.0; _tt_enable_cookie=1; _ttp=JddiY0W8fPUaWE8QRKLKD9e1FN-.tt.1; RF_CORVAIR_LAST_VERSION=551.1.0; _ga=GA1.2.745046164.1733025835; RF_BROWSER_CAPABILITIES=%7B%22screen-size%22%3A3%2C%22events-touch%22%3Afalse%2C%22ios-app-store%22%3Afalse%2C%22google-play-store%22%3Afalse%2C%22ios-web-view%22%3Afalse%2C%22android-web-view%22%3Afalse%7D; aws-waf-token=21c35ecf-ad57-4df9-9fb3-8c88c7a92288:BQoAqcscW7kNAAAA:J3Oy8ua911msCoCSecP9LP8VR8m6EpMlCqlkDqEeAkiyIALiP4zaChp9sLBr8uEKhRbL4p+vXoUN/Pk8zpnPfQm4cLZo7cZvoD7xILIG2xARw7gYTpTjVikOK673oO6sP0TLrzVg1JafeByHE0SalqmshbpPda0P4W+EgpNg0scmMxhHS3I1GUu0ObZrru8tedCGanArpMjRZRwlrRFSNluoNepIG0IyKPdJEyXgICdcy0IOPkX/bf90Riqx1OBOLw==; _dd_s=rum=0&expire=1733027254805',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }


    try:
        response = requests.get(
            f'https://www.redfin.com/stingray/api/graph/6/{code}/All/regional-housing-market/home_prices',
            headers=headers,
        )

        data = json.loads(response.text.split("&&")[1])['payload']['metrics'][1]['aggregateData']

        res = {x['date'].rsplit("-",1)[0]:x['value'] for x in data}

        return res
    except:
        if response.status_code != 200:
            print("Request Error.")
        else:
            print("Counldn't get data")
        return {}


if __name__ == "__main__":
    data = get_median_sale_prices("Austin", "TX")
    print(data)