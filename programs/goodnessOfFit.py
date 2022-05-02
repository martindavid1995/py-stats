import numpy as np
import scipy.stats


alpha = .05

def main():
    observed_counts = np.array([
                                [13.7,10.88,2.02,13.7],
                                [27.71,27.71,4.08,22.01],
                                [17.69,25.62,3.05,14.64],
                                [26.47,38.43,5.12,15.37]
                                ])

    
    hypTest(observed_counts)

def hypTest(data):
    x2 = getX2(data) 
    print("X2 value is :",round(x2,3))
    
    df = ((len(data)-1) * (len(data[0])-1))
    
    cv = scipy.stats.chi2.ppf(1-alpha,df)
    
    print("Critical value is ",cv)
    if (cv > x2):
        print("cv > chiVal => p > a so fail to reject H0")
    else:
        print("cv > chiVal => p < a so reject H0")
     

def getX2(obs):
    exp = getExp(obs)
    totX = 0
    
    for i in range(0,len(obs)):
        for j in range(0,len(obs[0])):
            totX += ((obs[i][j]-exp[i][j])**2)/exp[i][j]
    
    return totX   
 
def getExp(data):
    # Sum up rows and cols
    r = data.sum(axis=1)
    c = data.sum(axis=0)
    
    ests = np.zeros([len(data),len(data[0])], dtype=float)
    for i in range(0,len(data)):
        for j in range(0,len(data[0])):
            ests[i][j] = (r[i]*c[j])/sum(r)
    
    return ests

if __name__ == "__main__":
    main()