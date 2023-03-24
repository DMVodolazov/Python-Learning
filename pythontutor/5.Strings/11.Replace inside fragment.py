s = input()
a = s[:s.find('h')+1]
b = s[s.find('h')+1:s.rfind('h')]
c = s[s.rfind('h'):]
d = b.replace('h','H')
s = a + d + c
print(s)