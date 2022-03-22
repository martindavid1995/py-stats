import numpy as np

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
    

def sum_rows(data: np.array):
    sums = []
    for i in range(len(data)):
        p_sum = 0
        for j in range(len(data[0])):
            p_sum += data[i][j]
        sums.append(p_sum)
    return sums

def main():
    # data = np.array(   [[321.2,	409.5,	311.0,	326.5,	316.8,	349.8,	309.7],
    #                     [401.1,	347.2,	361.0,	404.5,	331.0,	348.9,	381.7],
    #                     [389.4,	366.2,	351.0,  357.1,	409.9,	367.3,	382.0],
    #                     [353.7,	452.9,	461.4,	433.1,	410.6,	384.2,	362.6],
    #                     [406.4,	441.8,	419.9,	410.7,	473.4,	441.2,	465.8]])
    
    data = np.array([[67,50,70,60,55],
                     [49,32,65,39,43],
                     [40,39,41,60,45]])
    

    
    print("SST: ",SST(data))
    print("SSTr: ",SSTr(data))
    print("SSE: ",SSE(data))
    

if __name__ == "__main__":
    main()
    
    