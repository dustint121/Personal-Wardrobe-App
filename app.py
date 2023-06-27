from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

import pyodbc
from backend import queries




app = Flask(__name__)
CORS(app)

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-KHUP1V2;DATABASE=Wardrobe;Trusted_Connection=yes")


@app.route("/")
def dbUsers():
    return "Successfully connected to database"    


@app.route("/clothes", methods=['GET', 'POST'])
def get_pieces():
    try:
        if request.method == "GET":
            result = queries.retrieve_all_clothing(conn)
            return result, 200

        else:
            return "{0} not an implemented method".format(request.method)
    except Exception as e:
        return str(e), 500





if __name__ == "__main__":
    app.run()
    # conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-KHUP1V2;DATABASE=Wardrobe;Trusted_Connection=yes")
    # queries.add_clothing_piece(conn, short_descriptor="Test Cloth", brand="Club Monoco", category="Pants", 
    #                            url="https://di2ponv0v5otw.cloudfront.net/posts/2023/06/26/6499d2f6dff94d754b503d8e/m_wp_6499d2f6dff94d754b503d8f.webp")
    # queries.retrieve_all_clothing(conn)
    # retrieve_images(conn)
    # cursor = conn.cursor()
    # cursor.execute("SELECT @@version;") 
    # row = cursor.fetchone()
    # print(row)