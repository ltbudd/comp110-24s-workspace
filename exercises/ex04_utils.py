"""List Utility Functions."""

__author__ = "730648814"

# Defining all function
def all(list: list[int], num: int) -> bool:
    if len(list) > 0:
        for i in range(len(list)):
            if list[i-1] != num:
               return False
               break
        return True  
    else:
        return False

# Defining max function
def max(nlist: list[int]) -> int:
    if len(nlist) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        big: int = nlist[0]
        for i in range(len(nlist)):
            print(i)
            if nlist[i-1] > big:
                big = nlist[i-1]
        return big
    
# Defining is_equal function
def is_equal(a_list: list[int], b_list: list[int]) -> bool:
    if len(a_list) != len(b_list):
        return False
    else:
        for i in range(len(a_list)):
            if a_list[i-1] != b_list[i-1]:
                return False
        return True
    

# Defining extend function
def extend(a_list: list[int], b_list: list[int]) -> None:
    for i in range(len(b_list)):
        a_list.append(b_list[i-1])

