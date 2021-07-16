import uuid

class Client:

    def __init__(self, name:str, company:str, email:str, position:str, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()  # Generate a unique uid


    def to_dict(self):
        ''' 
        Let you access to a dictionary 
        representation of our object
        '''
        return vars(self)


    @staticmethod
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']



