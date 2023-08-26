@echo off

SET projectDir=%~dp0

REM pause
"%projectDir%.venv\Scripts\python.exe" "%projectDir%getConfluenceVersion.py"

REM echo "Errorlevel" %ERRORLEVEL%
REM pause

if %ERRORLEVEL% == 1 (pause && echo "New Version available") else (echo "Do nothing")

REM pause
