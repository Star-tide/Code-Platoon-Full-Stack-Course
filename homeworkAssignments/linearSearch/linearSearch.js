function search(searchTerm, arr) {
    indexList = []
    for(i = 0; i < arr.length; i++){
        if (searchTerm.toLowerCase() === arr[i].toLowerCase()) {
            indexList.push(i)
        }
    }
    return indexList
}

console.log(search('A', 'Banana'))