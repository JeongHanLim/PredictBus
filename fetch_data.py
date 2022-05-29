
import requests
import json

class get_station_data(object):
    def __init__(self, station_name="신안인스빌", key_file = "key_param.json", link_file = "link.json"):
        self.encode_key, self.decode_key, self.station_key = self.parse_key(key_file)
        self.arrival_url, self.station_url = self.parse_link(link_file)
        self.station_id = self.get_station_id(self.station_url, self.station_key)

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

    def get_station_id(self, station_name)
        params= {}

    def something(self):
        params = {'serviceKey': '서비스키', 'stationId': '200000078'}
        response = requests.get(self.station_url, params=params)


        return



response = requests.get(arrival_url, params=params)
print(response.content)



if __name__ == "__main__":
    station_key = get_station_name("신안인스빌")

