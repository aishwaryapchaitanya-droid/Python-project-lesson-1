test_dict = {'codingal': 2, 'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 1, 'Interesting': 1}

print("The original dictionary : " +str(test_dict))

k = 1

res = 0 
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

print("Frequency of K is : " + str(res))