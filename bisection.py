def Bisection(func,x0,x1,maxiter,tol):
    count=0
    x=[]
    if(abs(func(x0))<1e-12):
        x.append(x0)
    if(abs(func(x1))<1e-12):
        x.append(x1)
    for i in range(maxiter):
        xr=x0+(x1-x0)/2
        count+=1
        x.append(count,xr,func(xr))
        if(abs(xr-x1)<tol):
            break
        if(func(xr)*func(x0)<0):
            x1=xr
        if(func(xr)*func(x1)<0):
            x0=xr
    return xr,x