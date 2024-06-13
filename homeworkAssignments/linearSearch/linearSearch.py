def search(search_term, arr):
    index_group = []
    for index, item in enumerate(arr):
        if item.lower() == search_term.lower():
            index_group.append(index)

    return index_group

print(search('a', 'banana'))