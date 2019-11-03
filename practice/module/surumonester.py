"""递归打印嵌套list"""


def print_lol(aslist,level):
    for item in aslist:
        if isinstance(item, list):
            print_lol(item,level+1)
        else:
            for tab_stop in range(level):
                print("\t",end=" ")
            print(item)
