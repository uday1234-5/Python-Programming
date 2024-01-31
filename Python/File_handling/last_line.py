fil = open("sample.txt","r")
for i in fil:
    out = next(fil)
print(out)
