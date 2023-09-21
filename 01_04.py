
def count_uniques(list_of_strings):
    bookkeeping = {}
    #creates entries for all new words and adds +1 if it already exists.
    for word in list_of_strings:
        if word not in bookkeeping:
            bookkeeping[word] = 1
        else:
            bookkeeping[word] += 1
    return bookkeeping

test_list = ['Dog', 'Cat', 'Wolf', 'Dog', 'Mouse', "Dog", 'Wolf']
print(count_uniques(test_list))