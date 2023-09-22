def linear_search_product(products, target):
    indices = []
    
    for i in range(len(products)):
        if products[i] == target:
            indices.append(i)
    
    return indices
products = ["apple", "banana", "apple", "grapes", "apple"]
target = "apple"
print(linear_search_product(products, target))

