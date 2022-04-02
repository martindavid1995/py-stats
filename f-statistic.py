import numpy as np
import termtables as tt
import scipy.stats as sps

def sum_of_squares(data):
    sum = 0
    for val in data:
        sum += val**2
    return sum

def SST(data: np.array):
    I = len(data)
    J = len(data[0])
    data = data.flatten()
    return sum_of_squares(data)-(1/(I*J))*(sum(data)**2)

def SSTr(data: np.array):
    I = len(data)
    J = len(data[0])
    return ((1/J)*sum_of_squares(sum_rows(data)))-(1/(I*J))*(sum(data.flatten())**2)

def SSE(data: np.array):
    return SST(data)-SSTr(data)

def MSTr(data: np.array):
    I = len(data)
    return SSTr(data)/(I-1)

def MSE(data: np.array):
    I = len(data)
    J = len(data[0])
    return SSE(data)/(I*(J-1))

def f(data: np.array):
    return MSTr(data)/MSE(data)

def sum_rows(data: np.array):
    sums = []
    for i in range(len(data)):
        p_sum = 0
        for j in range(len(data[0])):
            p_sum += data[i][j]
        sums.append(p_sum)
    return sums

def get_table(data):
    I = len(data)
    J = len(data[0])
    v1 = I - 1
    v2 = I*(J-1)
    _SSTR = SSTr(data).round(2)
    _SSE = SSE(data).round(2)
    _SST = SST(data).round(2)
    _MSTR = MSTr(data).round(2)
    _MSE = MSE(data).round(2)
    _f = f(data).round(2)
    
    
    table = tt.to_string(
    [["Treatements", v1, _SSTR, _MSTR, _f], ["Error", v2, _SSE, _MSE, "X"], ["Total", v1+v2, _SST, "X", "X"]],
    header=["Source of Variation", "Degrees of Freedom", "Sum of Squares", "Mean Square", "f"],
    style=tt.styles.ascii_thin_double)
    return(table) 

def hypTest(data, alpha):
    I = len(data)
    J = len(data[0])
    v1 = I - 1
    v2 = I*(J-1)
    _f = f(data).round(2)
    _fcrit = sps.f.ppf(q=1-alpha, dfn=v1, dfd=v2).round(2);
    if _f > _fcrit:
        print(_f, " > ", _fcrit, "which means p < a so we reject H0")
    else:
        print(_f, " < ", _fcrit, "which means p > a so we fail to reject H0")
    
def main():
    data = np.array([[67,50,70,60,55],
                     [49,32,65,39,43],
                     [40,39,41,60,45],
                     [75,70,70,75,70],
                     [28,33,34,30,29],
                     [28,35,34,29,33]])
    
    alpha = .05
    print(get_table(data))
    hypTest(data, alpha)

if __name__ == "__main__":
    main()
    
    