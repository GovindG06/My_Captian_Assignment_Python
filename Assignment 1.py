# write a program which accepts the radius of a circle from the user and computes area 
r = int(input("Input the radius of the circle : "))
area = r*r
print('The area of the circle with radius', r,'is:',area)





#write a python program to accept a filename from the user and print the extension of that
a=input()
n = len(a)
if a[n-2:n]=="py":
  print("python")
else:
  print("invalid")  
