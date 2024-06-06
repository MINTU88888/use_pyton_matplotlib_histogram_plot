import matplotlib.pyplot as plt
import numpy as np
import random
x = np.random.randint(10,60,(50))
print(x)
no = [48,49,28,26,23,43,30,59,50,43,30,28,21,58,23,32,15,48,33,53,28,59,51,55,
46,26,30,13,25,34,53,12,41,49,54,42,57,54,12,37,32,36,55,48,36,36,31,54,29,45]
# bins perameter x axis pe jo value define hai unko set kr deta hai 
# edgecolor perameter graph mai jo boundary line hai usko color kr deta hai
# cumulative perameter graph ko reverce kr deta hai,or cumulative perameter mai humesa -1 ki value he jati hai
# aligh perameter ye betata hai ki x axis ki value ko graph ke mid mai , left mai , right mai ,center mai
# rwidth = "0 se 1" perameter graph mai vo value hai unki width ko kam krti hai
# orientation  = "" ye perameter ye betata hai kio graph ko verticle krna hai ya horizontel 
l = [10,20,30,40,50,60]
plt.xlabel("x axis",fontsize = 30)
plt.ylabel("y axis",fontsize = 30)
plt.hist(no,label="company ",edgecolor = "r",bins=l,cumulative=-1,align="mid")
plt.legend()
plt.title("histogram graph",fontsize = 30)
print(plt.show())