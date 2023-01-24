from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.ninja_model import Ninja

#create class method to obtain all dojos, one to get one dojo with all the ninjas to that dojo
#and one to create a new dojo 
#--------- Dojos table -must add all columns-  ----------# 
class Dojos:  #should be Dojo
    def __init__(self,data):
        self.id = data ['id']
        self.name = data ['name']
        self.created_at = data ['created_at']
        self.updated_at = data ['created_at']
        self.ninjas = []
        #place rest of table data as dic/hashmap


    #---- get all method /this gets all dojos/-----#    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos'
        results = connectToMySQL(DATABASE).query_db( query)

        #this is an empty dojo list-----
        dojos = []
        #---- we iterate for results 
        for dojo in results :
            new_dojo = cls(dojo)
            dojos.append(new_dojo)
        return dojos

    @classmethod
    def create (cls,data):

        query = '''
            INSERT INTO dojos (name)
            VALUES (%(name)s)
        '''
        return connectToMySQL(DATABASE).query_db(query,data)

    #------- get one dojo --------#
    @classmethod
    def get_one(cls,data):
        query = '''
            SELECT * FROM dojos 
            WHERE id = %(id)s
        '''
    
        results =  connectToMySQL(DATABASE).query_db(query,data)
    
        return cls (results[0])

    #----- get one with ninjas------#
    @classmethod
    def get_one_with_ninjas(cls,data):
        query = '''
            SELECT * FROM dojos
            JOIN ninjas on ninjas.dojo_id = dojos.id 
            WHERE dojo_id = %(id)s;
        '''
        # """  if this query was used intead ,then the if statement below wouldnt be needed because of the LEFT
        # SELECT * FROM dojos
        # LEFT JOIN ninjas on ninjas.dojo_id = dojos.id 
        # WHERE dojos.id = 8;
        # """
        results = connectToMySQL(DATABASE).query_db(query,data)
        

        #---- this is an /if/ there is no results
        if not results or len(results)<0:
            return cls.get_one(data)
        dojo = cls( results[0] )#Dojos.get_one_with_ninjas(data)
        dojo.ninjas = []
    
        for row in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id" : row["ninjas.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"],
                "dojo_id" : row ["dojo_id"]
            }
            new_ninja= Ninja(ninja_data)
            dojo.ninjas.append( new_ninja ) 
        return dojo

