# function to iterate forwards in place
def remove_dups(list1, list2):
    i = 0
    while i < len(list1):
        if(list1[i] in list2):
            del(list1[i])
        else:
            i += 1

# uses built-in reversed function to iterate backwards through list
# in place
def remove_dups_reversed(list1, list2):
    for i in reversed(list1):
        if i in list2:
            list1.remove(i)



ls1 = [1, 2, 3, 4]
ls2 = [1, 2, 3, 6]

print(f"Before duplicate removal: {ls1}")
remove_dups_reversed(ls1, ls2)
print(f"After duplicate removal: {ls1}")