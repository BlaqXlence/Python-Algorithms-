from decimal import Decimal
def LinearSearch(lst):
     max_product = Decimal('-Infinity')
     max_i = -1
     max_j = -1

     for i in lst:
        for j in lst:
            if max_product < i * j and i is not j:
                max_product = i * j
                max_i = i
                max_j = j

     return max_i, max_j
 
lst = [1, 3, 5, 2, 6]


print(LinearSearch(lst))
