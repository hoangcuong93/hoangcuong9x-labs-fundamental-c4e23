from matplotlib import pyplot
from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_database()
customers = db["customers"]
refs = {}
customers_list = customers.find()
for customer in customers_list:
    refs[customer["ref"]] = refs.get(customer["ref"], 0) + 1
for (k, v) in refs.items():
    print(k, v, sep = ": ")
print("The number of customers group by​ 'refs': ")
ref_count = list(refs.values())
ref_names = list(refs.keys())

pyplot.pie(ref_count, labels=ref_names, autopct="%.3f %%", shadow=True, explode=[0, 0, 0.2, 0])
pyplot.title("References from Events, Ads and Word of Mouth")
pyplot.axis("equal")
pyplot.show()

client.close()
