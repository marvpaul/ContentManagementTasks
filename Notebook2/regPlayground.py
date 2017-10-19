import re

awesomeString = "Hello, this is just for testing purposes! :) :O"
awesomeChars = "CaseSensitive"
awesomeChars2 = "abc"

list={awesomeString, awesomeChars, awesomeChars2}
print(list)

for k in list:
    print(k)
    print(re.search("[a-z]*", k).span())
#print((re.search("{a-z}*", k) for k in list))