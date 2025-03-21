from pyeda.inter import expr ,truthtable
import numpy as np
import matplotlib.pyplot as plt

def build_kmap(expression):
    parsed_expr=expr(expression)
    tt=truthtable(parsed_expr.vars,parsed_expr)
    num_vars=len(parsed_expr.vars,parsed_expr)
    if num_vars not in [2,3,4]:
        raise ValueError("this implementation supports only 2,3,4 variabls")
    if num_vars==2:
        kmap=np.zeros((2,2),dtype=int)
        for minterm in tt:
            if minterm[1]:
                kmap[minterm[0][0],minterm[0][1]]=1
    elif num_vars==3:
        kmap=np.zeros((2,4),dtype=int)
        for minterm in tt:
            if minterm[1]:
                kmap[minterm[0][0],minterm[0][1]]=1
    elif num_vars==4:
        kmap=np.zeros((4,4),dtype=int)
        for minterm in tt:
            if minterm[1]:
                kmap[minterm[0][0],minterm[0][1]]=1
    return kmap
