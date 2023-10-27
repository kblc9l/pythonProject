import re


s = 'purple aDice@gooGle.com, blah monkey boB@Bbc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', s, re.IGNORECASE )
for name, host in tuples:
    print(name, host)
