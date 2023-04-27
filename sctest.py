import os
import subprocess

def win():

    subprocess.Popen(["powershell.exe","./test.ps1"]) 

def unix():
    subprocess.Popen(['sh', './test.sh']) 

if (os.name == 'nt'):
    win() 


if(os.name == 'posix'):
    unix()
