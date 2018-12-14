#!/usr/bin/python3

import sys
import os
import re
import requests

BASE_URL = "https://teamnewpipe.github.io/documentation"

RETURN_VALUE = 0

os.chdir("docs")
for filename in os.listdir():
    #print(filename + ":")
    if ".md" in filename:
        with open(filename) as file:
            filedata = file.read()
            for link in re.findall('\[.*\]\(([^\)]*)\)', filedata):
                if link.startswith("#"):
                    checkstring = "# " + link.replace("#", "").replace("-", " ")
                    if not checkstring in filedata.lower():
                        RETURN_VALUE = 1
                        print(filename + ": Could not find target for" + link)
                else:
                    if link.startswith("img/"):
                        link = BASE_URL + "/" + link
                    if not link.startswith("http"):
                        RETURN_VALUE = 1
                        print(filename + ": " + link + " is not filled out or not http")
                    elif not link.startswith("https"):
                        RETURN_VALUE = 1
                        print(filename + ": " + link + " is not https")
                    else:
                        res = requests.get(link)
                        if res.status_code != 200:
                            RETURN_VALUE = 1
                            print(filename + ": " + link + " returns " + str(res.status_code))

sys.exit(RETURN_VALUE)
