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
# bst = BSTNode("a")

# for name in names_1:  # O(n)
#     # ipdb.set_trace()
#     bst.insert(name)  # O(nlogn)
# # This runs in the worst case of O(nlogn)

# for name in names_2:  # O(n)
#     if bst.contains(name):  # O(nlogn)
#         duplicates.append(name)  # O(1)
# This also runs in the worst case of O(nlogn)
# --------------------------------------------------
# 2O(nlogn) reduces to O(nlogn)


## Stretch ##

# Using sorting and index comparison to find repeated values in the sorted list
# time complexity: O(n log n)
# runtime: 0.011981964111328125 seconds
names = names_1 + names_2  # O(2n)
names.sort()  # O(nlogn)
counter = 1  # O(1)
repeat = ""  # O(1)
for idx in range(len(names)):  # O(n + k)
    ipdb.set_trace()
    current_name = names[idx]  # O(1)
    if idx > 0:  # O(1)
        if names[idx - 1] == names[idx]:  # O(1)
            counter += 1  # O(1)
            repeat = current_name  # O(1)
            if counter >= 2:  # O(1) and prevents multiple duplicates of same name
                duplicates.append(names[idx])  # O(1)
        else:
            # Reset counter, both at O(1)
            counter = 1
            repeat = ""

# # uncomment if there can be more than 2 of each name in the combined list
# duplicates = set(duplicates)  # Adds another O(n) pass
# duplicates = list(duplicates)  # Adds another O(n) pass
# ------------------------------------------------------------------------
# For the data as is, the above is O(nlogn) + O(2n) * (3 * O(1)) = O(nlogn)
# For the data with more duplicates, O(logn)


## End Stretch ##

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
