
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Ninja:
    def __init__(self,data):
        self.id = data ['id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.age = data ['age'] 
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.dojo_id = data ['dojo_id']
        

#------- create method to add ninja on form ------#
    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO ninjas (first_name,last_name,age,dojo_id)
            VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s) 
        """
        return connectToMySQL(DATABASE).query_db( query, data )

    # @classmethod
    # def get_one(cls,data):
    #     query = '''
    #         SELECT * FROM ninjas 
    #         WHERE id = %(id)s
    #     '''
    
    #     results =  connectToMySQL(DATABASE).query_db(query,data)
    #     one_ninja = cls(results[0])
    #     print("---------------------------->", one_ninja)
    #     return one_ninja


# @classmethod
# def save(cls, data ):
#         query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
#         # data is a dictionary that will be passed into the save method from server.py
#         return connectToMySQL('first_flask').query_db( query, data )