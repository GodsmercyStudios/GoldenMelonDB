# Simple NoSQL Python Database

class GoldenDB():
    def __init__(database):
        import json
        # Create a dictionary for database
        database = {}
    
    def insert(key, value):
        # Add key-value
        database.append[key] = value
    
    def get(key):
        container = database.get(key, None)
        return container
    
    def delete(key):
        # delete key value pairs
        del database[key]
    
    def save(filename):
        with open(filename, "w") as fh:
            json.dump(database, fp)

    def load(filename):
        with open(filename, "r") as fh:
            database = json.load(fp)
    
    def listall():
        return list(database)
    
    
