from flask import Flask, request
import json, httplib, urllib
app = Flask(__name__)

# --------- GET calls------------------------
@app.route('/get_cook', methods=['GET'])
def get_cooks():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Cook/', '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    })
    result = json.loads(connection.getresponse().read())
    print(result)
    print(type(result))
    print(json.dumps(result))
    print(type(json.dumps(result)))
    return json.dumps(result)


@app.route('/get_menu/<menu_id>', methods=['GET'])
def get_menu(menu_id):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Menu/'+menu_id, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    })
    result = json.loads(connection.getresponse().read())
    # result is the JSON representation of the menu object requested
    return result


@app.route('/get_cook/<cook_id>', methods=['GET'])
def get_cook(cook_id):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Cook/'+cook_id, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    })
    result = json.loads(connection.getresponse().read())
    # result is the JSON representation of the menu object requested
    return result


@app.route('/get_order/<order_id>', methods=['GET'])
def get_order(order_id):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Order/'+order_id, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    })
    result = json.loads(connection.getresponse().read())
    # result is the JSON representation of the menu object requested
    return result


#--------Create Menu, Cook, Order----------------------------------------------


@app.route('/create_food', methods=['POST'])
def create_food():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    name = "Pad Thai"
    description = "Steamed vegetables fried with noodles, and tofu"
    dietaryRestriction = "None"
    spicyLevel = 2
    connection.request('POST', '/1/classes/Food', json.dumps({
        "name": name,
        "description": description,
        "dietaryRestriction": dietaryRestriction,
        "spicyLevel": spicyLevel,
    }), {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json"
    })
    result = json.loads(connection.getresponse().read())    
    return result['objectId']


@app.route('/create_menu', methods=['POST'])
def create_menu():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    arrayFoodIds = ["JnogXVpUsk", "YFbATirCJ4"]
    cookId = "me36TAsNuN"
    connection.request('POST', '/1/classes/Menu', json.dumps({
        "arrayFoodIds": arrayFoodIds, # request.form['Description'],
    }), {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json"
    })
    result = json.loads(connection.getresponse().read())
    menu_id = result['objectId']

    # Update cook with menu_id

    connection.request('PUT', '/1/classes/Cook/'+cookId, json.dumps({
       "menuId": menu_id
    }), {
       "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
       "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
       "Content-Type": "application/json"
    })
    return menu_id # This should be a success message or error message


@app.route('/create_order', methods=['POST'])
def create_order():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    cookId = "me36TAsNuN"
    hungryId = "kVPzQNpR0h"
    selectedFoodItems = ["JnogXVpUsk"]

    connection.request('POST', '/1/classes/Order', json.dumps({
        "cookId": cookId,
        "hungryId": hungryId,
        "selectedFoodItems": selectedFoodItems,
    }), {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json"
    })
    result = json.loads(connection.getresponse().read())   
    return result['objectId']


@app.route('/create_cook', methods=['POST'])
def create_cook():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    user_id = "ulR5Pcv0Qw" # Wont be using POST. Will have to take from user logged in
    capacity_remaining = 3
    startTime = "2015-02-28T02:06:57.931Z"
    endTime = "2015-02-28T12:06:57.931Z"
    category = "Oriental"
    # TODOCreate only if prev user_id not used
    connection.request('POST', '/1/classes/Cook', json.dumps({
        "userId": user_id, # request.form['Description'],
        "capacityRemaining": capacity_remaining, # request.form['Category'],
        "endTime": {
            "__type": "Date",
            "iso": endTime, #request.form['endTime']
        },
        "startTime": {
            "__type": "Date",
            "iso": startTime, #request.form['endTime']
        },
        "category": category,
    }), {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json"
    })
    result = json.loads(connection.getresponse().read()) 
    return result['objectId']


# --Get Menu/Menus--------------------------------------------------------------------


@app.route('/get_all_menus', methods=['GET'])
def get_all_menus():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Menu', )    


# --Update------------------------------------------------------------------


@app.route('/update_capacity_remaining/<cook_id>', methods=['PUT'])
def update_capacity_remaining(cook_id):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Cook/'+cook_id, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json" 
    })
    result = json.loads(connection.getresponse().read())
    if(result['capacityRemaining'] == 0):
        return "Limit reached"

    connection.request('PUT', '/1/classes/Cook/'+cook_id, json.dumps({
       "capacityRemaining": {
            "__op": "Increment",
            "amount": -1
        }
    }), {
       "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
       "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
       "Content-Type": "application/json"
    })
    result = json.loads(connection.getresponse().read())
    print result
    return result


#----------Authentication------------------------------------------------


@app.route('/signup', methods=['POST'])
def signup():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/users', json.dumps({
           "username": "cooldude26",
           "password": "p_n7!-e823",
           "fullName": "Cool Dude Man",
           "address": {
                "__type": "GeoPoint",
                "latitude": 40.0,
                "longitude": -30.0
            },
           "phone": "4153920202"
         }), {
           "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
           "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
           "Content-Type": "application/json"
         })
    result = json.loads(connection.getresponse().read())
    # TODO: save session token somehow
    print result
    return "result"


@app.route('/signin', methods=['POST'])
def signin():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    params = urllib.urlencode({"username":"cooldude6","password":"p_n7!-e8"})
    connection.connect()
    connection.request('GET', '/1/login?%s' % params, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    })
    result = json.loads(connection.getresponse().read())
    print result
    # do something with sessionToken
    return "result"


@app.route('/logout', methods=['POST'])
def logout():
    # clear session token
    return "result"


# --------------------------------------------------------------


if __name__ == '__main__':
    app.run()