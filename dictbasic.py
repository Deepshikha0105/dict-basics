data = {'Fruit': ['Apple', 'Banana', 'Orange'], 'Subject': ['Phy', 'Math', 'English']}
#Add new dictionary in data.
data2 = {'Juice': ['Guava', 'Banana', 'Orange'], 'Coach': ['Phy', 'Biology', 'English']}
data3= data.copy()
for key, value in data2.items():
    data3[key]=value

print(data3)


#Add ‘Biology’ in ‘Subject’
data3["Subject"]=['Phy', 'Math', 'English', "biology"]
print(data3)

#Create new key in  ‘Animal’ with value  [’dog’,’cat’]
data3["animal"]= ["dog", "cat"]
print(data3)
