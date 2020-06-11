#!/usr/bin/env python3
# This utility will sanitize a Microsoft Outlook Safelinks URL
import re
import string
URL = ""
headlessURL = ""
mydict = {"%2C":",","%2F":"/","%3A":":","%3D":"=","%3F":"?","%40":"@","%7C":"|","%26":"&","%2B":"+"}
URL = input("Input the Safelinks URL:\n")
if "safelinks.protection.outlook.com" in URL:
	print("URL integrity check...PASSED")
else:
	print("URL integrity check...FAILED")
size = len(URL)
headlessURL = URL[52:size]
for h in mydict:
	headlessURL=re.sub(h, mydict[h], headlessURL)
print("The sanitized URL is:", headlessURL)
