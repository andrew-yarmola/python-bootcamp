def requires(group):                            
    def decorator(func):                                            
        def decorated(*args,**kwargs):                            
            if group is None or group in get_groups(cur_user_id()) :     
                return func(*args,**kwargs)                         
            raise Exception("Permission Denied")                  
        return decorated                                          
    return decorator

def cur_user_id():
    """ Returns the current user id if the user is authenticaed, otherwise return None """
    return 501
    
def get_groups(user_id):
    """ Returns a groups for the given user, e.g. ['admin','authenticaed','wheel'] """
    return ('authenticaed',)

@requires('authenticaed')
def launch_task():
    """ Launch a new task. Accessible to authenticated users """

@requires('wheel')    
def save_task_result():
    """ Save task results. Accessable to wheel users """

@requires('admin')
def delete_user(user_id):
   """ Delete the given user. Accessable to admins """
