import math

def f(x): #python representation of f(x) = sin(x) * cos(x)
    return math.sin(x) * math.cos(x)

def areaUnderCurve(start,end,step_size):
    area = 0 #initialize area variable to store total area under the curve
    x = start #start from the beginning of the interval
    while x < end: #continue until reaching the end of the interval
        area += abs(f(x)) * step_size #add the absolute value of the area of the current rectanglar portion of the graph
        x += step_size #increment to next position along x-axis
    return area #return total area

start = 0 #define start of the interval
end = 4 * math.pi #define the end of the interval (4π)
step_size = 0.001 #define the step size for approximating the area 

area = areaUnderCurve(start,end,step_size)
print("Simulated area under curve of f(x): ", area)