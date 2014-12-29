def median(lst):
    sort_lst = sorted(lst)
    lst_len = len(lst)
    if lst_len % 2 == 0:
        mdn = (sort_lst[(lst_len-1)/2] + sort_lst[(lst_len)/2])/2.0
    else:
        mdn = sort_lst[(lst_len - 1)/2]
    return mdn
"""
Write a function called median that takes a list as an input and returns the median value of the list.

For example: median([1,1,2]) should return 1.

    The list can be of any size and the numbers are not guaranteed to be in any particular order.
    If the list contains an even number of elements, your function should return the average of the middle two.
"""