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
sleepTime = 1
class buildHouse:
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
    def delete_building(cookieInput):
        print("Delete Building")
        url = "http://w024.cryuni.com/api/City/deleteBuilding"
        # get Payload
        with open(directoryLocation+'deleteBuildingPayload.json') as data_file:
            data = json.load(data_file)
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
    def speedDelete(jobID):
        # jobID = buildHouse.delete_building(buildHouse.getCookie("temp"))
        print("Speed Delete")
        url = "http://w024.cryuni.com/api/Item/useConsumable"
        # get Payload
        with open(directoryLocation + 'speedUpPayload.json') as data_file:
            data = json.load(data_file)
            data['item_use_option']['job_id']=jobID
            jsonPayload = json.dumps(data)
        # make Http call
        r = requests.post(url, data=jsonPayload, headers=globalHeader)
        # check response
        body = r.content.decode()
        parsedJson = json.loads(body)
        print(parsedJson)
        # parser = JsonTraverseParser(body)
        # jobID = parser.traverse("sync.jobs.*.item.id")
        # TODO need to handled the response here
        assert r.status_code == 200
    def buildNewHouse(anything):
        print("New House")
        url = "http://w024.cryuni.com/api/City/createBuilding"
        # get Payload
        with open(directoryLocation + 'buildNewHouse.json') as data_file:
            data = json.load(data_file)
            jsonPayload = json.dumps(data)
        # make Http call
        r = requests.post(url, data=jsonPayload, headers=globalHeader)
        # check response
        body = r.content.decode()
        parsedJson = json.loads(body)
        print(parsedJson)
        parser = JsonTraverseParser(body)
        jobID = parser.traverse("sync.jobs.0.item.id")
        # TODO need to handled the response here
        assert r.status_code == 200
        return jobID
    def speedBuild(jobID):
        print("Speed build")
        url = "http://w024.cryuni.com/api/Job/completeJobInstantly"
        sleep(sleepTime)
        # get Payload
        with open(directoryLocation + 'speedBuildHouse.json') as data_file:
            data = json.load(data_file)
            data['id'] = jobID
            jsonPayload = json.dumps(data)
        # make Http call
        r = requests.post(url, data=jsonPayload, headers=globalHeader)
        # check response
        body = r.content.decode()
        parsedJson = json.loads(body)
        print(parsedJson)
        # TODO need to handled the response here
        assert r.status_code == 200
    def upgradeHouse(anything):
        print("Upgrade building")
        url = "http://w024.cryuni.com/api/City/upgradeBuilding"
        # get Payload
        with open(directoryLocation + 'upgradeHouse.json') as data_file:
            data = json.load(data_file)
            jsonPayload = json.dumps(data)
        # make Http call
        r = requests.post(url, data=jsonPayload, headers=globalHeader)
        # check response
        body = r.content.decode()
        parsedJson = json.loads(body)
        print(parsedJson)
        parser = JsonTraverseParser(body)
        jobID = parser.traverse("sync.jobs.0.item.id")
        # TODO need to handled the response here
        assert r.status_code == 200
        return jobID
    def runBot(times):
        count = 0
        buildHouse.setHeader(buildHouse.getCookie("anything"))
        jobID = ""
        while count < times:
            jobID = buildHouse.delete_building("Anything")
            sleep(sleepTime+4)
            buildHouse.speedDelete(jobID)
            sleep(sleepTime)
            jobID=buildHouse.buildNewHouse("Anything")
            sleep(sleepTime + 4)
            buildHouse.speedBuild(jobID)
            sleep(sleepTime)
            jobID=buildHouse.upgradeHouse("anything")
            sleep(sleepTime + 4)
            buildHouse.speedBuild(jobID)
            sleep(sleepTime)
            jobID=buildHouse.upgradeHouse("anything")
            sleep(sleepTime + 4)
            buildHouse.speedBuild(jobID)
            sleep(sleepTime)
            jobID=buildHouse.upgradeHouse("anything")
            sleep(sleepTime + 4)
            buildHouse.speedBuild(jobID)
            sleep(sleepTime)
            jobID=buildHouse.upgradeHouse("anything")
            sleep(sleepTime + 4)
            buildHouse.speedBuild(jobID)
            sleep(sleepTime)

print("Starting!!!")
bot = buildHouse
tempvalue = bot.runBot(5)