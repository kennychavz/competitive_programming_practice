def lonelyinteger(a):

    # list where we keep the elements
    element_list = []

    # we loop through the elements
    for element in a:
        print(a)
        # if the element is already in a list we remove it
        if element in element_list:
            element_list.remove(element)
        
        # we add the element to a list
        else:
            element_list.append(element)

lonelyinteger([1,2,3,4,3,2,1])
