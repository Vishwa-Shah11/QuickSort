
def most_freq(L):
    return max(set(L), key = L.count)
    
def remove_items(L, value):
    v = L.count(value)
    for i in range(v):
        L.remove(value)
    return L

def DishPrepareOrder(order_list):
    preparation_order = []
    while order_list:
        order_id = most_freq(order_list)
        preparation_order.append(order_id)
        order_list = remove_items(order_list, order_id)
        #print(order_list)
        #print(preparation_order)
 
    return preparation_order

nums = [1006, 1008, 1009, 1008, 1007, 1005, 1008, 1001, 1003, 1009, 1006, 1003, 1004, 1002, 1008, 1005, 1004, 1007, 1006, 1002, 1002, 1001, 1004, 1001, 1003, 1007, 1007, 1005, 1004, 1002]

#nums = eval(input())
#print(most_freq(nums))
print(DishPrepareOrder(nums))

def DishPrepareOrder(order_list):
    st=sorted(set(order_list))
    dc={}
    for i in st:
        dc.update({i:order_list.count(i)})
    dc=dict(sorted(dc.items(), key=lambda item: item[1],reverse=True))
    ls=[]
    for i in dc.keys():
        ls.append(i)
    #print(ls)
    return ls