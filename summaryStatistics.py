def sum_x_y(x,y):
    sum = 0
    for i in range(len(x)):
        sum += x[i]*y[i]
    return sum

def sum_squares(arr):
    return sum(map(lambda i : i**2, arr))

def Sxy(x,y):
    return sum_x_y(x,y)-((sum(x)*sum(y))/len(x))

def Sxx(x):
    return sum_squares(x)-(sum(x)**2/len(x))

def b1(x,y):
    return Sxy(x,y)/Sxx(x)

def b2(x,y):
    return (sum(y)-b1(x,y)*sum(x))/len(x)

def SSE(x,y):
    return Sxx(y)-b1(x,y)*Sxy(x,y)

def variance(x,y):
    return SSE(x,y)/(len(x) - 2)

def coefficient_determination(x,y):
    return 1-(SSE(x,y)/Sxx(y))