from urllib.request import urlopen
from atlasUtil import loadsJsonp
from atlasUtil import convertListDate
from atlasUtil import findLatestRelease
from atlasUtil import findLatestLongTermRelease

#Current Versions Confluence
#https://my.atlassian.com/download/feeds/current/confluence.json

#getConfluence Version
#https://www.atlassian.com/software/confluence/download-archives

#Long Term Releases
#https://confluence.atlassian.com/enterprise/atlassian-enterprise-releases-948227420.html

##########################################################################
#### Properties
##########################################################################
longTermRelease=7
jsonurl="https://my.atlassian.com/download/feeds/current/confluence.json"

##########################################################################
#### Script Run
##########################################################################

response=urlopen(jsonurl)

json_str=response.read().decode('utf-8')

json_list=loadsJsonp(json_str)

convertListDate(json_list, '%d-%b-%Y')

print('#################################################################################')
print("Latest Release: " + findLatestRelease(json_list))
print("Latest LTS: " + findLatestLongTermRelease(json_list, longTermRelease))
print('#################################################################################')
