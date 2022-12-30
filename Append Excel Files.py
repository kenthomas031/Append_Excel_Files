# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:11:47 2020

@author: u0a009
"""


import os

archiveFolder = '\\\\calpd1inf01\\GP-CALG-Share\\Zelalem_Python_Destination\\FNOLEmailTextPilot' #edit this line if the saved file changes
#fileName = 'et_fnol_hourly20200213_12h46m.txt'

archiveFiles = os.listdir(archiveFolder) #Getting names of all files in the folder

with open('myFile.txt','w') as newFile:  #you can rename the file to something more appropriate
    
    count = 0
    for fileName in archiveFiles: #iterating through folder
        if 'et_fnol_' in fileName: #edit this line to change surveys
            with open(archiveFolder + '\\' + fileName) as dataFile:
                if count == 0:
                    for line in dataFile:
                        newFile.write(line)
                else: #skipping the line for column names in the rest of the files
                    firstLineFlag = 0
                    for line in dataFile:
                        if firstLineFlag == 0:
                            pass
                        else:                            
                            newFile.write(line)
                        firstLineFlag += 1
                count += 1
