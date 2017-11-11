"""
Author: Ryan Baclit
Email: gamehelphere@gmail.com
Date: 11/11/2017
Disclaimer:

This software does not come with a warranty of any kind. It is your responsibility
to take care of your computer, software, and related setups. You will not hold the
author responsible for any problems that may arise during your use of the software.

Description:

The SQLite3 database portion of my WSGI Python server. It uses the schema included with this
project that contains basic recipe data for some tasty Filipino dishes. :)

I intend to use this server in other projects and will add notes about it later.

"""

import sqlite3

class RLB_SQL:

    def __init__(self):

        pass

    """

    The getRecipeList() method will connect to the SQLite3 database file and get the list of all recipes
    recored in the database. The database file must be in the same directory as the other Python files of
    this project. If you change directories, make sure to add the appropriate paths to help this script
    find the database to its new location.

    """

    def getRecipeList(self):

        dbConnection = sqlite3.connect('rlbrecipetime.sql')
        dbCursor = dbConnection.cursor()
        query = "SELECT * FROM recipe"
        dbCursor.execute(query)
        rows = dbCursor.fetchall()
        jsonRows = []

        if rows != None:
            for column in rows:

                """
                Assemble the JSON edition of this result if there is one.
                """

                newRow = {'recipecode' : column[0], 'description' : column[1], 'date' : column[2], 'servingsize' : column[3], 'servingsizeunit' : column[4]}
                jsonRows.append(newRow)

        return jsonRows

    """

    The getIngredientsList() method will get the ingredients of the selected recipe using the recipe code. This currently returns
    an empty array and will be changed soon.

    """

    def getIngredientsList(self, givenRecipeCode):

        dbConnection = sqlite3.connect('rlbrecipetime.sql')
        dbCursor = dbConnection.cursor()

        """

        I used some JOIN keywords to make the query connected to collect all needed information. You know, standard CRUD in SQL. :)

        """

        query = "SELECT ingredientcode, ingredients.description AS ingredientname, amount, unit.description AS unitname FROM ingredients JOIN unit ON ingredients.unitcode = unit.unitcode WHERE recipecode = " + givenRecipeCode
        dbCursor.execute(query)
        rows = dbCursor.fetchall()
        jsonRows = []

        if rows != None:
            for column in rows:
                print(column[0])

        return jsonRows
