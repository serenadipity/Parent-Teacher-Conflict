import utils

a = {}
a[1] = ['tf1', 'tl2', [1, 'afternoon', 1, "pf1", "pl1"], [2, 'afternoon', 7, "pf2", "pl2"]]
a[2] = ['tf2', 'tl2', [3, 'afternoon', 3, "pf3", "pl3"], [4, 'afternoon', 15, "pf4", "pl4"]]
a[3] = ['tf3', 'tl3', [5, 'afternoon', 0, "pf5", "pl5"], [6, 'afternoon', 32, "pf6", "pl6"]]
a[4] = ['tf4', 'tf4', [5, 'afternoon', 6, "pf5", "pl5"], [6, 'afternoon', 41, "pf6", "pl6"]]

print utils.thingToDo(a,'date')
