def main():
    fil = open("uday.txt","w")
    for x in range(1,51):
        fil.write(str(x )+ "\n")          # fil.write("\n")
        
    fil.close()
main()
        