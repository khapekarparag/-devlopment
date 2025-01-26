def lists(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    lists(list, idx+1)

fruits=["mango","banana","apple"]
lists(fruits)    