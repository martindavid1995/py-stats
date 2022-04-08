
def main():
    x = [67,37,70,40,35,65,40,35,30,40]
    y = [75,85,60,90,80,75,70,90,95,80]
    if (len(x) != len(y)):
        raise Exception("Length of x and y are not equal")
    B1 = round(b1(x,y),2)
    B2 = round(b2(x,y),2)
    var = round(variance(x,y),4)
    c_d = round(coefficient_determination(x,y),2)
    
    print("Least squares line: ") 
    print("y = ",B1," x +",B2)
    print("Variance: ",var)
    print("Coefficient Determination: ",c_d)
    
def sum_x_y(x,y):
    sum = 0
    for i in range(len(x)):
        sum += x[i]*y[i]
    return sum

def sum_squares(arr):
    return sum(map(lambda i : i**2, arr))

def Sxy(x,y):
    return sum_x_y(x,y) - ((sum(x)*sum(y))/len(x))

def Sxx(x):
    return sum_squares(x) - (sum(x)**2/len(x))

def b1(x,y):
    return Sxy(x,y)/Sxx(x)

def b2(x,y):
    return (sum(y)-b1(x,y)*sum(x))/len(x)

def SEE(x,y):
    return Sxx(y)-b1(x,y)*Sxy(x,y)

def variance(x,y):
    return SEE(x,y)/(len(x) - 2)

def coefficient_determination(x,y):
    return 1-(SEE(x,y)/Sxx(y))
        
if __name__ == "__main__":
    main()