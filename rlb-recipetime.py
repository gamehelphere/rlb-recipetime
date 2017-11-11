"""
Author: Ryan Baclit
Email: gamehelphere@gmail.com
Date: 11/11/2017
Disclaimer:

This software does not come with a warranty of any kind. It is your responsibility
to take care of your computer, software, and related setups. You will not hold the
author responsible for any problems that may arise during your use of the software.

Description:

The WSGI Python web server to handle HTTP requests from my AngularJS 5 project.

"""

from bottle import hook, route, request, Bottle, run, response, post
from rlb_sql import RLB_SQL

"""
Hook to allow Cross-Site behavior to test with the local loop IP address. I need
to do this because the port of this script is not in any standard port.

"""

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

"""
Make secure browsers fine with the local loop address when they send in OPTIONS request.

This is cool about BottlePy. You can put multiple route() definitions to accomodate multiple HTTP requests, and a
function to handle it. :)

"""

@route('/grabrecipes', method = 'OPTIONS')
@route('/showrecipeingredients', method = 'OPTIONS')
def prepare():

    enable_cors()

    return

"""
The /grabrecipes route will get the current list of recipes from the connected SQLite3 database.
"""

@route('/grabrecipes', method = 'PUT')
def grabRecipes():

    rlbSQL = RLB_SQL()
    jsonRows = rlbSQL.getRecipeList()

    response.headers['Content-Type'] = 'application/json'

    """"

    Return as a dictionary to become a JSON format value back to the calling site.
    I stuck with the 'data' key as the main key to the values to help new AngularJS programmers
    understand how to do Angular with BottlePy.

    """

    return dict(data = jsonRows)


"""

The /showrecipeingredients route() with its function. This function will return the ingredients from the connected
SQLite3 database back to the caller. Similar to the grabRecipes() function, this function will return the data in
JSON format through a dictionary.

"""

@route('/showrecipeingredients', method = 'GET')
def showRecipeIngredients():

    recipeCode = request.query.recipecode

    print("Recipe code ay ")
    print(recipeCode)

    rlbSQL = RLB_SQL()
    if recipeCode != None:
        jsonRows = rlbSQL.getIngredientsList(recipeCode)
    response.headers['Content-Type'] = 'application/json';

    return dict(data = jsonRows)

run(host='0.0.0.0', port=5002, debug=True)
