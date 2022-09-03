#!/usr/bin/python3
# this is the base model for the airbnb project
"""this model defines all
common attributes for other classes
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """this class class defines all
    common attr for all other classes
    """

    def __init__(self, *args, **kwargs):
        """the class constructor"""
        if kwargs:
            if 'id' in list(kwargs):
                self.id = kwargs['id']
            if 'updated_at' in list(kwargs):
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if 'created_at' in list(kwargs):
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if 'my_number' in list(kwargs):
                self.my_number = kwargs['my_number']
            if 'name' in list(kwargs):
                self.name = kwargs['name']
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """the unofficial repr of this class"""
        string = "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)
        return string

    def save(self):
        """updates 'updated_at' with the currenct time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        dic = dict.copy(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = datetime.isoformat(self.created_at)
        dic['updated_at'] = datetime.isoformat(self.updated_at)
        return dic
