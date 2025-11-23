'''
Integration

https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Integral_approximations-3-steps.png/320px-Integral_approximations-3-steps.png
Please try to add 1~3 line of code to finish the integration
def anonymous(x):
return x**2 + 1
def integrate(fun, start, end):
step = 0.1
intercept = start
area = 0
while intercept < end:
intercept += step
your work here
return area
print(integrate(anonymous, 0, 10))
'''

def anonymous(x):
    return x**2 + 1

def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
        area += anonymous(intercept) * step
    return area

print(integrate(anonymous, 0, 10))

