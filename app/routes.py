from flask import Blueprint, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
main = Blueprint('main', name)

@main.route('/tweets_by_day', methods=['GET'])
def tweets_by_day():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"tweet": {"$regex": term, "$options": "i"}}},
        {"$group": {"_id": "$date", "count": {"$sum": 1}}}
    ]
    result = list(mongo.db.tweets.aggregate(pipeline))
    return dumps(result)

@main.route('/unique_users', methods=['GET'])
def unique_users():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"tweet": {"$regex": term, "$options": "i"}}},
        {"$group": {"_id": "$user_id"}}
    ]
    unique_users_count = len(list(mongo.db.tweets.aggregate(pipeline)))
    return jsonify({'unique_users': unique_users_count})

@main.route('/average_likes', methods=['GET'])
def average_likes():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"tweet": {"$regex": term, "$options": "i"}}},
        {"$group": {"_id": None, "average_likes": {"$avg": "$likes"}}}
    ]
    result = list(mongo.db.tweets.aggregate(pipeline))
    avg_likes = result[0]['average_likes'] if result else 0
    return jsonify({'average_likes': avg_likes})

@main.route('/places', methods=['GET'])
def places():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"tweet": {"$regex": term, "$options": "i"}}},
        {"$group": {"_id": "$place_id"}}
    ]
    places = [place['_id'] for place in list(mongo.db.tweets.aggregate(pipeline))]
    return jsonify({'places': places})

@main.route('/times_of_day', methods=['GET'])
def times_of_day():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"tweet": {"$regex": term, "$options": "i"}}},
        {"$project": {"time": 1}}
    ]
    times = [item['time'] for item in list(mongo.db.tweets.aggregate(pipeline))]
    return jsonify({'times_of_day': times})

@main.route('/top_user', methods=['GET'])
def top_user():
    term = request.args.get('term', '')
    pipeline = [
        {"$match": {"tweet": {"$regex": term, "$options": "i"}}},
        {"$group": {"_id": "$user_id", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 1}
    ]
    result = list(mongo.db.tweets.aggregate(pipeline))
    top_user = result[0]['_id'] if result else None
    tweet_count = result[0]['count'] if result else 0
    return jsonify({'top_user': top_user, 'tweet_count': tweet_count})

#3if name == '__main__':
    #3app.run(debug=True)