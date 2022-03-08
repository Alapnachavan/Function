# write a phython of recursion list sum.go to the editor 
# test data : [1,2,[3,4],[5,6]]
# expected result :21


def recursion_list_sum(data_list):
    total=0
    for element in data_list:
        if type(element)==type([]):
            total=total+recursion_list_sum(element)
        else:
            total=total+element 
    return total 
print(recursion_list_sum([1,2,[3,4],[5,6]]))
