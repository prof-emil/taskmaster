# Wrap do MongoDB
import pymongo
# Lib para fazer o URL-Encode
import urllib.parse
# Bcrypt usado para hashing e salting
import bcrypt


# Definindo um schema para a collection usuario
userSchema = {
    "$jsonSchema" : {
        "bsonType" : "object",
        "required" : ["username", "password"],
        "properties": {
            "username" : { "bsonType" : "string" },
            "password" : { "bsonType" : "string" } 
            } 
        }
    }


url_cluster ="mongodb+srv://admin:admin@clusterts.hmyzydo.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(url_cluster)
db = client["ssidbiii"]

def run_migrations:
    if not "usuarios" in db.list_collection_names():
        db.create_collection("usuarios", validator=userSchema)


def create_user(usuario, senha):
    usuario = urllib.parse.quote(usuario)

    if db["usuarios"].find_one({"username": usuario }):
        return False

    senha = urllib.parse.quote(senha)
    senha_bytes = senha.encode("utf-8")
    salt = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha_bytes, salt)

    return db["usuarios"].insert_one({"username": usuario, "senha": hash_senha})


def busca_user(usuario):
    usuario = urllib.parse.quote(usuario)

    resposta = db["usuarios"].find_one({"username": usuario }):
    if not resposta:
        return False

    return resposta

def valida_user(usuario, senha):
    usuario = busca_user(usuario)

    if not usuario:
        return False

    senha = urllib.parse.quote(senha)
    if bcrypt.checkpw(senha, usuario["senha"]):
        return True

    return False





