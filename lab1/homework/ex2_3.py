from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
posts = db['posts']
new_post = {
    "title": "Hoàng cương",
    "author": "linh tinh",
    "content": "Mình bắt chước loài mèo kêu nha , Kêu cùng anh méo méo méo méo",
}
posts.insert_one(new_post)
client.close()