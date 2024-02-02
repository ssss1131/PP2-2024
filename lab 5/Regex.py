import re

# 1
lines = """ab     ababababab    aaaaaaaaaa abb
a_____   b_   C_
C_
a_aa
a_A
abb
abbb
AAIOSDKPOAKSDPOAaspdkassapdpoad AAs abab
applb  aaaasdasodiakb
abbbbbb
AppleBananaMacbookMAC"""
for line in lines.split('\n'):
    search = re.search("[ab*]", line)
    # print(search)

# 2
for line in lines.split('\n'):
    if re.search(r"(abb.?)|(abbb.?)",line):                # тут точка это любой символ после этого а вопросик типа вырубает его если символа вообще не будет после то он полибому примет так как вопросик вырубает точку он тип либо 0 либо 1 раз повтор делает в нашем случий точку
        pass
        # print(line)

# 3
for line in lines.split('\n'):
    if re.search(r"[a-z]_+.?", line):
        pass
        #print(line)


#4
for line in lines.split("\n"):
    if re.search(r"[A-Z][a-z]",line):
        pass
        #print(line)

#5
for line in lines.split("\n"):
    if re.search(r"[a].?[b]+\Z",line):
        print(line)
