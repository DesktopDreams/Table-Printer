tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    """ Below is an algorithm to find the highest interger in each sublist of tableData.
         For example, highest interger from tableData[0] is 8, from 'cherries'.
    """ 
    colWidths = [0] * len(tableData)
    for b in range(len(tableData)):
               colWidths[b] = [len(i) for i in tableData[b][0:]]
               max_num = 0
               for c in colWidths[b]:
                   if c > max_num:
                       max_num = c
                       colWidths[b] = max_num
    """ Below is the code to sort the table in its intended output. """
    k = 0
    v = 0 # Setting v = 0 allows us to iterate over tableData[k] while getting the same position in each sublist.
    while True:
        try:
            for k in range(len(tableData)):
                print(str(tableData[k][v].rjust(colWidths[k])), end=' ')
            print('')
        except Exception:
            pass
        if k == 2: #Once we done iterating, we will reset it by increasing the value of v by 1, and continuing the loop,
            v = v + 1
            continue
printTable()
