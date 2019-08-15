from functools import wraps

def time_this(func) :
    @wraps(func) 
    def timed_func(*args,**kwargs) :
        import datetime                 
        before = datetime.datetime.now()                     
        x = func(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print("Elapsed Time = {}".format(after-before))     
        return x                                             
    return timed_func
