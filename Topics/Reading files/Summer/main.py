#  write your code here 

file = open('data/dataset/input.txt')
count = 0
for line in file:
    if line == 'summer\n':
        count += 1
print(count)
