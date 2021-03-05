
# Name: Filer.py
# Project: VilCRYPT
# Version: 1.0
# Description: This file will be handling all file handling operations

import datetime
from tabulate import tabulate
import os



class Filer:

# To create a .txt file
# Obj=Filer(Filename.extension, FolderName)   => Make object
# obj.makeFile()  => Creates File

    def __init__(self, fname, dirname):
        d=datetime.datetime.now()
        self.fname=fname
        d=d.strftime("%c")
        self.dirname=dirname
        arr1=["PROGRAM", "VilCRYPT"]
        arr2=["VERSION", "1.0"]
        arr3=["PROGRAMMMER","SYED VILAYAT ALI RIZVI"]
        File=self.fname
        arr4=["ABOUT FILE", File.upper()]
        arr5=["TIME OF CREATION", d]
        data=[arr1, arr2, arr3, arr4, arr5]
        self.table=tabulate(data, tablefmt="pretty")

    def makeFile(self):
        try:
            os.mkdir(self.dirname)
        except FileExistsError:
            pass
        dirname=self.dirname
        fname=dirname+"//"+self.fname
        try:
            f=open(fname, "w")
            f.write(self.table+"\n")
            f.write("\n"*5)
            f.close()
        except FileNotFoundError:
            pass
    
    def writeFile(self, data):
        dirname=self.dirname
        data=data
        fname=dirname+"//"+self.fname
        f=open(fname, "a")
        f.write(data+"\n")
        f.close()
    
class Utility(Filer):

# To create Utility files
# Obj=Utility(FileTYPE)   => Make object
# obj.generate()  => Creates File
# File Types includes:
# help
# error
# activity.log

    def __init__(self, ftype):
        self.dirname = "User Files"
        self.ftype=ftype
        F=ftype+".txt"
        d=datetime.datetime.now()
        d=d.strftime("%c")
        arr1=["PROGRAM", "VilCRYPT"]
        arr2=["VERSION", "1.0"]
        arr3=["PROGRAMMMER","SYED VILAYAT ALI RIZVI"]
        arr4=["ABOUT FILE", F.upper()]
        arr5=["CREATED AT", d]
        data=[arr1, arr2, arr3, arr4, arr5]
        self.table=tabulate(data, tablefmt="pretty")

    def generate(self):
        ftype=self.ftype
        if(ftype.lower()=="help"):
            try:
                os.mkdir(self.dirname)
            except FileExistsError:
                pass

            try:
                fname=self.dirname+"//"+"Help.txt"
                try:
                    f=open(fname, "w")
                    f.write("\n"*5)
                    f.write("WELCOME to VilCRYPT \n")
                    f.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    f.write(self.table+"\n")
                    f.write("\n"*5)
                    f.write("GENERAL COMMANDS: \n")
                    f.write("~~~~~~~~~~~~~~~~~\n")
                    com = [["To Encrypt a Message: ", "ENCODE", "ENCODE - \"Message...\""], ["To Decrypt a Message: ", "DECODE", "DECODE - \"Message...\" - \"encryption key\" - \"path to the file with .vilC extension\""], ["To View History: ", "VIEW", "VIEW-ACTIVITY - (recent/viewall)"], ["To See Current Settings: ", "VIEW-SETTING", "VIEW-SETTINGS"], ["To Edit the Settings: ", "EDIT-SETTINGS","EDIT - SETTINGS"]]
                    Table=tabulate(com, headers=["PURPOSE", "COMMAND", "SYNTAX"], tablefmt="pretty")
                    f.write(Table+"\n")
                    f.write("\n"*5)
                    f.write("EXAMPLE: \n")
                    f.write("~~~~~~~~~~~\n")
                    example=[
                        ["ENCRYPTION", "ENCODE - \"Message...\"", "Hello World!", "ENCODE - Hello World!", '''Encryption Key: XXXXXXXXX
                        CIPER FILE SAVED AS \'filename.vilC\'
                        FILE PATH: path//to//the//File'''],
                        ["\n", "\n", "\n", "\n", "\n"],
                        ["DECRYPTION", "DECODE - \"{Encryption key}\" - \"{Path to the file}\"", "XXXXXXXX, Myfiles/Secret.vilC", "XXXXXXXX - Myfiles/Secret.vilC", '''Decryption Process Completed!
                        DECRYPTED FILE SAVED AS \'filename.vilC\'
                        FILE PATH: path//to//the//File'''],
                        ["\n", "\n", "\n", "\n", "\n"],
                        ["VIEW PAST ACTIVITIES", "VIEW-ACTIVITY", "VIEW-ACTIVITY", "VIEW-ACTIVITY", '''Command Executed Sucessfully!
                        activity.log MADE at path//to//file'''],
                        ["\n", "\n", "\n", "\n", "\n"],
                        ["VIEW CURRENT SETTINGS", "VIEW-SETTINGS", "VIEW-ACTIVITY", "VIEW-SETTINGS", '''SETTINGS:
                        USERNAME: XXXXXXX
                        ENCRYPTION MODE: encryption_level
                        Encryption ID: xxxx-xxxx'''],
                        ["\n", "\n", "\n", "\n", "\n"],
                        ["EDIT USER SETTINGS", "EDIT-SETTINGS - \'data to be editted\'", "USERNAME", "EDIT-SETTINGS - USERNAME", '''EXISTING USERNAME: xxxxx
                        NEW USERNAME: XXXXXX
                        Are you sure? (Y/N) Y
                        USERNAME changed Successfully''']]
                    Table=tabulate(example, headers=["TASK", "SYNTAX", "INPUT DATA", "SAMPLE", "OUTPUT DATA"], tablefmt="pretty", colalign=("center", "center", "center", "center","left"))
                    f.write(Table+'\n')
                    f.write("\n"*5)
                    f.write("LICENSE \n")
                    f.write("~~~~~~~ \n")
                    arr=[
                        ["PRODUCT NAME", "VilCRYPT 1.0"],
                        ["VERSION", "1.0.0"],
                        ["PROGRAMMED BY", "SYED VILAYAT ALI RIZVI"],
                        ["OWNED BY", "SYED VILAYAT ALI RIZVI"],
                        ["RIGHTS", "ALL RIGHT RESERVED"]]
                    data=tabulate(arr, tablefmt="pretty", colalign=("center", "center"), headers=["INFO", "DESCRIPTION"])
                    f.write(data+"\n")
                    f.write("\n"*2)
                    f.write("-------------------------------------------------------------------------------")
                except FileNotFoundError:
                    print("Error: "+self.fname+" not found!")
                finally:
                    f.close()
            except FileNotFoundError:
                pass

        elif(ftype.lower()=="license"):
            try:
                os.mkdir(self.dirname)
            except FileExistsError:
                pass

            fname=self.dirname+"//"+"License.txt"
            try:
                f=open(fname, "w")
                f.write("\n"*5)
                f.write("WELCOME to VilCRYPT \n")
                f.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                f.write(self.table+"\n")
                f.write("\n"*5)
            except FileNotFoundError:
                print("Error: License.txt does not exist!")
            finally:
                f.close()

        

    
