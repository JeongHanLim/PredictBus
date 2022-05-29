
import requests
import json
import xmltodict
from datetime import datetime

class get_station_data(object):
    def __init__(self, key_file = "key_param.json", link_file = "link.json"):
        self.encode_key, self.decode_key, self.station_key = self.parse_key(key_file)
        self.arrival_url, self.station_url = self.parse_link(link_file)
        self.station_id = 121000009 #신분당선강남역


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

    def get_station_id(self, station_name):
        pass
        #평택신안인스빌 : 214001274
        #신분당선강남역 : 121000009
        #고덕르폴로랑아파트 : 214001182
        #openapi.gbis.go.kr/ws/rest/busstationservice?serviceKey=1234567890&keyword=고덕르폴로랑아파트

    def realtime_status(self, station_id):
        #판교도서관:206000004
        key = self.encode_key
        url = "http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList?serviceKey={}&stationId={}".format(key,station_id)
        response = requests.get(url).content
        current_time = str(datetime.now().strftime("%H:%M"))
        with open("data/"+current_time+"_"+str(station_id)+".txt", "wb") as f:
           f.write(response)
        return



# response = requests.get(arrival_url, params=params)
# print(response.content)



if __name__ == "__main__":
    # Airflow / Jenkins 
    # station_key = get_station_name("신안인스빌")
    import time
    from threading import Thread
    TIME_INTERVAL = 5

    getter = get_station_data()
    while True:
        if int(time.time())%TIME_INTERVAL == 0:
            # TODO : Make each one's thread
            getter.realtime_status(121000009) # 신분당선강남여121000009
            getter.realtime_status(214001274)
            getter.realtime_status(214001182)
            # 구미동차고지 206000335
            print(str(datetime.now().strftime("%H:%M")) + ", file saved")
            time.sleep(60)

