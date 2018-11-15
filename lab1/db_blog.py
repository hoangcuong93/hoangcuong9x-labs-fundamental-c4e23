from pymongo import MongoClient

uri = "mongodb://hoangcuong93:cuong11a6@ds127961.mlab.com:27961/c4e23-blog"

#1 connect
client = MongoClient(uri)

#2 get default database 
db = client.get_database()

#3 get collection
posts = db['posts']
movies = db['movies']

#4 create data
new_post = {
    "title": "Hom nay giong bao",
    "comtent": "toi o nha code",
}
new_movies = {
    "title": "doremon",
    "rating": "10"
}
#5 insert data
# posts.insert_one(new_post)
# movies.insert_one(new_movies)

# 5 read data
posts_list = posts.find()
# p = posts_list[2]
for p in posts_list:
    print(p['title'])
    print(p['comtent'])

#6 close connection
client.close()