from urllib.request import urlopen
from atlasUtil import loadsJsonp
from atlasUtil import findLatestLongTermRelease
from atlasUtil import convertListDate

#https://www.atlassian.com/software/jira/update

##########################################################################
#### Properties
##########################################################################
jsonurl="https://my.atlassian.com/download/feeds/current/jira-software.json"
longTermRelease=9.4

##########################################################################
#### Script Run
##########################################################################
response=urlopen(jsonurl)

json_str=response.read().decode('utf-8')

json_list=loadsJsonp(json_str)
convertListDate(json_list, '%d-%b-%Y')

print('#################################################################################')
print(json_list)
print("Latest Release: " + findLatestLongTermRelease(json_list, longTermRelease))
print('#################################################################################')
