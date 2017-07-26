s = input("please enter the string")
n = int(input("please enter the roation key"))
l = []
for i in range(0,len(s)):
    if s[i].isalpha():
        if s[i].islower():
            o = ord(s[i])%97
            c = (o+n)%26
            l.append(chr(97+c))
        else:
            O = ord(s[i])%65
            C = (O+n)%26
            l.append(chr(65+C))
    else:
        l.append(s[i])
for i in l:
    print(i,end='')
