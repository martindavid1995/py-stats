import utilities.summaryStatistics as ss
import scipy.stats as sp
import math

alpha = .05
two_tailed = True

def main():
    x = [67,37,70,40,35,65,40,35,30,40]
    y = [75,85,60,90,80,75,70,90,95,80]
    
    if (len(x) != len(y)):
        raise Exception("Length of x and y are not equal")
    
    hyp_test(x,y)
    
def r_coef(x,y):
    return ss.Sxy(x,y)/((math.sqrt(ss.Sxx(x))*math.sqrt(ss.Sxx(y))))

def hyp_test(x,y):
    R = r_coef(x,y)
    print("r-coefficient: ",round(R,4))
    n = len(x)
    t = (R*math.sqrt(n-2))/(math.sqrt(1-(R**2)))
    print("t-score: ",round(t,2))
    p = sp.t.sf(abs(t), df=n-2)
    if two_tailed:
        p *= 2
    print("p-value: ",round(p,4))
    if (p < alpha):
        print("p < a so reject H0")
    else:
        print("p > a so fail to reject H0")
    

if __name__ == "__main__":
    main()