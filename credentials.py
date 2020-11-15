class Credentials:
    '''
    Class for generating account credentials,passwords and save this information
    '''
    
    credentials_list=[]

    def __init__(self,site_name,account_name,password):
        '''
        method to define the properties each user object will hold
        '''

        self.site_name=site_name
        self.account_name=account_name
        self.password=password

    def save_credentials(self):
        """Method that saves credential objects into credentials_list"""
        self.credentials_list.append(self)
    
    def delete_credential(self):
        '''
        Method to delete a created and saved credential
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls, site_name):
        '''
        Method that takes in a site name and returns a credential that matches that site name
        Args:
            name: site_name that has an account name and a numbered password
        Returns:
            The site_name ,account_name and it's corresponding Password
        '''

        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential
    
    @classmethod
    def credential_exists(cls, name):
        '''
        Method to check whether a credential exists
        Args:
        name: name of site to search whether it exists
        boolean: True or False depending if the contatc exists
        '''

        for credential in cls.credentials_list:
            if credential.site_name == name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        Method to display all saved credentials
        '''
        return cls.credentials_list