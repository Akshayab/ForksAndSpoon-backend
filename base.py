from flask import Flask, request
import json, httplib, urllib
app = Flask(__name__)

# --------- GET calls------------------------


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


#-------------------------------------------------------------------

# Stage 2 of I want to become a cook
# submit menu details
# MAY NEED TO SQUISH CREATE_MENU AND CREATE_ORDER
@app.route('/create_menu', methods=['POST'])
def create_menu():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/classes/Menu', json.dumps({
        "Description": "Ramen", # request.form['Description'],
        "Category": "Chinese", # request.form['Category'],
        "dietaryRestriction": "Vegetarian", # request.form['dietaryRestriction']
        "spicyLevel": 3,
    }), {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json"
    })
    result = json.loads(connection.getresponse().read())
    # If successful, result contains objectId, and createdAt
    # In case of an error, result contains the error message
    return "result" # This should be a success message or error message


# Stage 3 of I want to become a cook
# Menu_id, Cook_id and hungry_id = undefined
@app.route('/create_order', methods=['POST'])
def create_order():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    cook_id = "XGoOxKcOwL"
    hungry_id = "someUserId" # hungry could either be undefined or a user_id
    connection.request('POST', '/1/classes/Order', json.dumps({
        "cookId": cook_id, # request.form['Description'],
        "hungryId": hungry_id, # request.form['Category'],
    }), {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json"
    })
    result = json.loads(connection.getresponse().read())   
    return "result"


# Stage 1 of I want to become a cook
# Submit user object and capacity_remaining
@app.route('/create_cook', methods=['POST'])
def create_cook():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    user_id = "ulR5Pcv0Qw" # Wont be using POST. Will have to take from user logged in
    menu_id = "enterSomeMenuId"
    capacity_remaining = 3
    # TODOCreate only if prev user_id not used
    connection.request('POST', '/1/classes/Cook', json.dumps({
        "userId": user_id, # request.form['Description'],
        "capacityRemaining": capacity_remaining, # request.form['Category'],
        "menuId": menu_id,
        "endTime": {
            "__type": "Date",
            "iso": "2015-02-28T12:06:57.931Z", #request.form['endTime']
        },
        "startTime": {
            "__type": "Date",
            "iso": "2015-02-28T02:06:57.931Z", #request.form['endTime']
        },
    }), {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json"
    })
    result = json.loads(connection.getresponse().read()) 
    return "result"


@app.route('/update_capacity_remaining/<cook_id>', methods=['PUT'])
def update_capacity_remaining(cook_id):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Cook/'+cook_id, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json" 
    })
    if(request.capacityRemaining == 0):
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


@app.route('/update_order_with_hungry_user/<order_id>/<hungry_id>', methods=['POST'])
def update_order_with_hungry_user(order_id, hungry_id):
    # TODO: A cook cannot be hungry
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()

    connection.request('PUT', '/1/classes/Order/'+order_id, json.dumps({
       "hungryId": hungry_id
    }), {
       "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
       "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
       "Content-Type": "application/json"
    })
    return "result"

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