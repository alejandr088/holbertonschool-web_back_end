#!/usr/bin/env python3
"""List all documents in Python"""
import pymongo


def list_all(mongo_collection):
    """lists all documents in a collection"""
    a_list = []
    if not mongo_collection:
        return a_list
    return mongo_collection.find()
