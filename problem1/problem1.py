def threeOrFive(x): return x%3 == 0 or x%5 == 0
fullList = range(0,1000)
filteredList = filter(threeOrFive, fullList)
print(filteredList)
summedFiltered = sum(filteredList)
print(summedFiltered)
