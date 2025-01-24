# Gradient descent for linear regression
# formula : yhat = wx + b
# loss  = mean squared error= (y-yhat)**2 / N




import numpy as np

# Initialize the parameters
x = np.random.randn(10,1)
y = 2*x + np.random.rand()
# parameters
w = 0.0
b=0.0

# hyper parameter
learning_rate = 0.01

# create a gradient function
def descend(x,y,w,b,learning_rate):
    dldw = 0.0
    dldb = 0.0
    N = x.shape[0]

    #loss = (y-(wx+b))**2
    for xi,yi in zip(x,y):
        dldw += -2*xi*(yi - (w*xi+b))
        dldb += -2*(yi - (w*xi+b))

    #mkaes an update the w parameter
    w = w - learning_rate*(1/N)*dldw 
    b = b - learning_rate*(1/N)*dldb

    return w,b    

# iteratively make updates
for epoch in range(400):
    # Run gradient descent
    w,b = descend(x,y,w,b,learning_rate)
    yhat = w*x +b
    loss = np.divide(np.sum((y-yhat)**2, axis=0),x.shape[0])
    print(f'Epoch: {epoch}, loss is: {loss}, parameters w: {w}, b: {b}')
    pass


