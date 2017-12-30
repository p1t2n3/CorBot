import requests
import json
import random
import time
from jsontraverse.parser import JsonTraverseParser
from time import sleep

# global env
rhash = ""
userAgent = ""
cookie = ""
x_Unity_Version = ""
host = ""
content_Type = ""
connection = ""
accept_Encoding = ""
content_Length = '65'
bossList = []
globalHeader = {}
directoryLocation = "/Users/max/Documents/Project/mitmSource/mitmproxy/examples/botVerOne/"
sleepTime = 8
class battle:
    def __init__(self):
        print("start build")
    def setHeader(currentCookies):
        # head
        global rhash
        global userAgent
        global cookie
        global content_Type
        global x_Unity_Version
        global host
        global connection
        global accept_Encoding
        global content_Length
        global globalHeader

        # set Header value
        rhash = "7036377b-366c-4352-beb2-3be0877962cb"
        cookie = currentCookies
        userAgent = "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K)"
        content_Type = "application/json"
        accept_Encoding = "gzip"
        connection = "Keep-Alive"
        x_Unity_Version = "5.4.3p3"
        host = "w024.cryuni.com"
        # set Header
        globalHeader = {
            'Cookie': cookie,
            'Content-Type': content_Type,
            'X-Unity-Version': x_Unity_Version,
            'rhash': rhash,
            'User-Agent': userAgent,
            'Host': host,
            'Connection': connection,
            'Accept-Encoding': accept_Encoding,
            'Content-Length': '109'
        }
    def high_attack(destination):
        print("High powerAttacking!!!!")
        url = "http://w024.cryuni.com/api/Field/march"
        # get Payload
        with open(directoryLocation+'high_march.json') as data_file:
            data = json.load(data_file)
            data['destination'] = destination
            jsonPayload = json.dumps(data)
        # make Http call
        r = requests.post(url, data=jsonPayload, headers=globalHeader)
        # check response
        body = r.content.decode()
        # parsedJson = json.loads(body)
        # print(parsedJson)
        parser = JsonTraverseParser(body)
        jobID = parser.traverse("sync.jobs.0.item.id")
        # TODO need to handled the response here
        assert r.status_code == 200
        return jobID
    def low_attack(destination):
        print("Low power Attack!!!!")
        url = "http://w024.cryuni.com/api/Field/march"
        # get Payload
        with open(directoryLocation+'low_march.json') as data_file:
            data = json.load(data_file)
            data['destination'] = destination
            jsonPayload = json.dumps(data)
        # make Http call
        r = requests.post(url, data=jsonPayload, headers=globalHeader)
        # check response
        body = r.content.decode()
        # parsedJson = json.loads(body)
        # print(parsedJson)
        parser = JsonTraverseParser(body)
        jobID = parser.traverse("sync.jobs.0.item.id")
        # TODO need to handled the response here
        assert r.status_code == 200
        return jobID
    def getCookie(Anything):
        print("Renewing cookie!!!")
        text_file = open("cookieList", "r")
        cookieList = text_file.readlines()
        text_file.close()
        # cookie = random(cookieList)
        # set Header
        return cookieList[0]
    def speedAttack(jobID,type):
        print("Speed up !!!")
        url = "http://w024.cryuni.com/api/Item/useConsumable"
        # if type=="high":
        #     # get Payload
        #     with open(directoryLocation + 'speedAttackHigh.json') as data_file:
        #         data = json.load(data_file)
        # elif type=="low":
        #     # get Payload
        with open(directoryLocation + 'speedAttackHigh.json') as data_file:
            data = json.load(data_file)
            data['item_use_option']['job_id'] = jobID
            jsonPayload = json.dumps(data)
        # make Http call
        r = requests.post(url, data=jsonPayload, headers=globalHeader)
        # check response
        body = r.content.decode()
        parsedJson = json.loads(body)
        print(parsedJson)
        assert r.status_code == 200
    #MainRun How many attack

    def runBot(times,destination):
        battle.setHeader(battle.getCookie("anything"))
        count = 0
        while count < times:
            jobID = battle.low_attack(destination)
            sleep(0.1)
            # X times of item uses
            for x in range(5):
                battle.speedAttack(jobID,"Low")
                sleep(1)
            # for x in range(7):
            #     battle.speedAttack(jobID,"Low")
            #     sleep(0.1)
            ++count



print("Starting!!!")
bot = battle
tempvalue = bot.runBot(1,7406413)