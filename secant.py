def Secant(func,x0,x1,maxiter,tol):
    count=0
    x=[]
    for i in range(maxiter):
        if(func(x1)-func(x0)==0):
            break
        xi=x1-(func(x1)*(x1-x0))/(func(x1)-func(x0))
        count+=1
        x.append(count,xi,func(xi))
        if(abs(xi-x1)<tol):
            break
        x0=x1
        x1=xi
    return xi,x