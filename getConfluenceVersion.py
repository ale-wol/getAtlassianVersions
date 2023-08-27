from urllib.request import urlopen
from packaging.version import parse
from atlasUtil import loadsJsonp
from atlasUtil import convertListDate
from atlasUtil import findLatestEnterpriseRelease

#Current Versions Confluence
#https://my.atlassian.com/download/feeds/current/confluence.json

#getConfluence Version
#https://www.atlassian.com/software/confluence/download-archives

#Long Term Releases
#https://confluence.atlassian.com/enterprise/atlassian-enterprise-releases-948227420.html

##########################################################################
#### Properties
##########################################################################
jsonurl="https://my.atlassian.com/download/feeds/current/confluence.json"
currentInstalledConfluenceVersion="7.20"

##########################################################################
#### Script Run
##########################################################################

response=urlopen(jsonurl)

json_str=response.read().decode('utf-8')

json_list=loadsJsonp(json_str)

convertListDate(json_list, '%d-%b-%Y')

print('#################################################################################')
## print("Latest Release: " + findLatestRelease(json_list))
currentAtlassianEnterpriseVersion = findLatestEnterpriseRelease(json_list)
print("Latest Confluence Enterprise(LTS) Release: " + currentAtlassianEnterpriseVersion)
print('#################################################################################')

parsedAtlasVersion =  parse(currentAtlassianEnterpriseVersion) 
parsedInstalledVersion = parse(currentInstalledConfluenceVersion)


if parsedInstalledVersion < parsedAtlasVersion:
    print('There is a new Version available:' + currentAtlassianEnterpriseVersion)
    exit(1)
else:
    exit(0)