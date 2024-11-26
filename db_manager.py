# Handles database interactions
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["barcode_db"]
collection = db["barcodes"]

def create_barcode_entry(data):
    collection.insert_one(data)

def read_barcodes():
    return list(collection.find())

def update_barcodes(query, updated_data):
    collection.update_one(query, {"$set": updated_data})

def delete_barcodes(query):
    collection.delete_one(query)