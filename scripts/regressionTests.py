import utilities.summaryStatistics as ss
import math
import scipy.stats as sp

two_tailed = True
alpha = .05

def main():
    x = [67,37,70,40,35,65,40,35,30,40]
    y = [75,85,60,90,80,75,70,90,95,80]

    if (len(x) != len(y)):
        raise Exception("Length of x and y are not equal")
    
    # get_std_dev(x,y)
    # get_r_2(x,y)
    # get_CI(x,y)
    # hyp_test(x,y)
    

def get_r_2(x,y):
    dec = 1 - (ss.SSE(x,y)/ss.Sxx(y))
    dec = round(dec,4)
    print("r-squared: ",dec)

def get_std_dev(x,y):
    print("Standard Deviation: ",round(math.sqrt(ss.variance(x,y)/ss.Sxx(x)),4))
    
def get_CI(x,y):
    df = len(x)-2
    S = math.sqrt(ss.SSE(x,y)/(df))
    a = alpha/2
    
    if (two_tailed):
        a_ = alpha/2
    else:
        a_ = alpha
    
    t = abs(sp.t.ppf(q=a_,df=len(x)-1))
    
    B1 = ss.b1(x,y)
    Sxx = ss.Sxx(x)
    print(S)
    range = t * (S/(math.sqrt(Sxx)))
    low = round(B1 - range,6)
    high = round(B1 + range,6)
    print("Standard Deviaton: ",round(S,4))
    print("(",low,",",high,")")
    
def hyp_test(x,y):
    B1 = ss.b1(x,y)
    df = len(x)-2
    S = math.sqrt(ss.SSE(x,y)/(df))
    Sxx = ss.Sxx(x)  
    B10 = float(input("Enter B1 nought: "))
    t = (B1-B10)/(S/math.sqrt(Sxx))
    tr = round(t,2)
    print("Enter t score from table A.10 with t =",tr,"df = ",df)
    ts = float(input("t: "))
    if two_tailed:
        ts = ts * 2
    print("t score: ",ts)  
    print("f score: ",round(t**2,4))  
    if ts < alpha:
        print("t < a so we reject H0")
    else:
        print("t > a so we fail to reject H0")
        
if __name__ == "__main__":
    main()
