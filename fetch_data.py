import requests
import json
import os
import xmltodict
import time
from datetime import datetime


class Api_Call():
    def __init__(self, key_file="key_param.json", link_file="link.json", ):
        self.encode_key, self.decode_key, self.station_key = self.parse_key(key_file)
        self.arrival_url, self.station_url = self.parse_link(link_file)
        self.station_ids = self.get_station_ids()
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

    def get_station_ids(self, station_name=None):
        if station_name is None:
            return [214001274, 121000009, 214001182]
        if len(station_name) == 0:
            raise KeyError  # Check for details
        raise NotImplementedError
        # 평택신안인스빌 : 214001274
        # 신분당선강남역 : 121000009
        # 고덕르폴로랑아파트 : 214001182
        # openapi.gbis.go.kr/ws/rest/busstationservice?serviceKey=1234567890&keyword=고덕르폴로랑아파트

    def store_station_data(self, TIME_INTERVAL_SEC):
        # 판교도서관:206000004
        while True:
            if not int(time.time()) % TIME_INTERVAL_SEC == 0:
                pass
            else:
                for station_id in self.station_ids:
                    key = self.encode_key
                    url = "http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList?serviceKey={}&stationId={}".format(
                        key, station_id)
                    response = requests.get(url).content
                    current_date = str(datetime.now().strftime("%Y%m%d"))
                    current_time = str(datetime.now().strftime("%H%M"))
                    pathdir_to_save = os.path.join("data/data_to_parse/", current_date)
                    if not os.path.isdir(pathdir_to_save):
                        os.mkdir(pathdir_to_save)
                    with open(pathdir_to_save +"/"+ current_time + "_" + str(station_id) + ".txt", "wb") as f:
                        f.write(response)
                print(str(datetime.now().strftime("%H:%M")) + ", file saved")
                time.sleep(240)

            try:
                pass
            except KeyboardInterrupt as e:
                print(e)
                return


if __name__ == "__main__":
    # Airflow / Jenkins
    import time


    Api_Call().store_station_data(TIME_INTERVAL_SEC=300)  # 신분당선강남여121000009
        # 구미동차고지 206000335
