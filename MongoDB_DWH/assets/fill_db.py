import json
import pymongo


def get_database():
    connection_string = "mongodb://localhost"
    client = pymongo.MongoClient(connection_string)
    return client["dwh"]


if __name__ == "__main__":
    dbname = get_database()

    data_persons = json.load(open("data_persons_merged.json", "r"))
    collection_name = dbname["person"]
    collection_name.insert_many(data_persons)

