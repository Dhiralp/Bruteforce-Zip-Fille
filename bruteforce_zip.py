# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:21:48 2021

@author: Dhiral
"""

from zipfile import ZipFile
import argparse
parser = argparse.ArgumentParser(description="\nUsage: python bruteforce_zip.py -z <zipfile.zip> -p <passwordlist.txt>")
parser.add_argument("-z", dest="ziparchive", help="Zip archive file")
parser.add_argument("-p", dest="passfile", help="Password file")
parsed_args = parser.parse_args()

try:
    ziparchive = ZipFile(parsed_args.ziparchive)
    print(ziparchive)
    passfile = parsed_args.passfile
    foundpass = ""
    
except:
    print(parser.description)
    exit(0)
    
    
with open(passfile,"r") as f:
    for line in f:
        password = line.strip("\n")
        password = password.encode("utf-8")
        
        try:
            foundpass = ziparchive.extractall(pwd=password)            
            if foundpass==None:
                print("Found Password : ",password.decode())
                break
                
        except RuntimeError:
            pass
        
    if foundpass=="":
        print("\n  Password not found. Try a bigger password list.")