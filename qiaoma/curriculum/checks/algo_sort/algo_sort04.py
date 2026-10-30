assert binary_search([1, 3, 5, 7, 9], 9) == 4, "别漏掉最后一个元素"
assert binary_search([1, 3, 5, 7, 9], 1) == 0
assert binary_search([1, 3, 5], 4) == -1
assert binary_search([], 1) == -1
