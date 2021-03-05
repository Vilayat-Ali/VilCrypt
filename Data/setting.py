
# Name: setting.py
# Project: VilCRYPT
# Version: 1.0
# Description: This file will be handling user defined settings for the application


# Importing necessary modules
import os

# ------------------------------------------------------------------------------------
# TO EDIT A SETTING IN A USER-DEFINED SETTING:
#     To use edit function to change anything in the user defined settings
#     obj = Setting()
#     obj.edit("USER DEFINED SETTING", "VALUE")
# -------------------------------------------------------------------------------------
# This is used to search for the value of a required setting key in the user.bat file
#     obj = Setting()
#     variable = obj.tellSetting("option in th settings")
# -------------------------------------------------------------------------------------
# obj = Setting()
# =>Only to understand => obj.reset("HISTORY OF ACTIVITES", "RESET ALL USERDEFINED INFO")
# =>Correct => obj.reset(settings/history)
# -------------------------------------------------------------------------------------

class Setting:
    def __init__(self):
        # Predefined User setting fields
        self.info=["NO: 0\n","USERNAME: \n","ORGANIZATION: \n","ENCRYPTION MODE: \n"]
        # User defined settings
        try:
            fs=open("Settings//User.bat")
        except FileNotFoundError:
            # Tells whether the user has refreshed settings/started off with the application
            try:
                os.mkdir("Settings")
            except FileExistsError:
                pass
            fs=open("Settings//User.bat","w")
            # User defined settings
            for x in self.info:
                fs.write(x)
        finally:
            fs.close()
        # User defined settings

        # Application usage history
        try:
            fs=open("Settings//Activity.bat")
        except FileNotFoundError:
            # Tells whether the user has refreshed settings/started off with the application
            try:
                os.mkdir("Settings")
            except FileExistsError:
                pass
            fs=open("Settings//Activity.bat","w")
            # User defined settings
        finally:
            fs.close()
        # Application usage history


# No in the Settings//User.bat will be denoting whether a person has just started off with VilCrypt or he has previously used it before.
#       No equal to zero means that the user has just started off.
#       After every visit the value to No will change/edit automatically.


    def edit(self, option, editData):
        option=option.lower()
        sett=[]
        bat = open("Settings//User.bat", "r")
        for x in bat:
            sett.append(x)
        fs=open("Settings//User.bat")
        data=fs.readlines()
        fs.close()
        N=0
        for line in data:
            Line = line.lower()
            n=0
            for ch in Line:
                if(ch==":"):
                    break
                else:
                    n=n+1
            search=Line[0:n]
            if(search==option):
                dt=str(line[0:n])
                dt=dt+': '
                data[N]=dt+editData+"\n"
                sett[N]=data[N]
                fs=open("Settings//User.bat", "w")
                for x in sett:
                    fs.write(x)
                fs.close()
            else:
                N=N+1

# This is used to search for the value of a required setting key in the user.bat file
# obj = Setting()
# variable=obj.tellSetting("option in th settings")

    def tellSetting(self, option):
        option=option.lower()
        fs=open("Settings//User.bat","r")
        N=0
        key=[]
        value=[]
        for line in fs:
            orgl=line
            line=line.lower()
            try:
                for ch in range(1000):
                    if(line[ch]==":"):
                        N=ch
                        key.append(line[0:ch])
                        value.append(orgl[(N+1):(len(orgl)-1)])
                    else:
                        pass
            except IndexError:
                pass
# Finding a perfect for the searched value
        for x in range(len(key)):
            if(key[x]==option):
                return value[x]

    def reset(self, mode):
        mode=mode.lower()
        if(mode=='settings'):
            os.remove("Settings//User.bat")
        elif(mode == 'history'):
            os.remove("Settings//Activity.bat")


