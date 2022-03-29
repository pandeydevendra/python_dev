import MySQLdb
import json
from flask import make_response

# cursor = db.cursor(MySQLdb.cursors.DictCursor)

class user_contoller_model():
    def __init__(self):
        try:
            self.db = MySQLdb.connect("localhost", "root", "root@123", "flask_tutorial")
            self.db.autocommit=True
            self.cur = self.db.cursor(MySQLdb.cursors.DictCursor)

            print("connection successful")
        except:
            print("some error")

    def user_getall_model(self):
        read_query = "SELECT * FROM users"
        self.cur.execute(read_query)
        result = self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)
            # return {"payload" : result}
            # return make_response({"payload" : result}, 200)
            response = make_response({"payload" : result}, 200)
            response.headers["Acces_Control_Allow_Origin"] = "*"
            return response

        else:
            # return {"meassage" : "No record found"}
            return make_response({"meassage" : "No record found"}, 204)


    def user_addone_model(self, data):
        add_query = f"""INSERT INTO users(name, email, phone, role, password, id) 
                    VALUES('{data['name']}', '{data['email']}', '{data['phone']}', 
                    '{data['role']}','{data['password']}', {data['id']})"""
        self.cur.execute(add_query)
        if self.cur.rowcount>0:
            return make_response({"meassage" : "User created successfully!"}, 201)
        else:
            return make_response({"meassage" : "Nothing to add"}, 204)
        

    def user_update_model(self, data):
        update_query = f"""
            UPDATE users SET 
            name = '{data['name']}', email = '{data['email']}', 
            phone = '{data['phone']}', role = '{data['role']}',
            password = '{data['password']}' WHERE id = {data['id']}"""
        print(update_query)
        self.cur.execute(update_query)
        if self.cur.rowcount>0:
            return make_response({"meassage" : "Record updated successfully!"}, 201)
        else:
            return make_response({"meassage" : "Nothing to Update"}, 202)
        
    def user_delete_model(self, id):
        delete_query = f"DELETE FROM users WHERE id = {id};"
        print(delete_query)
        self.cur.execute(delete_query)
        if self.cur.rowcount>0:
            return make_response({"meassage" : "Record deleted successfully!"}, 200)
        else:
            return make_response({"meassage" : "Nothing to delete"}, 202)
