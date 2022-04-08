from statistics import mean
import numpy as np
import termtables as tt
import scipy.stats as sps
import math
from itertools import combinations  
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

def summation(data: np.array):
    sum = 0
    for i in range(len(data)):
        arr = data[i]
        for j in range(len(arr)):
            sum += data[i][j] 
    return sum

def sum_x_js(data: np.array):
    tot_sum = 0
    for i in range(len(data)):
        part_sum = sum(data[i])
        tot_sum += (part_sum**2)/len(data[i])
    return tot_sum    
        

def size(data: np.array):
    size = 0
    for i in range(len(data)):
        arr = data[i]
        for j in range(len(arr)):
            size += 1 
    return size  

def sum_of_squares(data: np.array):
    sum = 0
    for i in range(len(data)):
        arr = data[i]
        for j in range(len(arr)):
            sum += data[i][j]**2  
    return sum

def SST(data: np.array):
    return sum_of_squares(data) - ((1/size(data))*(summation(data)**2))

def SSTr(data: np.array):
    return sum_x_js(data) - ((1/size(data))*(summation(data)**2))

def SSE(data: np.array):
    return SST(data)-SSTr(data)

def MSTr(data: np.array):
    return SSTr(data)/(len(data)-1)

def MSE(data: np.array):
    return SSE(data)/(size(data)-len(data))

def f(data: np.array):
    return MSTr(data)/MSE(data)

def get_table(data):
    I = len(data)
    J = len(data[0])
    v1 = I - 1
    v2 = I*(J-1)
    _SSTR = round(SSTr(data),2)
    _SSE = round(SSE(data),2)
    _SST = round(SST(data),2)
    _MSTR = round(MSTr(data),2)
    _MSE = round(MSE(data),2)
    _f = round(f(data),2) 
    
    table = tt.to_string(
    [["Treatements", v1, _SSTR, _MSTR, _f], ["Error", v2, _SSE, _MSE, "X"], ["Total", v1+v2, _SST, "X", "X"]],
    header=["Source of Variation", "Degrees of Freedom", "Sum of Squares", "Mean Square", "f"],
    style=tt.styles.ascii_thin_double)
    return(table) 

def hyp_test(data, alpha):
    I = len(data)
    J = len(data[0])
    v1 = I - 1
    v2 = I*(J-1)
    _f = round(f(data),2)
    _fcrit = sps.f.ppf(q=1-alpha, dfn=v1, dfd=v2).round(2);
    if _f > _fcrit:
        print(_f, " > ", _fcrit, "which means p < a so we reject H0")
    else:
        print(_f, " < ", _fcrit, "which means p > a so we fail to reject H0")
        
def getMeans(data: np.array):
    means = []
    for i in range(len(data)):
        arr = data[i]
        sum = 0
        for j in range(len(arr)):
            sum += data[i][j]
        means.append(round(sum/len(data[i]),2))
    return means 
    
def get_w_vals(data, alpha):
    print("Enter Q from table A.10 with v =",size(data)-len(data), " m =",len(data)," a =",alpha)
    Q = input("Q: ")
    idx = list(range(len(data)))
    pairs = list(combinations(idx, 2))
    _MSE = MSE(data)
    for pair in pairs:
        i = pair[0]
        j = pair[1]
        Ji = len(data[i])
        Jj = len(data[j])
        sqt = math.sqrt(((_MSE/2)*((1/Ji)+(1/Jj))))
        W = round(float(Q) * float(sqt),2)
        print("W",i+1,",",j+1,": ",W)
        means = getMeans(data)
        diff = round(means[i]-means[j], 2)
        if (diff > W):
            print("Significant difference between ",i+1, " and ",j+1)

def main():
    data = np.array([[59.5, 53.3, 56.8, 63.1, 58.7],
                     [55.2, 59.1, 52.8, 54.5],
                     [51.7, 48.8, 53.9, 49.0],
                     [44.6, 48.5, 41.0, 47.3, 46.1]])

    alpha = .05
    
    print(get_table(data))
    hyp_test(data, alpha)
    get_w_vals(data, alpha)

if __name__ == "__main__":
    main()
    