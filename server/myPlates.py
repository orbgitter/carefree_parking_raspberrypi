import pymongo

def get_plates():
    r=[]
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["users"]
    for x in mycol.find():
      #print(x)
      r.append(x["licence"])
    print("the numbers are")
    print(r)
    return r
    pass