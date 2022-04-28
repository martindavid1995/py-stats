import scipy.stats
from scipy.stats import chisquare


alpha = .01

def main():
    observed = [100,200,300,400]
    proportion = [.25,.25,.25,.25]
    
#   For sets of uncategorized data, plug in the data and write in the cutoffs, and run hypTest1Set()
    data = [.1,.99,1.14,1.26,3.24,.12,.26,.8,.79,1.16,1.76,.41,.59,.27,2.22,.66,.71,2.21,.68,.43,.11,.46,.69,.38,.91,.55,.81,2.51,2.77,.16,1.11,.02,2.13,.19,1.21,1.13,2.93,2.14,.34,.44]
    cutoffs = [0.2231, .5108 ,.9163, 1.6094]
    
    # hypTest1Set(data, cutoffs)
    # hypTest(observed, proportion)
   
def hypTest1Set(data, cutoffs):
    split = splitData(data, cutoffs)
    
    observed = []
    proportion = []
    
    for d in split:
        observed.append(len(d))
        proportion.append(1/(len(cutoffs)+1))
        
    hypTest(observed, proportion)

def splitData(data, cutoffs):
    split = []
    numSplits = len(cutoffs) + 1
    
    for i in range(0,numSplits):
        split.append([])
        
    for val in data:
        if val >= 0 and val < cutoffs[0]:
            split[0].append(val)
        elif val >= cutoffs[-1]:
            split[-1].append(val)
        else:
            for i in range(0,len(cutoffs)-1):
                if val >= cutoffs[i] and val < cutoffs[i+1]:
                    split[i+1].append(val)
       
    return split              

def hypTest(observed, proportion):
    chiVal = getXsquared(observed, proportion)
    print("X^2 value is ",round(chiVal, 3))
    cv = scipy.stats.chi2.ppf(1-alpha,len(observed)-1)
    print("Critical value is ",cv)
    if (cv > chiVal):
        print("cv > chiVal => p > a so fail to reject H0")
    else:
        print("cv > chiVal => p < a so reject H0")
    
def getXsquared(observed, proportion):
    exp = []
    res = 0;
    n = sum(observed);
    
    for val in proportion:
        exp.append(n*val)
        
    for i in range(len(observed)):
        res += (((observed[i]-exp[i])**2)/exp[i])
        
    return res

if __name__ == "__main__":
    main()