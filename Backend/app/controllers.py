#############
## imports ##
#############
from flask import Flask, request, app, jsonify
from app import app, db
from models import Test
from sqlalchemy.exc import IntegrityError

###############
## Responses ##
###############
OK = ('', 200) #if everything was OK
created = ('', 201) #if something was created
pdenied = ('', 403) #if you doesn't have access
authrequired = ('', 401) #require auth
notfound = ('', 404) #force 404 error


#################
#### Routes  ####
#################

@app.route('/') #first create a index page
@app.route('/index') #second route, but does the same
def index(): #define function
    return jsonify(message='hi') #say hi to everyone

@app.route('/API/OK')
def returnOK():
    return OK #return HTTP Status-Code

@app.route('/API/Tests', methods=['GET', 'POST', 'PUT', 'DELETE']) #Define route with different HTTP request methods
def APITests():
    rdata = request.get_json() #allows to get JSON data from request example JSON data: {"title":"hello"}
    test_id = request.args.get('id') #get id from URL (/API/Tests/?id=<ID>)

    if request.method == 'GET': #define used method
        tests = Test.query.all() #get all tests
        jsonized = jsonify(tests=[(dict(id=test.id, title=test.title)) for test in tests]) #create list of tests
        return jsonized #return our list

    elif request.method == 'POST':
        title = rdata["title"] #get JSON "title"

        try: #try to add values into database, if you have same values entered, will force 403 error
            t = Test(title=title) #create new object
            db.session.add(t) #add to databasa
            db.session.commit() #commit changes

            return jsonify(created_id=t.id) #return id of created data (optional)
        except IntegrityError: #force error if data exists
            return pdenied

    elif request.method == 'PUT':
        new_title = rdata['title']
        try:
            db.session.query(Test).filter_by(id=test_id).update({"title": new_title}) #Update data
            db.session.commit()
            return OK
        except IntegrityError:
            return pdenied #force error if entered data is equal past data

    elif request.method == 'DELETE':

        Test.query.filter_by(id=test_id).delete() #delete by id(test_id)
        db.session.commit()
        return OK
