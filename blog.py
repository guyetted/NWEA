from flask import Flask, request
from flask_restful import Resource, Api
from flask import render_template, request, url_for
from sqlalchemy import create_engine
from json import dumps

#Create a engine for connecting to SQLite3.
#Assuming blog.db is in app root folder

e = create_engine('sqlite:///blog.db')

app = Flask(__name__)
api = Api(app)
# Define a route for the default URL, which loads the html forms
@app.route('/')
def form():
    return render_template('form_submit.html')



class Get_all(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct title, body from posts")
        return {'posts': [i for i in query.cursor.fetchall()]}


 
## associate class methods to web endpoints 

api.add_resource(Get_all, '/posts')

if __name__ == '__main__':
     app.run()
