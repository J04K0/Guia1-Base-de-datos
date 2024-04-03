import pymongo

MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIMEOUT=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/"

MONGO_BASEDATOS="Tienda"
MONGO_COLECCION="Despensa"

try:
    client=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIMEOUT)
    baseDatos=client[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]
    for documento in coleccion.find():
        print(documento)
    client.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido ",errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Error de conexión ",errorConexion)

