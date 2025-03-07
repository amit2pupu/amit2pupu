from flask import Flask,request,render_template
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import os
import pymongo

MONGO_URI=os.getenv('MONGO_URI')
client=pymongo.MongoClient(MONGO_URI)
db=client.test
collection=db['flask-tutorial']
app= Flask(__name__)
@app.route('/')
def home():
    day_of_the_week=datetime.today().strftime('%A')+ ', '+datetime.today().strftime('%B')+', '+datetime.today().strftime('%d') +'-'+datetime.today().strftime('%Y')
    return render_template('index.html',day_of_the_week=day_of_the_week)
@app.route('/api')

def name():
    name = request.values.get('name')
    age=request.values.get('age')
    age=int(age)
    if age<20:
        return'not welcome'

    result={
        'name':name,
        'age': age
    }
    
    return result
@app.route('/submit',methods=['Post'])
def submit():
    form_data=dict(request.form)
    collection.insert_one(form_data)
    return "Data Submitted Succefully!"

if __name__=='__main__':
    app.run(debug=True)
