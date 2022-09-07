from pymongo import MongoClient

#conexion local
conn =  MongoClient()
#conexion con Docker
#uri = 'mongodb://test:password@mongoapi:27017/apicrudhunty?authSource=admindocker' 
#conn =  MongoClient(uri)


