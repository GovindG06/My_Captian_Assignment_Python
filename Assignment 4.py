s  = list(input("please enter a string "))
so =[]   
for i in s:
    if i not in so:
      print(i,"=",s.count(i))
      so.append(i)
    else:
      continue
