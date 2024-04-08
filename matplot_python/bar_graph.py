import matplotlib.pyplot as plt

xpoints = ["Python","C++","C","JAVA"]
ypoints = [85,55,70,77]

# to define the axis name
plt.xlabel("Languages",fontsize = 15,fontcolor = "b")
plt.ylabel("Number",fontsize = 15,fontcolor = "m")
plt.title("Bar Graph",fontsize = 18)


# plt.bar(xpoints,ypoints,width = 0.4,color = ["y","b","m","g"],align = "center",edgecolor = "r",linewidth = 4,linestyle = ":",alpha = 0.4,label = "Popularity")
plt.bar(xpoints,ypoints,width = 0.4,color = ["y"],align = "center",edgecolor = "r",linewidth = 3,alpha = 0.6,label = "Popularity")
plt.legend()
plt.show()


#align = (edge , center)
#alpha = (0,1)