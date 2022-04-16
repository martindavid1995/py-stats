import summaryStatistics as ss
import math
import statistics as st
import scipy.stats as sp

alpha = .05

def main():
    x = [1.5,1.5,2.0,2.5,2.5,3.0,3.5,3.5,4.0]
    y = [24.0,24.5,26.0,29.5,33.5,39.0,40.5,48.0,50.0]
    
    if (len(x) != len(y)):
        raise Exception("Length of x and y are not equal")
    
    # confidenceInterval(x,y)
    # predictionInterval(x,y)
    # print(t_statistic(x,y))
    # hyp_test(x,y)
    
def hyp_test(x,y):
    print("Enter B-nought")
    b10 = float(input("B-nought:"))
    t = t_statistic(x,y,b10)
    print("t-statistic: ",round(t,3))
    p = p_value(x,t)
    print("p-value: ",round(p,5))
    if (p < alpha):
        print("p < a so we reject H0")
    else:
        print("p > a so we fail to reject H0")

def t_statistic(x,y,b10):
    S = math.sqrt(ss.SSE(x,y)/(len(x)-2))
    Sxx = ss.Sxx(x)
    b1 = ss.b1(x,y)
    return ((b1-b10)/(S/math.sqrt(Sxx)))
    

def p_value(x,t):
    return round(sp.t.sf(t, df=(len(x)-1)),4)
    
def confidenceInterval(x,y):
    print("--CONFIDENCE INTERVAL--")
    b0 = ss.b2(x,y)
    b1 = ss.b1(x,y)
    print("Enter value you are testing for")
    x_ = float(input("x: "))
    yHat = b0 + (b1*x_)
    s2 = ss.variance(x,y)
    s = math.sqrt(s2)
    Sy = math.sqrt(((1/len(x))+((x_-st.mean(x))**2)/ss.Sxx(x))) * s
    t = abs(sp.t.ppf(q=alpha/2,df=len(x)-2))
    ME = t * Sy
    CI_l = round(yHat - ME,3)
    CI_h = round(yHat + ME,3)
    print("(",CI_l,",",CI_h,")")


def predictionInterval(x,y):
    print("--PREDICTION INTERVAL--")
    b0 = ss.b2(x,y)
    b1 = ss.b1(x,y)
    print("Enter value you are testing for")
    x_ = float(input("x: "))
    yHat = b0 + (b1*x_)
    s2 = ss.variance(x,y)
    Sy = math.sqrt(((1/len(x))+((x_-st.mean(x))**2)/ss.Sxx(x))) * math.sqrt(s2)
    t = abs(sp.t.ppf(q=alpha/2,df=len(x)-2))
    ME = t * math.sqrt(s2 + (Sy**2))
    PI_l = round(yHat - ME,3)
    PI_h = round(yHat + ME,3)
    print("(",PI_l,",",PI_h,")")
    
        
if __name__ == "__main__":
    main()