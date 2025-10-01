def FalsePosition(func,x0,x1,maxiter,tol):
    count=0
    x=[]
    for i in range(maxiter):
        if(func(x1)-func(x0)==0):
            break
        xr=x1-(func(x1)*(x1-x0))/(func(x1)-func(x0))
        count+=1
        x.append((count,xr,func(xr)))
        if(abs(xr-x1)<tol):
            break
        if(func(xr)*func(x0)<0):
            x1=xr
        if(func(xr)*func(x1)<0):
            x0=xr
    return xr,x