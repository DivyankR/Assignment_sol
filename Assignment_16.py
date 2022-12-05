# Question 1:

years_list = []
for i in range(1999,2005):
    years_list.append(i)
print(years_list)
yob = years_list[0]

# Question 2:

for i in years_list:
    if i-yob == 3:
        print(i)


# Question 3:

print(max(years_list))

# Question 4:

things = ['mozzarella','cinderella','salmonella']

# Question 5:

print(things[1].capitalize())

print(things)

# as we can see, it didn't change the element in the list

# Question 6:

surprise_list = ["Groucho","Chico","Harpo"]

# Question 7:

s = surprise_list[len(surprise_list)-1].lower()
s = s[::-1]
print(s.capitalize())


# Question 8:

e2f = {'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f)


# Question 9:

print(e2f['walrus'])


# Question 10:

f2e = {}
for i,j in e2f.items():
    f2e[j] = i

print(f2e)


# Question 11:

print(f2e['chien'])


# Question 12:

s = set(e2f.keys())
print(s)


# Question 13:

life = {"animals": {"cats": ["Henri", "Grumpy", "Lucy"], "octopi": {}, "emus": {}}, "plants": {}, "others": {}}


# Question 14:

print(list(life.keys()))


# Question 15:

print(list(life["animals"].keys()))


# Question 16:

print(life["animals"]["cats"])


