from fetch_data import api_call
from threading import Thread
TIME_INTERVAL_SEC = 300

class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(TIME_INTERVAL_SEC):
            # run a function
            pass


#TODO : GET DATA FROM TXTFILE
station=["신분당선강남역", "신안인스빌앞", "성균관대역"]
api = api_call(station = station, key_file="key_param.json", link_file="link.json",)
t_data_to_mysql = Thread(target=api.store_station_data, args=(TIME_INTERVAL_SEC,))


t_data_to_mysql.start()



