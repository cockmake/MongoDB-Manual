import datetime

from a_mongo import client

db = client.t

# 多条件查询
# db.inventory.insert_many([
#     {"item": "journal", "status": "A", "size": {"h": 14, "w": 21, "uom": "cm"},
#      "instock": [{"warehouse": "A", "qty": 5}]},
#     {"item": "notebook", "status": "A", "size": {"h": 8.5, "w": 11, "uom": "in"},
#      "instock": [{"warehouse": "C", "qty": 5}]},
#     {"item": "paper", "status": "D", "size": {"h": 8.5, "w": 11, "uom": "in"},
#      "instock": [{"warehouse": "A", "qty": 60}]},
#     {"item": "planner", "status": "D", "size": {"h": 22.85, "w": 30, "uom": "cm"},
#      "instock": [{"warehouse": "A", "qty": 40}]},
#     {"item": "postcard", "status": "A", "size": {"h": 10, "w": 15.25, "uom": "cm"},
#      "instock": [{"warehouse": "B", "qty": 15}, {"warehouse": "C", "qty": 35}]}
# ])

# 数组查询

# db.inventory.insert_many([
#     {"item": "journal", "qty": 25, "tags": ["blank", "red"], "dim_cm": [14, 21]},
#     {"item": "notebook", "qty": 50, "tags": ["red", "blank"], "dim_cm": [14, 21]},
#     {"item": "paper", "qty": 100, "tags": ["red", "blank", "plain"], "dim_cm": [14, 21]},
#     {"item": "planner", "qty": 75, "tags": ["blank", "red"], "dim_cm": [22.85, 30]},
#     {"item": "postcard", "qty": 45, "tags": ["blue"], "dim_cm": [10, 15.25]}
# ])

# for item in db.inventory.find(
# ):
#     print(item)

# 查询空字段或缺少字段

# db.inventory.insert_many([
#     {"item": None},
#     {}
# ])

#    { item: "canvas", qty: 100, size: { h: 28, w: 35.5, uom: "cm" }, status: "A" },
#    { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
#    { item: "mat", qty: 85, size: { h: 27.9, w: 35.5, uom: "cm" }, status: "A" },
#    { item: "mousepad", qty: 25, size: { h: 19, w: 22.85, uom: "cm" }, status: "P" },
#    { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "P" },
#    { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
#    { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
#    { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" },
#    { item: "sketchbook", qty: 80, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
#    { item: "sketch pad", qty: 95, size: { h: 22.85, w: 30.5, uom: "cm" }, status: "A" }

# 更新文档

# db.inventory.insert_many(
#     [
#         {"item": "canvas", "qty": 100, "size": {"h": 28, "w": 35.5, "uom": "cm"}, "status": "A"},
#         {"item": "journal", "qty": 25, "size": {"h": 14, "w": 21, "uom": "cm"}, "status": "A"},
#         {"item": "mat", "qty": 85, "size": {"h": 27.9, "w": 35.5, "uom": "cm"}, "status": "A"},
#         {"item": "mousepad", "qty": 25, "size": {"h": 19, "w": 22.85, "uom": "cm"}, "status": "P"},
#         {"item": "notebook", "qty": 50, "size": {"h": 8.5, "w": 11, "uom": "in"}, "status": "P"},
#         {"item": "paper", "qty": 100, "size": {"h": 8.5, "w": 11, "uom": "in"}, "status": "D"},
#         {"item": "planner", "qty": 75, "size": {"h": 22.85, "w": 30, "uom": "cm"}, "status": "D"},
#         {"item": "postcard", "qty": 45, "size": {"h": 10, "w": 15.25, "uom": "cm"}, "status": "A"},
#         {"item": "sketchbook", "qty": 80, "size": {"h": 14, "w": 21, "uom": "cm"}, "status": "A"},
#         {"item": "sketch pad", "qty": 95, "size": {"h": 22.85, "w": 30.5, "uom": "cm"}, "status": "A"}
#     ]
# )

# 删除文档

# db.inventory.insert_many(
#     [
#         {"item": "journal", "qty": 25, "size": {"h": 14, "w": 21, "uom": "cm"}, "status": "A"},
#         {"item": "notebook", "qty": 50, "size": {"h": 8.5, "w": 11, "uom": "in"}, "status": "P"},
#         {"item": "paper", "qty": 100, "size": {"h": 8.5, "w": 11, "uom": "in"}, "status": "D"},
#         {"item": "planner", "qty": 75, "size": {"h": 22.85, "w": 30, "uom": "cm"}, "status": "D"},
#         {"item": "postcard", "qty": 45, "size": {"h": 10, "w": 15.25, "uom": "cm"}, "status": "A"},
#     ]
# )


# 批量插入文档bulk_write操作
# collection_name = "pizzas"
# db[collection_name].insert_many([
#     {"_id": 0, "type": "pepperoni", "size": "small", "price": 4},
#     {"_id": 1, "type": "cheese", "size": "medium", "price": 7},
#     {"_id": 2, "type": "vegan", "size": "large", "price": 8}
# ])


# 执行文本搜索

# collection_name = "stores"
# db[collection_name].insert_many(
#     [
#         {'_id': 1, 'name': 'Java Hut', 'desc': 'Coffee and cakes'},
#         {'_id': 2, 'name': 'Burger Buns', 'desc': 'Gourmet hamburgers'},
#         {'_id': 3, 'name': 'Coffee Shop', 'desc': 'Just coffee'},
#         {'_id': 4, 'name': 'Clothes Clothes Clothes', 'desc': 'Discount clothing'},
#         {'_id': 5, 'name': 'Java Shopping', 'desc': 'Indonesian goods'}
#     ]
# )

# 聚合操作
# collection_name = "orders"
# db[collection_name].insert_many(
#     [
#         {'_id': 0, 'name': 'Pepperoni', 'size': 'small', 'price': 19, 'quantity': 10,
#          'date': datetime.datetime(2021, 3, 13, 8, 14, 30)},
#         {'_id': 1, 'name': 'Pepperoni', 'size': 'medium', 'price': 20, 'quantity': 20,
#          'date': datetime.datetime(2021, 3, 13, 9, 13, 24)},
#         {'_id': 2, 'name': 'Pepperoni', 'size': 'large', 'price': 21, 'quantity': 30,
#          'date': datetime.datetime(2021, 3, 17, 9, 22, 12)},
#         {'_id': 3, 'name': 'Cheese', 'size': 'small', 'price': 12, 'quantity': 15,
#          'date': datetime.datetime(2021, 3, 13, 11, 21, 39, 736000)},
#         {'_id': 4, 'name': 'Cheese', 'size': 'medium', 'price': 13, 'quantity': 50,
#          'date': datetime.datetime(2022, 1, 12, 21, 23, 13, 331000)},
#         {'_id': 5, 'name': 'Cheese', 'size': 'large', 'price': 14, 'quantity': 10,
#          'date': datetime.datetime(2022, 1, 12, 5, 8, 13)},
#         {'_id': 6, 'name': 'Vegan', 'size': 'small', 'price': 17, 'quantity': 10,
#          'date': datetime.datetime(2021, 1, 13, 5, 8, 13)},
#         {'_id': 7, 'name': 'Vegan', 'size': 'medium', 'price': 18, 'quantity': 10,
#          'date': datetime.datetime(2021, 1, 13, 5, 10, 13)}
#     ]
# )

# for item in db[collection_name].find():
#     print(item)
