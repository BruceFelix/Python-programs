#1 
empty_list = []

#2
shoes_list = ['Jordan','Timberland', "clarks", 'Gucci','Loafers']

#3
print(len(shoes_list))

#4
print(shoes_list[0],shoes_list[2], shoes_list[-1])

#5
mixed_data_types = ['Bruce', "22", '177cm', 'single', '588-1']

#6
it_companies = ['Facebook', 'Google', 'Microsoft','Apple', "IBM","Oracle", "Amazon"]

#7
print(it_companies)

#8
print("The number of IT companies: ",len(it_companies))

#9
print(it_companies[0],it_companies[3],it_companies[-1])

#10
it_companies[0] = "Huawei"
print(it_companies)

#11
it_companies.append("Facebook")
print(it_companies)

#12
it_companies.insert(4, "Pixer")
print(it_companies)

#13
it_companies[1] = it_companies[1].upper()
print(it_companies)

#14
print(("#").join(it_companies))

#15
print("Facebook" in it_companies)

#16 
it_companies.sort()
print(it_companies)

#17

it_companies.reverse()
print(it_companies)

#18
print(it_companies[0:3])

#19 
print(it_companies[-3:])