import re, os

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

searchString = "My number is 415-555-4242 and my cell is 212-242-5433."

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

