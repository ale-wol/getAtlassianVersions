# Python Scripts to get Jira & Confluence current Version

## General
Some python Scripts to scrape Web Ressources from Atlassian and get the current LTS Version from Confluence and Jira.
You can also compare the current Version against an self configured Version to see if there is a new Version available.
There are also 2 Batch Scripts to automate the Python tasks in Windows

## Python Scripts

### getConfluenceVersion.py
Python Script to get the current LTS Confluence Version from Atlassian and compare it with an self configured.
If there is a newer Version available the Scripts exits with Code 1 if there isn't a new Version available the Scripts exits with Code 0.

### getJiraVersion.py
Python Script to get the current LTS Jira Version from Atlassian and compare it with an self configured.
If there is a newer Version available the Scripts exits with Code 1 if there isn't a new Version available the Scripts exits with Code 0.

### atlasUtil.py
Python Script where a some shared Methods which are used by getJiraVersion.py and getConfluenceVersion.py

## Batch Scripts

### run_get_conf_version_python.bat
This Script is used to automat the Python Script in an Windows environment.
Batch Script to run getConfluenceVersion.py and read out the error code and check if there is a newer Version available.

### run_get_jira_version_python.bat
This Script is used to automat the Python Script in an Windows environment.
Batch Script to run getJiraVersion.py and read out the error code and check if there is a newer Version available.