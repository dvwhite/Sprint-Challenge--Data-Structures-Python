import time
import ipdb
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# The naive approach that the sprint had originally
# time complexity: O(n^2) + O(1) = O(n^2)
# runtime: 6.548135757446289 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# A more efficient approach using binary search trees
# Add all names in names_1 to a binary search tree
bst = BSTNode("a")

for name in names_1:  # O(n)
    # ipdb.set_trace()
    bst.insert(name)  # O(nlogn)
# This runs in the worst case of O(nlogn)

for name in names_2:  # O(n)
    if bst.contains(name):  # O(nlogn)
        duplicates.append(name)  # O(1)
# This also runs in the worst case of O(nlogn)
# --------------------------------------------------
# 2O(nlogn) reduces to O(nlogn)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
