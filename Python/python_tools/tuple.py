# mytuple = ("uday","ram","kamal")
# print(mytuple,type(mytuple))
# print(len(mytuple))


# tuple1 = (1,2,3,4,5,6,7)
# tuple2 = (4,5,5,6,7,8)
# print(tuple1,tuple2)

# tuple1 = (1,2,3,4,5,6,7)
# tuple2 = (4,5,5,6,7,8)
# x=tuple1+tuple2
# print(x)

# mytuple_1 = ("hello","world")
# tuple_2 = mytuple_1*2
# print(tuple_2)

# mytuple_1 = ("hello  ")
# mytuple_2 = ("world")
# tuple_3 = mytuple_1+mytuple_2
# print(tuple_3)


# s = ("s1","s2","s3","s4","s5")
# for i in s:
#     print(i,end=" ")


# s = ("s1","s2","s3","s4","s5")
# for i in range(len(s)):
#     print(s[i],end=" ")

# s = ("s1","s2","s3","s4","s5")
# i = 0
# while(i<len(s)):
#     print(s[i] ,end=" ")
#     i +=1

# s = ("s1","s2","s3","s4","s5","s6","s7")
# print(s[:0])
# print(s[-62:])
# print(s[:5])
# print(s[1:1])
# print(s[-4:-1])

# s = ("s4","s2","s3","s4","s5","s5","s7","s8","s5")
# # print(s.count("s5"))
# # print(s.count("s4"))
# # print(s.count("s1"))
# # print(s.count("s2"))
# print(s.index("s2"))
# print(s.index("s4"))
# print(s.index("s3"))


# s = ("s4","s2","s3","s4","i")
# b = list(s)
# b[3] = "x"
# z = tuple(b)
# print(z)

# s = ("s4","s2","s3","s4","i")
# b = list(s)
# b.append("x")
# z = tuple(b)
# print(z)

# s = ("s4","s2","s3","s4","i")
# b = list(s)
# x = ["2","3","4"]
# b.extend(x)
# z = tuple(b)
# print(z)

# students = ("s1","s2","s3")
# one, two,d = students
# print(one)
# print(two)
# print(d)


# students = ("s1","s2","s3","s3","s4","s5","s6")
# one,two, *three = students
# print(one)
# print(two)
# print(three)


# words = ['hello','world','how','are','you']
# joined_text =  "".join(words)
# print(joined_text) # Output: 'hello,world'


t1 = (1 , 2)
t2 = (1 , 2 , 8)
print(id(t1))
print(id(t2))