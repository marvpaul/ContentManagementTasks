fruits = {
    'apple': 1.99,
    'orange': 2.99,
    'banana': 2.49,
    'grape': 3.99
}
print(fruits['apple'])

fruits_list = [(k, fruits[k]) for k in fruits]
print(fruits_list[0][0])

fruits_sorted_by_price = sorted(fruits_list, key = lambda k:k[1], reverse=True); 
print(fruits_sorted_by_price)