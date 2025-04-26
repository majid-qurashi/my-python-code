#majid qurashi 220365
my_list=[220365 , "Majid Qurashi" , "CSE", "5th Sem", 2022]
print(my_list)
print (len(my_list))
print (my_list[3])
#Append
my_list.append("kupwara")
print(my_list)
#copy
my_list2 = my_list.copy()
print(my_list2)
#Extend
my_list3=[1,2,3,4]
my_list4=[5,6,7,8]
my_list3.extend(my_list4)
print(my_list3)
#delete
my_list5 =[1,2,3,4,5]
del my_list5 [3]
print(my_list5)
#remove
my_list6=[3,4,5,6,7]
my_list6.remove(6)
print(my_list6)
#reverse
my_list7= [1,2,3,4,5]
my_list7.reverse()
print(my_list7)
#pop
my_list8 =[1,2,3,4,5]
my_list8.pop()
print(my_list8)
#clear
my_list9 = [1,2,3,4,5]
my_list9.clear()
print(my_list9)
#sort
my_list10 = [3,4,2,6,1,5]
my_list10.sort()
print(my_list10)