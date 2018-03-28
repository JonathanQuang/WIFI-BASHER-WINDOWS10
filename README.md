# Wifi-Basher-Windows10
Brute force forgotten wifi passwords

# Purpose
If you have forgotten maybe the last three characters of your wifi password, then this is the tool for you.

Lets say your password is BobRen, but in your head, you only remember Bob***. In the <keyMaterial> of the
XML file, type in Bobaaa

Due to technical limitations and my relatively new entrance to the CS world (I wrote this when I was 17), I could only manage one
password bash per second (slightly over a second anyway)

# Disclaimer
This tool has only been tested with Verizon Fios Routers on a Windows10 laptop.
Any damage from using this tool is the user's problem.

DO NOT use this for any illegal activity.
DO read the How to Use Section
DO look at the example

PLEASE have python 2 installed and a path variable setup for python


# How to use
0. Connect to the Wifi network you desire as if you  knew the password to generate the network profile.
0a)view your network profiles in command prompt with "netsh wlan show profile"
0b)execute "netsh wlan export profile "type_profile_name_here" key=clear" and open the xml file to see if it
is compatible with the example.
1. Familiarize yourself with the example folder in this repo.
2. If you see INSERT STUFF HERE or anything of that nature, please use common sense and refer to the example
when filling it out. Alternatively, consider subsituting your own xml file.
3. Run the command prompt and cd into this repo
4. Run output.bat
5. If you ever need to stop the script, hit ctrl+c
