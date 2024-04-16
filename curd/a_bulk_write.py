from a_mongo import client
from pymongo import InsertOne, UpdateOne, DeleteOne, ReplaceOne, DeleteMany

db = client.t
collection_name = "pizzas"
print("写入前：")
for item in db[collection_name].find():
    print(item)

result_status = db[collection_name].bulk_write(
    [
        InsertOne({'_id': 3, 'type': "beef", 'size': "medium", 'price': 6}),
        InsertOne({'_id': 4, 'type': 'sausage', 'size': 'large', 'price': 10}),
        UpdateOne(
            {'type': 'cheese'},
            {'$set': {'price': 8}}
        ),
        DeleteOne({'type': "pepperoni"}),
        ReplaceOne(
            {'type': 'vegan'},
            {'type': 'tofu', 'size': 'small', 'price': 4},
            False  # 默认情况下是True 即没有符合条件的数据会进行插入操作
        )
    ]
)
print(result_status)
print("写入后：")
for item in db[collection_name].find():
    print(item)
