import random
import string
#users_list
class User:
    '''
    class to create users accounts and save their informations
    '''
    users_list=[]
    def __init__(self,first_name,last_name,password):
        '''
        Method to define the properties for each user object
        '''

        self.first_name=first_name
        self.last_name=last_name
        self.password=password
    
    def __init__(self):
        
        '''
        function for saving a new created user instance
        '''
        user.users_list.append(self)


