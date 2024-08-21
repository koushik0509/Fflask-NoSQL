import logging

from flask import Blueprint, jsonify, request, current_app
from flask_pymongo import PyMongo
from bson.json_util import dumps

logging.basicConfig(level=logging.DEBUG)
main = Blueprint('main', __name__)


@main.route('/tweets_by_day', methods=['GET'])
def tweets_by_day():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"text": {"$regex": "spears", "$options": "i"}}},
        {"$group": {"_id": {"$substr": ["$created_at", 0, 10]}, "count": {"$sum": 1}}}
    ]
    result = list(current_app.mongo.db.tweets.aggregate(pipeline))
    logging.debug(f"Aggregate result: {result}")

    return dumps(result)

@main.route('/unique_users', methods=['GET'])
def unique_users():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"text": {"$regex": term, "$options": "i"}}},
        {"$group": {"_id": "$author_id"}}
    ]
    unique_users_count = len(list(current_app.mongo.db.tweets.aggregate(pipeline)))
    return jsonify({'unique_users': unique_users_count})

@main.route('/average_likes', methods=['GET'])
def average_likes():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"text": {"$regex": term, "$options": "i"}}},
        {"$group": {"_id": None, "average_likes": {"$avg": "$like_count"}}}
    ]
    result = list(current_app.mongo.db.tweets.aggregate(pipeline))
    avg_likes = result[0]['average_likes'] if result else 0
    return jsonify({'average_likes': avg_likes})

@main.route('/places', methods=['GET'])
def places():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"text": {"$regex": term, "$options": "i"}}},
        {"$group": {"_id": "$place_id"}}
    ]
    places = [place['_id'] for place in list(current_app.mongo.db.tweets.aggregate(pipeline))]
    return jsonify({'places': places})

@main.route('/times_of_day', methods=['GET'])
def times_of_day():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"text": {"$regex": term, "$options": "i"}}},  # Filter by term in the text
        {"$project": {
            "time": {"$substr": ["$created_at", 11, 5]},  # Extract time (HH:mm) from created_at field
            "_id": 0
        }},
        {"$group": {
            "_id": "$time",  # Group by extracted time (HH:mm)
            "count": {"$sum": 1}  # Count the number of tweets for each time
        }},
        {"$sort": {"_id": 1}}  # Sort by time
    ]

    # Execute the aggregation pipeline
    result = list(current_app.mongo.db.tweets.aggregate(pipeline))
    logging.debug(f"Aggregate result: {result}")

    # Format the result for JSON response
    times_of_day = {item['_id']: item['count'] for item in result}
    return jsonify({'times_of_day': times_of_day})

@main.route('/top_user', methods=['GET'])
def top_user():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"text": {"$regex": term, "$options": "i"}}},
        {"$group": {"_id": "$author_id", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 1}
    ]
    result = list(current_app.mongo.db.tweets.aggregate(pipeline))
    top_user = result[0]['_id'] if result else None
    tweet_count = result[0]['count'] if result else 0
    return jsonify({'top_user': top_user, 'tweet_count': tweet_count})

#3if name == '__main__':
    #3app.run(debug=True)