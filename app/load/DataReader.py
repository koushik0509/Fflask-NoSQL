import pandas as pd
from pymongo import MongoClient
def load_data_to_mongodb(tsv_file, mongo_uri, db_name, collection_name):
    # Load the TSV file
    df = pd.read_csv(tsv_file, sep='\t')
    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict(orient='records')
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    # Insert data into MongoDB
    collection.insert_many(data)
    print("Data loaded successfully into MongoDB.")

if __name__ == "__main__":
    # Update these variables as needed
    tsv_file = '/Users/koushikreddy/PycharmProjects/pythonProject/app/load/resources/correct_twitter_201904.tsv'
    mongo_uri = 'mongodb://localhost:27017/'
    db_name = 'twitter_db'
    collection_name = 'tweets'
    load_data_to_mongodb(tsv_file, mongo_uri, db_name, collection_name)