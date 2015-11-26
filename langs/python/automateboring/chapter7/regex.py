import re

# Example 1
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo =  phoneNumRegex.search('My number is 415-555-4242.')
print ('Phone number found: ' + mo.group())

# Example 2 - Grouping With parentheses
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo =  phoneNumRegex.search('My number is 415-555-4242.')

# All matches
print('mo group all: ' + mo.group())

# All matches
print('mo group 0: ' + mo.group(0))

# First match based on grouping
print('mo group 1: ' + mo.group(1))

# First match based on grouping
print('mo group 2: ' + mo.group(2))

# Print groups
print('Print groups: ' + str(mo.groups()))

# Define group members as variables
areaCode, mainNumber = mo.groups()

# Print the variables
print(areaCode)
print(mainNumber)

# Example 3 - Matching Multiple Groups with the Pipe
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print('mo group all: ' + mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print('mo group all: ' + mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print('mo group all: ' + mo.group())

# Get first match
print('mo group all: ' + mo.group())

# Get second match
print('mo group all: ' + mo.group(1))


# Example 4 - OPtional Matching with the Question Mark

# Match the man
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print('mo group match: ' + mo1.group())

# Match the woman
mo2 = batRegex.search('The Adventures of Batwoman')
print('mo group match: ' + mo2.group())

# Match an optional number
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

mo1 = phoneRegex.search('My number is 415-555-4242')
print('mo group match: ' + mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print('mo group match: ' + mo2.group())

print "\nExample 5 - Matching Zero or More with the Start"

# The  * (called the star or asterisk) means match zero or more
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print('mo group match: ' + mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print('mo group match: ' + mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowoman')
print('mo group match: ' + mo3.group())

print "\nExample 6 - Matching One or More with the Plus"

# the  + (or plus) means match one or more. appear at least once
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print('mo group match: ' + mo1.group())


mo2 = batRegex.search('The Adventures of Batwowowoman')
print('mo group match: ' + mo2.group())

print "\nExample 7 - Matching Specific Repetitions with Curly Brackets"

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print('mo group match: ' + mo1.group())

mo2 = haRegex.search('Ha') == None
#AttributeError NoneType
print(mo2) 

print "\nExample 8 - Greedy and Non Greedy Matching"

# Python regular expressions are greedy by default, which means that in
# ambiguous situations they will match the longest string possible.

greedyhaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyhaRegex.search('HaHaHaHaHa')
print('mo group match: ' + mo1.group())

greedyhaRegex = re.compile(r'(Ha){3,5}?')
mo2 = greedyhaRegex.search('HaHaHaHaHa')
print('mo group match: ' + mo2.group())

print "\nExample 9 - The findall() method"

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print('Print group: ' + mo.group())

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# Compiles a list and makes matches available by index
print('Compiles a list  ' + mo[0] + ' ' + mo[1])

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# Compiled list of groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

print "\nExample 10 - Character Classes"

'''
\d Any numeric digit from 0 to 9.
\D Any character that is  not a numeric digit from 0 to 9.
\w Any letter, numeric digit, or the underscore character.  (Think of this as matching "word" characters.)
\W Any character that is  not a letter, numeric digit, or the underscore character.
\s Any space, tab, or newline character. (Think of this as matching "space" characters.)
\S Any character that is  not a space, tab, or newline.
'''

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

print "\nExample 11 - Make your own Character Classes"
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD') 
print(mo)
'''
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
'''

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD') 
print(mo)
'''
['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D']
'''

print "\n Example 12 - The Caret and Dollar Sign Characters"

beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!') 
mo1 = beginsWithHello.search('He said hello.') == None
print(mo) ; print(mo1)
'''
<_sre.SRE_Match object at 0x6ffffe5b920>
True
'''

endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42') 
mo1 = endsWithNumber.search('Your number is forty two') == None
print(mo) ; print(mo1)
'''
<_sre.SRE_Match object at 0x6ffffe5b8b8>
True
'''

wholeStringIsNum = re.compile(r'\d+$')
mo = wholeStringIsNum.search('1234567890') 
mo1 = wholeStringIsNum.search('12345xyz67890') == None
mo2 = wholeStringIsNum.search('12  34567890') == None
print(mo) ; print (mo1) ; print(mo2)
'''
<_sre.SRE_Match object at 0x6ffffe5b920>
False
False
'''

print "\nExample 13 - Wilcards"
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.') 
print(mo)
'''
['cat', 'hat', 'sat', 'lat', 'mat']
'''

print "\nExample 14 - Match everything with a dot star"
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart') 
print(mo)
print(mo.group(1))
print(mo.group(2))

'''
<_sre.SRE_Match object at 0x6ffffe5c250>
Al
Sweigart
'''

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
'''
<To serve man>
'''

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
'''
<To serve man> for dinner.>
'''

print "\nExample 15 - Matching Newlines with the dot character"
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
print(mo)
'''
Serve the public trust.
'''

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.  \nUphold the law.').group()


'''
The  ? matches zero or one of the preceding group.
The  * matches zero or more of the preceding group.
The  + matches one or more of the preceding group.
The  {n} matches exactly n of the preceding group.
The  {n,} matches n or more of the preceding group.
The  {,m} matches 0 to m of the preceding group.
The  {n,m} matches at least n and at most m of the preceding group.
{n,m}? or  *? or  +? performs a nongreedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The  . matches any character, except newline characters.
\d ,  \w , and  \s match a digit, word, or space character, respectively.
\D ,  \W , and  \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isnt between the brackets.
'''
print "\nExample 16 - Case-Insensitive Matching"
robocop = re.compile(r'robocop', re.I)

print robocop.search('RoboCop is part man, part machine, all cop.').group()
'''RoboCop'''

print robocop.search('ROBOCOP protects the innocent').group()
'''ROBOCOP'''

print robocop.search('Al, why does your programming book talk about robocop so much?').group()
'''robocop'''

print "\nExample 17 - Substituting Strings with the sub() Method"
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo) 
'''
CENSORED gave the secret documents to CENSORED.
'''

namesRegex = re.compile(r'Agent (\w)\w*')
mo = namesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo)
'''
A**** told C**** that E**** knew B**** was a double agent.
'''

print "\nExample 18 - Managing Complex Regexes"
phoneRegex = re.compile(r'''(
  (\d{3}|\(\d{3}\))?  	#Area code
  (\s|-|\.)?			#Separator
  \d{3}					#first 3 digist
  (\s|-|\.)				#separator
  \d{4}					#last 4 digits
  (\s*(ext|x|ext.)\s*\d{2,5})? 	#extension
  )''', re.VERBOSE)
