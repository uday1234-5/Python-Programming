fil = open("sample.txt","r")
out = len(fil.read().split())
print(out)
fil.close()