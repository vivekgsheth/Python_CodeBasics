# Exercise 1
arr= [2200,2350,2600,2130,2190]

print(arr[1] - arr[0])

sum1=0
for i in range(0,3):
    sum1+=arr[i]
print(sum1)

for i in range(len(arr)):
    if arr[i] == 2000:
        print(i, '')

arr.append(1980)

arr[3] = arr[3]-200

print(arr)

# Exercise 2

heros = ['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append('Black Panther')
print(heros)

heros.remove('Black Panther')
heros.insert(3,'Black panther')
print(heros)

# Important : Replace hulk & thor with doctor strange
heros[1:3] = ['doctor strange']

heros.sort()
print(heros)

# Exercise 3
maxm = int(input())
l = []
for i in range(1,maxm):
    if i%2 != 0:
        l.append(i)
print(l)

