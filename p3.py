"""
ACCEPT THREE DIGITS AND PRINT ALL POSSIBLE COMBINATIONS FROM THE DIGITS
"""
a=int(input(" enter first number:"))
b=int(input(" enter second number:"))
c=int(input(" enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])

      
OUTPUT-
enter first number:1
enter second number:2
enter third number:3
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
