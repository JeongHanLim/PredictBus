import xml.etree.ElementTree as ET
import xmltodict
import os
""" 
    Parse xml file from "data_to_parse", and put data into MySQL.
    Change 
    Put data_to_parse when plateNo1 hs changed. 
    Don't care the situation of bus sequence being changed 
"""
class xml2mysql():
    def __init__(self):
        file_to_parse = os.listdir("data_to_parse")

    def parse(self):
        tree = ET.parse('data_to_parse/0729_121000009.txt')
        xml_data = tree.getroot()
        xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')

data_dict = dict(xmltodict.parse(xmlstr))





"""
 Structure of API
 response
 |- comMsgHeader
 |- msgHeader
    |- queryTime
    |- resultCode
    |- resultMessage
 |- msgBody
    |- busArrivalList
        List of dict, where dict.keys are 
        ['flag', 
        'locationNo1', 'locationNo2', 
        'lowPlate1', 'lowPlate2', 
        'plateNo1', 'plateNo2', 
        'predictTime1', 'predictTime2', 
        'remainSeatCnt1', 'remainSeatCnt2', 
        'routeId', 'staOrder', 'stationId']
    
"""
