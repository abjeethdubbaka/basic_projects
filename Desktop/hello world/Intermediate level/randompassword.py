import random
def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)
upppercaseLetter1=chr(random.randint(65,90))
upppercaseLetter2=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
punctuationsighn1 = chr(random.randint(32,64))
punctuationsighn2= chr(random.randint(32,64))
password = upppercaseLetter1 + upppercaseLetter2 + lowercaseLetter1 \
           +lowercaseLetter2 + digit1 + digit2 + punctuationsighn1 + punctuationsighn2
password = shuffle(password)
print(password)