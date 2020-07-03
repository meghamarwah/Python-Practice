
#Q:1) Given the string 'hello' give an index command that returns 'e'. # Print out 'e' using indexing
s = 'hello world!'
print("Indexing:",s[1])

#Q:2) Reverse the string 'hello' using slicing, reverse,len and without in built function.

print('Reverse String using slicing-',s[::-1])

print('Reverse String using reverse-',''.join(reversed(s)))

total_len = len(s)
revstr = ''
while (total_len>0):
    revstr += s[total_len-1]
    total_len = total_len-1
print('Reverse string using len-',revstr)  #note--> len() always starts from 1 but Indexing and slicing starts from 0

j=''
for i in s:
    j=i+(j)
print('Reverse String without using inbuilt method-',j)

#Q:3) Given the string hello, give two methods of producing the letter 'o' using indexing.
#Method1
print("Method1-",s[4])
#Method2
print("Method2-",s[-5])

#------------------------------------------------------------LIST-----------------------------------------------------



#Q.1)Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

#Q.2)Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

#------------------------------------------------------------Dictionaries---------------------------------------------



#Q.1)Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print('dict easy-',d['simple_key']) 
print('dict using keys-',d.values())

d = {'k1':{'k2':'hello'}}
print('dict moderate-',d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print('dict difficult-',d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print('dict annoying-',d['k1'][2]['k2'][1]['tough'][2][0])

d = {'k1':1, 'k2':2, 'k3':3}
for i in d:
    print(i)
for i,j in d.items():
    print(i,j)


#-------------------------------------------------------------Set---------------------------------------------------------


#Q.1)Use a set to find the unique values of the list below:

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))















