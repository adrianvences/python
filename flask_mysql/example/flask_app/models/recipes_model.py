from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask_app.models.user_model import User
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
#------- class constructor created from the MySql database-----#
class Recipe :
    def __init__(self,data) :
        self.id = data ['id']
        self.name = data ['name']
        self.description = data ['description']
        self.instructions = data ['instructions']
        self.under_30 = data ['under_30']
        self.date_cooked = data ['date_cooked']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.user_id = data ['user_id']

#------ create a recipe ------#
    @classmethod
    def add_recipe(cls,data):
        query = '''
        INSERT INTO recipes
        (name,description,instructions,date_cooked,under_30,user_id)
        VALUES (%(name)s,%(description)s,%(instructions)s,%(date_cooked)s,%(under_30)s, %(user_id)s)
        '''
        return connectToMySQL(DATABASE).query_db(query,data)




#----- get all recipes -------#
    @classmethod
    def get_all(cls):
        query = '''
        SELECT * FROM recipes
        '''
        results =  connectToMySQL(DATABASE).query_db(query)

        recipes = []
        for result in results :
            recipes.append(cls(result))
        
        return recipes




#------ delete recipe ------#
    @classmethod 
    def delete(cls,data):
        query = '''
        DELETE FROM recipes WHERE id = %(id)s
        '''
        connectToMySQL(DATABASE).query_db(query, data)

#------ thsi gets all with user_id-----#
    @classmethod
    def get_all_with_users(cls):
        
        query = '''
            SELECT * FROM recipes
            JOIN users
            ON users.id = recipes.user_id
        '''
        results = connectToMySQL(DATABASE).query_db(query)

        recipes = []
        for result in results :
            recipe = cls(result)

            user_data = {
                **result,
                'id' : result ['users.id'],
                'created_at' : result ['users.created_at'],
                'updated_at' : result ['users.updated_at']

            }

            recipe.user = User(user_data)

            recipes.append(recipe)
        return recipes


    #---- this validates recipes ------#
    @staticmethod
    def validate_recipes (data):
        is_valid = True 
        #---- if statements for each input ------#
        print(data)
        if len(data['name']) < 3:
            flash('please provide name longer than 3 letters')
            is_valid = False

        if len(data['description']) < 3:
            flash('please provide description longer than 3 letters')
            is_valid = False

        if len(data['instructions']) < 3:
            flash('please provide instructions longer than 3 letters')
            is_valid = False

        return is_valid 



#------find by recipe------#
    @classmethod
    def find_one_user_by_recipe(cls,data):
        query ='''
            SELECT * FROM recipes JOIN users ON users.id = recipes.user_id
            WHERE recipes.id = %(id)s ;
        '''

        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results[0])
        if results or len(results) > 0:
            # finding = cls.find_by_user(data['id'])
            # print('this is the finding---------->>>>>>>',finding)
            return results[0]

# grab the recipe and start with the recipe var 
        recipe = cls(results[0])

# this is setting it to be one result
# based on the results index 
        result = results[0]

# we are grabbing the data to make a user
        user_data = {
                **result,
                'id':result ['users.id'],
                'created_at': result ['users.created_at'],
                'updated_at' : result ['users.created_at']
            }

# we are creating a new attribute for recipe called creator
# and setting it equal to the User object using user_data 
        recipe.creator = User(user_data)

# and then we are returning the recipe object
        return recipe


#------- finds recipe by id--------#
    @classmethod
    def find_by_recipe(cls,id):

        data = {
            'id' : id,
        }
        query = '''
            SELECT * FROM recipes
            WHERE id = %(id)s
        '''
        results = connectToMySQL(DATABASE).query_db( query, data )

        if results and len(results) > 0:
            found_user = cls(results[0])
            return found_user
        else:
            return False




#------ this saves the edit made -----#
    @classmethod 
    def edit (cls,data):

        query = '''
            UPDATE recipes SET
            name = %(name)s,
            description = %(description)s,
            instructions = %(instructions)s,
            date_cooked = %(date_cooked)s,
            under_30 = %(under_30)s
            WHERE id = %(id)s
        '''

        return connectToMySQL(DATABASE).query_db(query,data)