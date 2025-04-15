import pandas as pd
from pymongo import MongoClient

def import_csv_to_mongodb(uri, db_name, collection_name, csv_file_path):
    """
    Imports data from a CSV file into a MongoDB collection.

    Parameters:
    - uri (str): MongoDB connection string
    - db_name (str): Database name
    - collection_name (str): Target collection name
    - csv_file_path (str): Path to the CSV file
    """
    try:
        # Load CSV into pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Convert DataFrame to list of dicts
        data = df.to_dict(orient="records")

        # Connect to MongoDB
        client = MongoClient(uri)
        db = client[db_name]
        collection = db[collection_name]

        # Insert data into MongoDB
        if data:
            result = collection.insert_many(data)
            print(f"✅ Inserted {len(result.inserted_ids)} documents into '{collection_name}'")
        else:
            print("⚠️ CSV file is empty. No data inserted.")

    except Exception as e:
        print(f"❌ Error: {e}")


def fetch_api_to_mongodb(uri, db_name, collection_name, api_url, params=None):
    """
    Fetches data from an API and inserts it into a MongoDB collection.

    Parameters:
    - uri (str): MongoDB connection string
    - db_name (str): Target database name
    - collection_name (str): Target collection name
    - api_url (str): The API endpoint to fetch data from
    - params (dict, optional): Dictionary of query parameters to append to the API call
    """
    try:
        # Fetch data from API
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()

        if not data:
            print("⚠️ No data found at the API endpoint.")
            return

        # Normalize if the data is inside a nested key (optional)
        if isinstance(data, dict):
            # Modify this part based on the API's data structure
            data = data.get("results", data.get("data", data))

        # Connect to MongoDB
        client = MongoClient(uri)
        db = client[db_name]
        collection = db[collection_name]

        # Insert into MongoDB
        if isinstance(data, list):
            result = collection.insert_many(data)
            print(f"✅ Inserted {len(result.inserted_ids)} documents into '{collection_name}'")
        else:
            result = collection.insert_one(data)
            print(f"✅ Inserted 1 document into '{collection_name}'")

    except requests.exceptions.RequestException as e:
        print(f"❌ API request error: {e}")
    except Exception as e:
        print(f"❌ MongoDB error: {e}")
