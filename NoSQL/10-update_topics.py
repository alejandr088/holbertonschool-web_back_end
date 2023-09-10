#!/usr/bin/env python3
"""Change school topics """
import pymongo


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school doc based on the name"""
    if not mongo_collection:
        return None
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
