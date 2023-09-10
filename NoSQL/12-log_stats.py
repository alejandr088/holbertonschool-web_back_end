#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
import pymongo


def log_stats():
    """provides some stats about Nginx logs stored in MongoDB"""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]

    total_logs = collection.count_documents({})

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in http_methods}

    get_status_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")

    print("Methods:")
    for method in http_methods:
        print(f"\t{method_counts[method]}")

    print(f"{get_status_count} status check")


if __name__ == "__main__":
    log_stats()
