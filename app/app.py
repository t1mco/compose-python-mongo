import time
from pymongo import MongoClient

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    myclient = MongoClient('mongodb', 27017)
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mydict = { "name": "John", "address": "Highway 37" }
    x = mycol.insert_one(mydict)

    return 'document count ' + str(mycol.find().count()) 

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="80", debug=True)
