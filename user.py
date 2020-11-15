class User: 
    '''
    class to create users accounts and save their informations
    '''
    users_list=[] # Empty users list
    
    def __init__(self,user_name,password):
        '''
        Method to define the properties for each user object
        '''

        self.user_name=user_name
        self.password=password
    
    def save_user(self):
        
        '''
        function for saving a new created user instance
        '''
        self.users_list.append(self)
    
if __name__ == '__main__':
    main()



