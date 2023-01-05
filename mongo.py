import pymongo 
def set_parking(myclient):
    mydb = myclient["mydatabase"]
    mycol = mydb["parking"]
    x = mycol.delete_many({})
    mydict = { "parking": "True" }

    x = mycol.insert_one(mydict)

    
def set_unparking(myclient):

    mydb = myclient["mydatabase"]
    mycol = mydb["parking"]
    x = mycol.delete_many({})
    mydict = { "parking": "False" }
    x = mycol.insert_one(mydict)
    
