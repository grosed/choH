import scipy
from math import log

def choH(data) :
    test = lambda i : log(scipy.stats.kstest(data[-i:],data[:-i]).pvalue)
    return [float(x) for x in list(map(test,range(1,len(data))))]