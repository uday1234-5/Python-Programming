# # def fun():
# #     try:
# #         print("Hello")
# #         return 0
# #     finally:
# #         print("DONE")
# # fun()
# # print("Hi")



# def fun():
#     for i in range(5):
#         try:
#             if i==2:
#                 print("Hello")
#             break
#         finally:
#             print("DONE")
# fun()
# print("Hi")


def fun():
    for i in range(5):
        try:
            if i==5:    
                print("Hello")
            continue
        finally:
            print("DONE")
fun()
print("Hi")