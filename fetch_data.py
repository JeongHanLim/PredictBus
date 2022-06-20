
import requests
import json
import xmltodict
from datetime import datetime

class api_call(object):
    def __init__(self,  station, key_file = "key_param.json", link_file = "link.json",):
        self.encode_key, self.decode_key, self.station_key = self.parse_key(key_file)
        self.arrival_url, self.station_url = self.parse_link(link_file)
        self.station_ids = self.get_station_ids(station)
        print("requested station's station_id are ", self.station_ids, " in sequence")


    @staticmethod
    def parse_key(key_file):
        with open(key_file, "r+", encoding="utf-8") as f:
            key_data = json.load(f)
        return key_data["encoding_key"], key_data["decoding_key"], key_data["station_key"]

    @staticmethod
    def parse_link(link_file):
        with open(link_file, "r+", encoding="utf-8") as f:
            link_data = json.load(f)
        return link_data["arrival_url"], link_data["station_url"]

    def get_station_ids(self, station_name):
        if len(station_name) == 0:
            raise KeyError # Check for details
        return [214001274, 121000009, 214001182]
        #평택신안인스빌 : 214001274
        #신분당선강남역 : 121000009
        #고덕르폴로랑아파트 : 214001182
        #openapi.gbis.go.kr/ws/rest/busstationservice?serviceKey=1234567890&keyword=고덕르폴로랑아파트

    def store_station_data(self,TIME_INTERVAL_SEC):
        #판교도서관:206000004
        while True:
            if int(time.time()) % TIME_INTERVAL_SEC == 0:
                for station_id in self.station_ids:
                    key = self.encode_key
                    url = "http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList?serviceKey={}&stationId={}".format(key,station_id)
                    response = requests.get(url).content
                    current_time = str(datetime.now().strftime("%H:%M"))
                    with open("data_to_parse/"+current_time+"_"+str(station_id)+".txt", "wb") as f:
                       f.write(response)
        return


if __name__ == "__main__":
    # Airflow / Jenkins 
    # station_key = get_station_name("신안인스빌")
    import time
    from threading import Thread
    TIME_INTERVAL = 5

    api = api_call(station=["신안인스빌앞", "신분당선강남역"])
    getter = api_call.store_station_data(300)
    while True:
        if int(time.time())%TIME_INTERVAL == 0:
            # TODO : Make each one's thread
            getter.store_station_data(121000009, 300) # 신분당선강남여121000009
            getter.store_station_data(214001274, 300)
            getter.store_station_data(214001182, 300)
            # 구미동차고지 206000335
            print(str(datetime.now().strftime("%H:%M")) + ", file saved")
            time.sleep(60)

