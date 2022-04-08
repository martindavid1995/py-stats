from statistics import mean
import numpy as np
import termtables as tt
import scipy.stats as sps
import math
from itertools import combinations  
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

def main():
    # Variable length group data works, data can be a ragged array
    data = np.array([[67,50,70,60,55],
                     [49,32,65,39,43],
                     [40,39,41,60,45],
                     [75,70,70,75,70],
                     [28,33,34,30,29],
                     [28,35,34,29,33]])
    alpha = .05
       
    print(get_table(data))
    hyp_test(data, alpha)
    get_w_vals(data, alpha)
    
def is_ragged(data):
    l = len(data[0])
    for i in range(len(data)):
        if len(data[i]) != l:
            return True
    return False

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
    _MSE = MSE(data)
    if (is_ragged(data) == True):
        idx = list(range(len(data)))
        pairs = list(combinations(idx, 2))
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
    else:
        W = round(float(Q)*math.sqrt((_MSE/len(data[0]))),2)
        print(W)
        idx = list(range(len(data)))
        pairs = list(combinations(idx, 2))
        for pair in pairs:
            i = pair[0]
            j = pair[1]
            mi = sum(data[i])/len(data[0])
            mj = sum(data[j])/len(data[0])
            diff = mi - mj
            if (diff > W):
                print("Significant difference between ",i+1, " and ",j+1)
            

if __name__ == "__main__":
    main()
    