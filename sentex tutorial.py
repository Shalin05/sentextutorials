import statistics
import csv
import sys,urllib.request
'''
print ('THis is me shalin hellosnckjdjdakniueuf i uqwqudhi u iudhqiw uhiuw d')
x,y=32,'jewir'
print(x)
print(y)
condition=1
while condition < 10:
    print(condition)
    condition= condition+1
exampleList=[1,2,32,43,4,32,2,55,2,232,4,32,4]
for x in exampleList:
    print(x)
for x in range(1,12):
    print(x)

def example():
    print("hellow duhduuhdhojdojncjn")
    z=6+782
    print(z)
example()
def addition(num1, num3):
    z= num1+num3
    print(z)

addition(2,313)

text= "hello my name is Shalin\nI am an engineer "
sampleFile= open('test.txt','w')
sampleFile.write(text)
sampleFile.close()

appendText="New bit of information"
appendFile= open('test.txt','a')
appendFile.write(appendText)
appendFile.close()

readMe= open('test.txt','r').readlines()
print(readMe)

##x = input("What is your name? ")
##print("Hello",x)

y=[23,4,32,4,3,21,2,6,79,2,65,8,65,56,4]
mean=statistics.variance(y)
print(mean)
'''

with open('data.csv') as data:
    readCSV= csv.reader(data,delimiter=',')
    ls=[]
    ms=[]
    for row in readCSV:
        l=row[0]
        m=row[1]
        ls.append(l)
        ms.append(m)
    print(ls)
    print(ms)

whatNumber=input("What number you want? ")
indexNumber=ls.index(whatNumber)
indexOfM=ms[indexNumber]
print(indexOfM)

print('''
gfesdjjlddf
dsjfknd v
diflfjdlnc
dnieji3pq
''')

exDict={'Jack':15,'Bob':22,'Alice': 12,'Kevin':17}
print(exDict)
print(exDict['Jack'])
exDict['Tim'] = 15
print(exDict)
del exDict['Tim']
exDict['Jack'] = [15,'black']
print(exDict)
print(exDict['Jack'][1])

sys.stderr.write('This is stderr\n')
sys.stderr.flush()
sys.stdout.write('This is stdout\n')
print(sys.argv)

x=urllib.request.urlopen('https://www.google.com')

'''
File tutorial line 29
csv tutorial line 50
multi line print line 67
dictionary line 74
sys line 85
urllib line 90
'''