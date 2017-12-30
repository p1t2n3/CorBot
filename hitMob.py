# -*- coding: utf8 -*-
import json
import time
from time import sleep

import requests
from jsontraverse.parser import JsonTraverseParser

import os
import jprops



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
headers = {}
# directoryLocation = "/Users/max/Documents/Project/mitmSource/mitmproxy/examples/botVerOne/"
directoryLocation = os.getcwd()
wantedMobs = 63

#read Data from a property file
# cp = configparser.ConfigParser()
# cp.readfp(open(directoryLocation+"/general.properties"))
# testValriable = cp.getint("mainUrl")

# p = Properties()
# with open(directoryLocation+"/general.properties", "r") as f:
# 	p.load(f,"utf-8")
#
# for key in p.keys():
# 	print(key, p[key])
# testVal = p["foo"]

with open(directoryLocation+'/general.properties') as fp:
  properties = jprops.load_properties(fp)

currentURL = properties["url"]
class botV1:

    def __init__(self):
        print("new bot")

    # Get All info from boss loc
    def getAllInfo(cookieInput):
        with open('botLoc.json') as data_file:
            data = json.load(data_file)
            dumpedData = json.dumps(data)
        url = currentURL+"/api/Alliance/getFieldBossHelpRequests"
        global rhash
        global userAgent
        global cookie
        global bossList
        global content_Type
        global host
        global accept_Encoding
        global connection
        global x_Unity_Version

        rhash = "7036377b-366c-4352-beb2-3be0877962cb"
        cookie = cookieInput
        userAgent = "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K)"
        content_Type = "application/json"
        accept_Encoding = "gzip"
        connection = "Keep-Alive"
        x_Unity_Version = "5.4.3p3"
        host = "w024.cryuni.com"
        # headers = flow.request.headers

        parser = JsonTraverseParser(dumpedData)
        bossList = parser.traverse("field_bosses.field_detail.position")
        # filter list
        bossList = bossList[:wantedMobs]
        print(bossList)
        print(url + "\n")

    def startHitting(location):
        url = currentURL+"/api/Field/marchFieldBoss"
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

        # get Payload
        with open('/Users/max/Documents/Project/mitmSource/mitmproxy/examples/botVerOne/hitBoss.json') as data_file:
            data = json.load(data_file)
            data["destination"] = location
            jsonPayload = json.dumps(data)
            #gzip payload
            # out = io.BytesIO()
            # with gzip.GzipFile(fileobj=out, mode='w') as fo:
            #     fo.write(jsonPayload.encode())
            # gzippedObj = out.getvalue()
        localHeaders = {
            'Cookie': cookie,
            'Content-Type': content_Type,
            'X-Unity-Version': x_Unity_Version,
            'rhash': rhash,
            'User-Agent': userAgent,
            'Host': host,
            'Connection': connection,
            'Accept-Encoding': accept_Encoding,
            'Content-Length': content_Length }
        botV1.RefillStamima("Potion")
        mobAlive = True
        while mobAlive == True:
            # make Http call
            r = requests.post(url, data=jsonPayload, headers=localHeaders)
            body = r.content.decode()
            parsedJson = json.loads(body)
            # body = r.content.
            # jsonRes = parsedJson.decode("utf-8")
            parser = JsonTraverseParser(body)
            bossStatus = parser.traverse("application_error.message")
            stamStatus = parser.traverse("application_error.message_code")
            print(bossStatus)

            if bossStatus == "Not enough Aura.":
                botV1.RefillStamima("Potion")
            elif bossStatus == "No Monsters at destination.":
                print("Monster is Dead")
                mobAlive = False
            elif bossStatus == 'Hero not in condition to go on mission.':
                sleep(10)
            elif bossStatus == 'Unable to Deploy Troops to specified location.':
                mobAlive = False
            elif bossStatus == 'ログインしていません。':
                mobAlive = False
            elif bossStatus == "Unable to Deploy Troops as destination is too far away.":
                mobAlive = False
            elif bossStatus == "You cannot Deploy Troops to your own base.":
                mobAlive = False
            elif bossStatus == "Max no. of Deployments reached.":
                mobAlive = False
            elif bossStatus == None:
                sleep(1)
            sleep(0.3)

    def hitByList(list):
        print("Start Hitting!")
        # localHeaders.
        # try:
        # remove last few boss
        finished = 0
        #start normal
        for x in list:
                botV1.startHitting(x)
                print("Move to next target, finished target")
                finished += 1
                print(finished)


        print("Ending!!!")
        # except KeyboardInterrupt:
        #     pass

    def RefillStamima(anything):
        print(anything)
        print("Drink Potion!")
        url = currentURL+"/api/Item/useConsumable"
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

        #set Header
        localHeaders = {
            'Cookie': cookie,
            'Content-Type': content_Type,
            'X-Unity-Version': x_Unity_Version,
            'rhash': rhash,
            'User-Agent': userAgent,
            'Host': host,
            'Connection': connection,
            'Accept-Encoding': accept_Encoding,
            'Content-Length': '109'}
        # get Payload
        with open(directoryLocation+'usePot.json') as data_file:
            data = json.load(data_file)
            jsonPayload = json.dumps(data)
        # make Http call
        r = requests.post(url, data=jsonPayload, headers=localHeaders)
        # check response
        body = r.content.decode()
        # parsedJson = json.loads(body)
        # print(parsedJson)
        # TODO need to handled the response here
        assert r.status_code == 200
    def hitByArea(currentPosition, maxRadius):
        xVal = 65536
        yval = 1
        currentRadius = int(maxRadius)
        for x in range(-currentRadius,currentRadius+1,1):
            for y in range(-currentRadius,currentRadius+1,1):
                targetPosition = currentPosition+(x * xVal) + (y * yval)
                print("Target location",targetPosition)
                botV1.startHitting(targetPosition)
        # sleep(300)


    def readBookMark(bookMarkPosition):
        text_file = open("wantedBoss", "r")
        wantedBoss = text_file.readlines()
        text_file.close()
        url = currentURL+"/api/Bookmark/addBookmark"
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

        #set Header
        localHeaders = {
            'Cookie': cookie,
            'Content-Type': content_Type,
            'X-Unity-Version': x_Unity_Version,
            'rhash': rhash,
            'User-Agent': userAgent,
            'Host': host,
            'Connection': connection,
            'Accept-Encoding': accept_Encoding,
            'Content-Length': '80'}

        with open('/Users/admin/Documents/mitmSource/mitmproxy/examples/botVerOne/addBM2') as data_file:
            data = json.load(data_file)
            data['position']['position'] = bookMarkPosition
            jsonPayload = json.dumps(data)
        r = requests.post(url, data=jsonPayload, headers=localHeaders)
        # http.HTTPRequest(metho,)
        # assert r.status_code == 200
        body = r.content.decode()
        # parsedJson = json.loads(body)
        print("response bookmark:",body)
        parser = JsonTraverseParser(body)
        itemName = parser.traverse("bookmarks.item.name")
        if itemName in wantedBoss:
            bossPosition = parser.traverse("bookmarks.position.position")
            bossList.append(bossPosition)
        bookMarkID = parser.traverse("bookmarks.item.id")
        #set header forDeletiion
        sleep(0.5)
        url = currentURL+"/api/Bookmark/removeBookmark"
        localHeaders = {
            'Cookie': cookie,
            'Content-Type': content_Type,
            'X-Unity-Version': x_Unity_Version,
            'rhash': rhash,
            'User-Agent': userAgent,
            'Host': host,
            'Connection': connection,
            'Accept-Encoding': accept_Encoding,
            'Content-Length': '12'}
        with open('/Users/admin/Documents/mitmSource/mitmproxy/examples/botVerOne/removeBookmark.json') as data_file:
            data = json.load(data_file)
            data["id"] = bookMarkID
            jsonPayload = json.dumps(data)
        r = requests.post(url, data=jsonPayload, headers=localHeaders)
        # http.HTTPRequest(metho,)
        assert r.status_code == 200
        body = r.content.decode()
        print(body)

    def getCookie(Anything):
        print("Renewing cookie!!!")
        text_file = open("cookieList", "r")
        cookieList = text_file.readlines()
        text_file.close()

        # cookie = random(cookieList)
        # set Header
        return cookieList[0]

    def fightForTIme(minutes,location,range):
        t_end = time.time() + 60 * minutes
        while time.time() < t_end:
            bot.hitByArea(location,range)
        print("End of fighting!!")



print("Starting!!!")
bot = botV1
tempvalue = bot.getCookie("Anything")
botV1.getAllInfo(botV1.getCookie("Anything"))
# botV1.hitByArea(13828547,5)
botV1.hitByList(bossList)
# botV1.fightForTIme(480,35258841,1)