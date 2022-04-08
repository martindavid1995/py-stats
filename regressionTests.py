import leastSquares as ls
import fStatistic as fs
import math

two_tailed = True
alpha = .05

def main():
    x = [67,37,70,40,35,65,40,35,30,40]
    y = [75,85,60,90,80,75,70,90,95,80]
    
    # get_CI(x,y)
    hyp_test(x,y)
    
    
def get_CI(x,y):
    df = len(x)-2
    S = math.sqrt(ls.SSE(x,y)/(df))
    if two_tailed:
        a = alpha/2
    print("Enter t critical value from table A.5 with v =",df,",a =",a)
    t = float(input("t: "))
    B1 = ls.b1(x,y)
    Sxx = ls.Sxx(x)
    range = t * (S/(math.sqrt(Sxx)))
    low = round(B1 - range,4)
    high = round(B1 + range,4)
    print("Standard Deviaton: ",S)
    print("(",low,",",high,")")
    
def hyp_test(x,y):
    B1 = ls.b1(x,y)
    df = len(x)-2
    S = math.sqrt(ls.SSE(x,y)/(df))
    Sxx = ls.Sxx(x)
    B10 = float(input("Enter B1 nought: "))
    t = (B1-B10)/(S/math.sqrt(Sxx))
    tr = round(t,1)
    print("Enter t score from table A.8 with t =",abs(tr),"v =",df)
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
