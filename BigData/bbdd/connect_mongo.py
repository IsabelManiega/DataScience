import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client.itti

# print(db)

def insertar(db):
    db.test.insert_one({"name": "Raul", "age": 224})

# insertar(db)

def actualizar(db):
    datos = db.test.find({})
    for dato in datos:
        if dato['name'] == 'Raul':
            # print(dato['_id'])
            idMongo = dato['_id']
            db.test.update_one({'_id': idMongo}, 
                               {'$set':{'age':230}})

# actualizar(db)

def mostrar(db):
    datos = db.test.find({})
    for dato in datos:
        print(dato)



def delete(db):
    datos = db['test'].find({})
    for dato in datos:
        if dato['name'] == "Raul":
            idMongo = dato['_id']
            db.test.delete_one({'_id': idMongo})
    
# delete(db)
mostrar(db)