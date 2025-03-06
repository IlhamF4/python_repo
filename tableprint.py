tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]	
             
def printTable(list):
	colwidth = [0] * len(list)
	for i in range(len(list)):
		colwidth[i] = max(len(word) for word in list[i])
		
	for i in range(len(list[0])):
		for j in range(len(list)):
			print(list[j][i].rjust(colwidth[j]),end=" ")
		print()
printTable(tableData)