import pyodbc
from PIL import Image
import requests
import json
import io
import base64

def add_clothing_piece(conn, short_descriptor=None, brand=None, category=None, url=None):
    cursor = conn.cursor()
    image_data = None
    if url != None:
        image_data = Image.open(requests.get(url, stream=True).raw)
        # Convert the image data to bytes
        buffered = io.BytesIO()
        image_data.save(buffered, format="JPEG")
        image_data = buffered.getvalue() # Convert the BytesIO object to bytes
    query = "INSERT INTO Clothing_Pieces (Short_Descriptor, Brand, Category, Image_Data) VALUES (?, ?, ?, ?)"
    cursor.execute(query, short_descriptor, brand, category, image_data)
    conn.commit()


def retrieve_all_clothing(conn):
    cursor = conn.cursor()
    cursor.execute("Select * from Clothing_Pieces")

    columns = [column[0] for column in cursor.description] #get attributes from sql select query

    results = []
    # Loop through the rows in the cursor
    for row in cursor:
        row_dict = dict(zip(columns, row)) # Create a dict for each row using zip to match column names and values
        encoded_img = base64.b64encode(row_dict["Image_Data"]) # Encode the bytes to a base64 string
        row_dict["Image_Data"] = encoded_img.decode("utf-8")   # stringify byte data

        results.append(row_dict) # Append the dict to the results list
    return json.dumps(results)




    #Driver 18 doesn't work for some reason
    # print(pyodbc.drivers())
    # driver = "ODBC Driver 17 for SQL Server"
    # server = "LOCALHOST"
    # database = "Testing"
    # input = 'DRIVER={' + driver + '};SERVER='+server+';DATABASE='+database+';UID=sa;'
    # print(input)
    # pyodbc.connect(input)
