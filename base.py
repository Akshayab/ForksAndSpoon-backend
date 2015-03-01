from flask import Flask, request, Response
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
    return Response(json.dumps(result),  mimetype='application/json')


@app.route('/get_food', methods=['GET'])
def get_food():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Food/', '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    })
    result = json.loads(connection.getresponse().read())
    return Response(json.dumps(result),  mimetype='application/json')


@app.route('/get_food/<foodId>', methods=['GET'])
def get_menu(foodId):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Food/'+foodId, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    })
    result = json.loads(connection.getresponse().read())
    return Response(json.dumps(result),  mimetype='application/json')


@app.route('/get_menu', methods=['GET'])
def get_menus():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Menu/', '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    }) 
    result = json.loads(connection.getresponse().read())
    return Response(json.dumps(result),  mimetype='application/json')


@app.route('/get_menu/<menuId>', methods=['GET'])
def get_menu(menuId):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Menu/'+menuId, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    })
    result = json.loads(connection.getresponse().read())
    return Response(json.dumps(result),  mimetype='application/json')


@app.route('/get_cook/<cook_id>', methods=['GET'])
def get_cook(cook_id):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Cook/'+cook_id, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    })
    result = json.loads(connection.getresponse().read())
    return Response(json.dumps(result),  mimetype='application/json')


@app.route('/get_order/<order_id>', methods=['GET'])
def get_order(order_id):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Order/'+order_id, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    })
    result = json.loads(connection.getresponse().read())
    return Response(json.dumps(result),  mimetype='application/json')


#--------Create Menu, Cook, Order----------------------------------------------


@app.route('/create_food', methods=['POST'])
def create_food():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    jsonObj = request.json
    name = jsonObj['name']
    description = jsonObj['description']
    dietaryRestriction = jsonObj['dietaryRestriction']
    spicyLevel = jsonObj['spicyLevel']
    price = jsonObj['price']
    connection.request('POST', '/1/classes/Food', json.dumps({
        "name": name,
        "description": description,
        "dietaryRestriction": dietaryRestriction,
        "spicyLevel": spicyLevel,
        "price": price,
    }), {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json"
    })
    result = json.loads(connection.getresponse().read())    
    return Response(json.dumps({'foodId': result['objectId']}),  mimetype='application/json')


@app.route('/create_menu', methods=['POST'])
def create_menu():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    jsonObj = request.json
    arrayFoodIds = jsonObj['arrayFoodIds']
    cookId = jsonObj['cookId']
    connection.request('POST', '/1/classes/Menu', json.dumps({
        "arrayFoodIds": arrayFoodIds,
        "cookId": cookId,
    }), {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json"
    })
    result = json.loads(connection.getresponse().read())
    menuId = result['objectId']

    # Update cook with menu_id

    connection.request('PUT', '/1/classes/Cook/'+cookId, json.dumps({
       "menuId": menuId
    }), {
       "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
       "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
       "Content-Type": "application/json"
    })
    return Response(json.dumps({"menuId": menuId}),  mimetype='application/json') # This should be a success message or error message


@app.route('/create_order', methods=['POST'])
def create_order():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    jsonObj = request.json
    cookId = jsonObj['cookId']
    hungryId = jsonObj['hungryId'] # hard coded userId
    selectedFoodItems = jsonObj['selectedFoodItems']

    connection.request('GET', '/1/classes/Cook/'+cookId, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
        "Content-Type": "application/json" 
    })
    result = json.loads(connection.getresponse().read())
    if(result['capacityRemaining'] == 0):
        return Response(json.dumps({'error': "Sorry, capacity limit reached"}),  mimetype='application/json')

    connection.request('PUT', '/1/classes/Cook/'+cookId, json.dumps({
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
    return Response(json.dumps({'orderId': result['objectId']}),  mimetype='application/json')


@app.route('/create_cook', methods=['POST'])
def create_cook():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    jsonObj = request.json
    userId = jsonObj['userId'] # Wont be using POST. Will have to take from user logged in
    capacityRemaining = jsonObj['capacityRemaining']
    startTime = jsonObj['startTime']
    endTime = jsonObj['endTime']
    category = jsonObj['category']

    connection.request('POST', '/1/classes/Cook', json.dumps({
        "userId": userId, # request.form['Description'],
        "capacityRemaining": capacityRemaining, # request.form['Category'],
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
    return Response(json.dumps({'cookId': result['objectId']}),  mimetype='application/json')


#----------Is user routes------------------------------------------------


@app.route('/is_user_cook/<userId>', methods=['GET'])
def is_user_cook(userId):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    params = urllib.urlencode({"where":json.dumps({
        "userId": userId, 
    })})
    connection.connect()
    connection.request('GET', '/1/classes/Cook?%s' % params, '', {
        "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
        "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
    })
    result = json.loads(connection.getresponse().read())

    if len(result['results']) == 1:
        return Response(json.dumps({'isCook': True}),  mimetype='application/json')
    else:
        return Response(json.dumps({'isCook': False}),  mimetype='application/json')



#----------Authentication------------------------------------------------


# @app.route('/signup', methods=['POST'])
# def signup():
#     connection = httplib.HTTPSConnection('api.parse.com', 443)
#     connection.connect()
#     connection.request('POST', '/1/users', json.dumps({
#         "username": "cooldude26",
#         "password": "p_n7!-e823",
#         "fullName": "Cool Dude Man",
#         "address": {
#             "__type": "GeoPoint",
#             "latitude": 40.0,
#             "longitude": -30.0
#         },
#         "phone": "4153920202"
#         }), {
#             "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
#             "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV",
#             "Content-Type": "application/json"
#         })
#     result = json.loads(connection.getresponse().read())
#     # TODO: save session token somehow
#     print result
#     return "result"


# @app.route('/signin', methods=['POST'])
# def signin():
#     connection = httplib.HTTPSConnection('api.parse.com', 443)
#     params = urllib.urlencode({"username":"cooldude6","password":"p_n7!-e8"})
#     connection.connect()
#     connection.request('GET', '/1/login?%s' % params, '', {
#         "X-Parse-Application-Id": "mL4QwznW8QOvKhqbG9DpDRn42Kpj4rETCeLLEMju",
#         "X-Parse-REST-API-Key": "Ld88eQRGwvTfe7ocsG2Gn5K942B9s8dOTlhGEvEV"
#     })
#     result = json.loads(connection.getresponse().read())
#     print result
#     # do something with sessionToken
#     return "result"


# @app.route('/logout', methods=['POST'])
# def logout():
#     # clear session token
#     return "result"


# --------------------------------------------------------------


if __name__ == '__main__':
    app.run()