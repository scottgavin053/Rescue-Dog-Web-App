from pymongo import MongoClient
from bson import ObjectId, json_util
import json

class AnimalShelter(object):
    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        
        #connect to database with no authentication
        #self.client = MongoClient('mongodb://localhost:54636')
        
        #connect to database with authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:54636/AAC' % (username,password))
        self.database = self.client['AAC']



    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Complete this method to implement the R in CRUD
    def read(self,data):
        cursor = self.database.animals.find(data,{'_id':False})
        #returns cursor that is a pointer to a list of results
        return cursor

    # The U method of CRUD
    def update(self,data):
        if data is not None:
            upd_json = json.dumps(self.database.animals.save(data), default = str)
            print(upd_json)
        else:
            raise Exception("Nothing to update, becasue animal parameter is empty")
            
    #the D method of CRUD
    def delete(self,data):
        if data is not None:
            del_json = json.dumps(self.database.animals.remove(data), default = str)
            return del_json
        else:
            raise Exception("Nothing the remove, because parameter is empty")
               
               