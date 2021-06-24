
Q.no.2
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a = 20; a+= 30; a%=3;
print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print( True is False)
print("False" in "False")
print(((True == False) or (False > True)) and (False <= True))



Q.no.3
s1 = "Nice to have it"
s2 = "here"
s3 = s1+' '+s2
print(s3)



Q.no.4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])



Q.no.5
s1='Nice to have it'
s2='here'
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a.insert(0,s1)
a.append(s2)
print(a)


Q.no.6
color_list_1 = set(["White", "Black", "Purple"]) 
color_list_2 = set([ "Green","purple"])
print(color_list_1 - color_list_2)


Q.no.9
s=['without','hello','bag','world']
s.sort()
print(s)


Q.no.10:
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 
'Marks': [57,87,67,79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])


