import re
s='gh3r0v1o6mng70yc89z09vippim0e1yn2v7koghojgjed3wq2b10ul8i8l'
# print(re.findall("\d",s)) #find number
# print(re.findall("\d\d",s)) #find numbeที่ติดกัน
print(re.findall("\D", s))  # find str
