import re
import json
import datetime

##########################################################################
#### Methods
##########################################################################

def loadsJsonp(_jsonp):
    try:
         jsonRaw = re.match(".*?\(\[({.*})]\)",_jsonp,re.S).group(1)
         wrappedJson  = ''.join(('[',jsonRaw,']'))
         return json.loads(wrappedJson)
    except:
        raise ValueError('Invalid Input')

def convertListDate(json_list, format):
    for i in json_list:
        #print(datetime.datetime.strptime(i['released'], '%d-%b-%Y').strftime('%Y-%m-%d'))
        i['released'] = datetime.datetime.strptime(i['released'], format).strftime('%Y-%m-%d')
    return json_list

def findLatestRelease(json_list):
    youngestVersion = None
    youngestVersionReleased = datetime.time(0,0,0)
    for i in json_list:
        if(youngestVersion is None):
            youngestVersion=i['version']
            youngestVersionReleased=i['released']
        elif(youngestVersionReleased < i['released']):
            youngestVersionReleased=i['released']
            youngestVersion=i['version']
    return youngestVersion

def findLatestEnterpriseRelease(json_list):
    youngestVersion = None
    youngestVersionReleased = datetime.time(0,0,0)
    for i in json_list:
        if(i['edition']=="Enterprise"):
            if(youngestVersion is None):
                youngestVersion=i['version']
                youngestVersionReleased=i['released']
            elif(youngestVersionReleased < i['released']):
                youngestVersionReleased=i['released']
                youngestVersion=i['version']
    return youngestVersion

def findLatestLongTermRelease(json_list, longTermRelease):
    lts_json_list=list()
    youngestLtsVersion=None
    youngestLtsVersionReleased = datetime.time(0,0,0)
    for i in json_list:
        versionString=str(i['version'])
        if(versionString.startswith(str(longTermRelease))):
            lts_json_list.append(i)
    
    convertListDate(lts_json_list, '%Y-%m-%d')
    for i in lts_json_list:
        if(youngestLtsVersion is None):
            youngestLtsVersion=i['version']
            youngestLtsVersionReleased=i['released']
        elif(youngestLtsVersionReleased < i['released']):
            youngestLtsVersionReleased=i['released']
            youngestLtsVersion=i['version']
    
    return youngestLtsVersion
