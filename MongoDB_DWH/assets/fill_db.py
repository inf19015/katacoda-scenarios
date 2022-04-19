import json
import pymongo


def get_database():
    connection_string = "mongodb://localhost"
    client = pymongo.MongoClient(connection_string)
    return client["test"]


if __name__ == "__main__":
    data_persons = json.load(open("data_persons_merged.json", "r"))
    dbname = get_database()
    collection_name = dbname["person"]
    collection_name.insert_many(data_persons)
