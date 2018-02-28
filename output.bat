SET xmlFileName=Wi-Fi-#INSERT FILE NAME HERE#.xml
SET profileName=#INSERT FILE NAME HERE#

:loop
netsh wlan delete profile name=%profileName%
netsh wlan add profile filename=%xmlFileName%
netsh wlan connect %profileName%
TIMEOUT 1

ping google.com > pingResult.txt
python editor.py > pythonResult.txt
set /P pyResultText=<pythonResult.txt
echo oneBash

@echo off 

if %pyResultText%==yes (goto loop) else (echo "bashing Complete") 


