from __future__ import division
from collections import Counter
import random
from collections import defaultdict

users = [{"id":1,"name":"Luciano"},
{"id":2,"name":"Patty"},
{"id":3,"name":"Mabel"},
{"id":4,"name":"Callida"},
{"id":5,"name":"Bobette"},
{"id":6,"name":"Eadmund"},
{"id":7,"name":"Pearl"},
{"id":8,"name":"Leslie"},
{"id":9,"name":"Janaya"},
{"id":10,"name":"Stuart"},
{"id":11,"name":"Abel"},
{"id":12,"name":"Yasmin"},
{"id":13,"name":"Mindy"},
{"id":14,"name":"Jennee"},
{"id":15,"name":"Layla"},
{"id":16,"name":"Gunilla"},
{"id":17,"name":"Amelina"},
{"id":18,"name":"Klarrisa"},
{"id":19,"name":"Guthrey"},
{"id":20,"name":"Sammie"}]

friendships = [(0,1),
(1,2),
(1,3),
(2,3),
(3,4),
(4,5),
(5,6),
(6,7),
(7,8),
(8,9),
(7,9),
(9,10),
(10,11),
(11,12),
(12,13),
(13,14),
(14,15),
(15,16),
(15,17),
(15,18),
(16,17),
(17,18),
(18,19),
(19,1),
(12,2),
(8,3)]

for user in users:
    user["friends"] = []

for i,j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friendships(user):
    return len(user["friends"])

total_connections = sum(number_of_friendships(user) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

num_friends_by_id = [(user["id"], number_of_friendships(user)) for user in users]

sorted(num_friends_by_id, key=lambda it: it[1], reverse=True)

print(num_friends_by_id)

def friends_of_friends_ids_bad(user):
    return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]]

def not_the_same(user, other_user):
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    return all(not_the_same(friend, other_user) for friend in user["friends"])

def friends_friends_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user, foaf) and not_friends(user, foaf))

print(friends_friends_ids(users[3]))

interests_list = ["Hadoop",
 "Big Data",
 "HBase",
 "Java",
 "NOSql",
 "MongoDB",
 "Cassandra",
 "scipy",
 "Pyhton",
 "R",
 "numpy",
 "Postgres",
 "scikit-learn",
 "statistics",
 "deeplearning",
 "mathematics",
 "theory",
 "pŕopability",
 "neural networks",
 "MapReduce",
"regression",
"Haskel",
"artificial intelligence",
"Mahout",
"libsvm",
"Storm",
"decision tree",
"programming language",
"pandas",
"C++"]

interests = []

for user in users:
    random.shuffle(interests_list)
    tuple_interest = [(user["id"], interest) for interest in interests_list[:7]]
    [interests.append(ti) for ti in tuple_interest]

print(interests)

def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interest_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interest_by_user_id[user_id].append(interests)

def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interest_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])