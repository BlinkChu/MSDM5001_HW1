import re

xml_content = ""
with open('blocklist.xml','r') as f:
    xml_content = f.read()

# print(xml_content)

block_pattern = '(?P<blockid><emItem blockID="i\d+" id="{.+}">)'
blockid_lst = re.findall(block_pattern,xml_content)

ID_pattern = '(?P<blockid><emItem blockID=".+" id=".+@.+">)'
emails_lst = re.findall(ID_pattern,xml_content)

# print out the
print('Now print out the text lines with the “blockID” values that start with the letter “i” or “g”, and end with digits')
for i in emails_lst:
    if not (('/' in i) or ('/' in i) or ('^' in i)):
        print(i)

print('Now print out the text lines where the “ID” values are email addresses')
for i in blockid_lst:
    print(i)