from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoCRUD:
    
    #  Constructive
    def __init__(self, uri, db_name):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            self.client.admin.command("ping")
            print(f"✅ Connected to MongoDB database: '{db_name}'")
        except ConnectionFailure as e:
            print(f"❌ Connection failed: {e}")

    # Read
    def get_collection(self, collection_name):
        return self.db[collection_name]

    # Create
    def insert_document(self, collection_name, document):
        """Insert a single document"""
        collection = self.get_collection(collection_name)
        result = collection.insert_one(document)
        print(f"Inserted document with _id: {result.inserted_id}")
        return result.inserted_id

    # Create bulk
    def insert_documents(self, collection_name, documents):
        """Insert multiple documents"""
        collection = self.get_collection(collection_name)
        result = collection.insert_many(documents)
        print(f"Inserted {len(result.inserted_ids)} documents.")
        return result.inserted_ids

    # Read
    def read_documents(self, collection_name, query={}, projection=None):
        """Read documents that match the query"""
        collection = self.get_collection(collection_name)
        results = collection.find(query, projection)
        return list(results)

    #Update
    def update_document(self, collection_name, query, new_values):
        """Update a single document"""
        collection = self.get_collection(collection_name)
        result = collection.update_one(query, {'$set': new_values})
        print(f"Matched {result.matched_count}, Modified {result.modified_count}")
        return result.modified_count

    # Update bulk
    def update_documents(self, collection_name, query, new_values):
        """Update multiple documents"""
        collection = self.get_collection(collection_name)
        result = collection.update_many(query, {'$set': new_values})
        print(f"Matched {result.matched_count}, Modified {result.modified_count}")
        return result.modified_count

    # Delete
    def delete_document(self, collection_name, query):
        """Delete a single document"""
        collection = self.get_collection(collection_name)
        result = collection.delete_one(query)
        print(f"Deleted {result.deleted_count} document.")
        return result.deleted_count

    # Delete bulk
    def delete_documents(self, collection_name, query):
        """Delete multiple documents"""
        collection = self.get_collection(collection_name)
        result = collection.delete_many(query)
        print(f"Deleted {result.deleted_count} documents.")
        return result.deleted_count

    # Read all documents
    def list_all_documents(self, collection_name):
        """List all documents in the collection"""
        collection = self.get_collection(collection_name)
        return list(collection.find())

    # Read all table
    def list_collections(self):
        """List all collections in the database"""
        return self.db.list_collection_names()
    
    #Create Collection
    def create_mongo_collection(self, collection_name):
 
        try:
            if collection_name in self.db.list_collection_names():
                print(f"Collection '{collection_name}' already exists.")
                return self.db[collection_name]
            else:
                self.db.create_collection(collection_name)
                print(f" Created new collection: '{collection_name}'")
                return self.db[collection_name]
        except Exception as e:
            print(f" Error creating collection: {e}")
            return None