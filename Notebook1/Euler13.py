f = open('p013_numbers.txt', 'r')

lines = f.readlines()

numbers = [int(x) for x in lines]

print(sum(numbers))






