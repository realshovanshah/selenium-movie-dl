@ECHO OFF
@py "%~dp0selenium-torrent.py" %*

IF %ERRORLEVEL% == 15 GOTO END 
setlocal
:PROMPT
SET /P AREYOUSURE=Would you like to install the required module: Selenium? (Y/N)?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

pip install selenium
@py "%~dp0\selenium-torrent.py" %*

:END
endlocal
@pause
