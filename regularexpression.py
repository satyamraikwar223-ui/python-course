import re

pattern = "gamer"
#pattern = r"[A-Z]ammer"
 
text = ''' hlw hi namaste 
khelega free fire 
banega Gamer 
karega pannel us eon live streem 
lagega tujhpe Jammer
banega agar tu Hammer
before GTA6
  '''
match = re.search(pattern , text)
print(match)
#matches = re.finditer(pattern, text)
#for match in matches:
 #print(match)
 
 #print(match.span())
 #0utput = (98, 104)
#          (120, 126)
 #print(text[match.span()[0]:match.span()[1]])
 #output = Jammer
#          Hammer

#metacharactors in regular expressions
#pattern = r"[A-Z]ammer"
#output = <re.Match object; span=(98, 104), match='Jammer'>

#if 
#matches = re.findter(pattern, text)
#for match in matches:
# print(match)
#OUTPUT = <re.Match object; span=(98, 104), match='Jammer'>
#         <re.Match object; span=(120, 126), match='Hammer'