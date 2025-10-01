def NewtonRaphson(func,funcder,x0,maxiter,tol):
    count=0
    x=[]
    for i in range(maxiter):
        if(funcder(x0)==0):
            break
        xi=x0-func(x0)/funcder(x0)
        count+=1
        x.append((count,xi,func(xi)))
        if(abs(xi-x0)<tol):
            break
        x0=xi
    return xi,x