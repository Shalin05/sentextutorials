'''
Identifiers:

    \d = any number
    \D = anything but a number
    \s = space
    \S = anything but a space
    \w = any letter
    \W = anything but a letter
    . = any character, except for a new line
    \b = space around whole words
    \. = period. must use backslash, because . normally means any character.

Modifiers:

    {1,3} = for digits, u expect 1-3 counts of digits, or "places"
    + = match 1 or more
    ? = match 0 or 1 repetitions.
    * = match 0 or MORE repetitions
    $ = matches at the end of string
    ^ = matches start of a string
    | = matches either/or. Example x|y = will match either x or y
    [] = range, or "variance"
    {x} = expect to see this amount of the preceding code.
    {x,y} = expect to see this x-y amounts of the precedng code

White Space Charts:

    \n = new line
    \s = space
    \t = tab
    \e = escape
    \f = form feed
    \r = carriage return

Characters to REMEMBER TO ESCAPE IF USED!

    . + * ? [ ] $ ^ ( ) { } | \

Brackets:

    [] = quant[ia]tative = will find either quantitative, or quantatative.
    [a-z] = return any lowercase letter a-z
    [1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z

'''

import re
import urllib.request
import urllib.parse
'''
url='http://pythonprogramming.net'
values={'\s':'basics','submit':'search'}
data= urllib.parse.urlencode(values)
data=data.encode('utf-8')
req= urllib.request.Request(url,data)
resp= urllib.request.urlopen(req)
respData=resp.read()

paragraphs=re.findall(r'<p>(.*?)</p>',str(respData))
for eachParagraph in paragraphs:
    print(eachParagraph)
'''

exampleString='''
7061-6-0-0.wav 123432-6-33-44.wav 21312-5-314-3.wav
'''
ages= re.findall(r'(\d{1,6}-6.*?\.wav)',exampleString)
#names= re.findall(r'[A-Z][a-z]*',exampleString)
print(ages)
#print(names)

#ageDict={}
#x=0
#for eachName in names:
 #   ageDict[eachName]= ages[x]
  #  x+=1

#print(ageDict)