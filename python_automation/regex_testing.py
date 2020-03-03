import re, os
from collections import Counter

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

searchString = "My number is 415-555-4242 and my cell is 212-242-5433."
someText = """
415-555-4242
Harry Potter
10.140.120.11:4423 --> 192.12.232.123:80
10.140.120.231:80 --> 192.24.354.325:80
10.140.120.432:443 --> 124.24.232.543:443
10.140.120.11:4423 --> 192.12.232.123:3214
10.140.120.11:8080 --> 12.123.543.2:80
10.140.120.231:80 --> 192.24.354.325:80
212-435-4563
415-555-4242
415-555-4242
"""

phoneNumRE = re.compile(r"\d{3}-\d{3}-\d{4}")
IpRE = re.compile(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})", re.M)

mo = phoneNumRegex.search(searchString)
print(f"Phone number found: {mo.group()}")
print(f"Phone number found: {mo.group(0)}")
print(f"Phone number found: {mo.group(1)}")
print(f"Phone number found: {mo.group(2)}")
areaCode, mainNumber = mo.groups()
print(f"Area code found: {areaCode}")
print(f"Main phone number found: {mainNumber}")
print(f"Matching using findall(): {phoneNumRegex.findall(searchString)}")
print(f"Matching using findall(): {phoneNumRegex.findall(searchString)[1]}")
print(f"Matching using findall(): {phoneNumRegex.findall(searchString)[1][0]}")

print(os.getcwd())
print(os.path.abspath('.'))
with open('./regex_file.txt', 'r') as f:
    fileData = f.read()
    mo2 = phoneNumRegex.search(fileData)
    print(f"Phone number found: {mo2.group()}")

results = phoneNumRE.findall(someText)
c = Counter(results)
print({k:v for (k,v) in c.items() if v > 1})

resultsIP = IpRE.findall(someText)
cIP = Counter(resultsIP)
print({k:v for (k,v) in cIP.items() if v > 1})

srcResults = []
dstResults = []
for resultIP in resultsIP:
    srcResults.append(resultIP[0])
    dstResults.append(resultIP[2])
sIP = Counter(srcResults)
print(sIP)
dIP = Counter(dstResults)
print(dIP)
print({k:v for (k,v) in sIP.items() if v > 1})
print({k:v for (k,v) in dIP.items() if v > 1})

