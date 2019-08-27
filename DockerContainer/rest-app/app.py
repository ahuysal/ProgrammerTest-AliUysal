from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in your app root folder

e = create_engine('sqlite:///testdb.db')

app = Flask(__name__)
api = Api(app)

class Visits(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        conn.execute("delete from frequent_browsers")
        conn.execute("insert into frequent_browsers select v.personId person_id, count(v.siteId) num_sites_visited from visits v join people p on v.personId = p.id join sites s on v.siteId = s.id group by v.personId order by count(v.siteId) desc limit 10")
        query = conn.execute("select * from frequent_browsers")

        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

api.add_resource(Visits, '/Visits')

if __name__ == '__main__':
     app.run(host="0.0.0.0")