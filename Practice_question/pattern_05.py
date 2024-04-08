rows = 10
val = 65
for i in range(1,rows+1):
    for j in range(i):
        print(chr(val),end=" ")
        val += 1
        if val >90:
            val = 65
    val -= 1
    print()        