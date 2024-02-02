import re

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
AppleBananaMacbookMAC
a...........,,,,,asdawdas,,./   asdaw,"""
# 6
for line in lines.split('\n'):
    a = line
    a = re.sub(r"[\s.,]", "/", a)
    # print(a)

# 7
a_7 = "sau_sss_aa_aaa_a"


def ans(matc):
    return matc.group(1) + matc.group(2).upper()


s_7 = re.sub("(\w)_([\w])", ans, a_7)
# print(s_7)


# 8
a_8 = "SauSauMondayTuesdayOnePiece"

s_8 = re.findall("[A-Z][^A-Z]*", a_8)
# print(" ".join(s_8))

# 10
a_10 = "SssAhahSuudaGoodOne"


def ans_10(matc):
    return matc.group(1) + "_" + matc.group(2).lower()


s_10 = re.sub("(\w)([A-Z])", ans_10, a_10)
print(s_10)
