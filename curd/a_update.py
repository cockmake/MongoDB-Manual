from a_mongo import client


db = client.t
# collection_name = "inventory"
collection_name = "students"

# 查询条件
condition = {
    # "item": None,
    # "item": {"$exists": False},
    # "qty": {'$gte': 100},

}
# 更新或替换语句
operation = {
    # "$set": {"size.uom": "cm", "status": "P"},  # $set 操作是更新
    # "$currentDate": {"lastModified": True}
    # "$set": {"qty": 800}

    # "size": [1, 2, 3]  # 取代操作配合replace使用


}


# 更新前
print("更新文当前：")
for item in db[collection_name].find(condition):
    print(item)

# 更新文档

# db.inventory.update_one(condition, operation)
# db.inventory.update_many(condition, operation)

# 替换一个文档
# db.inventory.replace_one(condition, operation)

# 替换多个文档
# db.inventory.find(condition)
# for item in db.inventory.find(condition):
#     db.inventory.replace_one(item, operation)



print("更新文当后：")
for item in db[collection_name].find(condition):
    print(item)