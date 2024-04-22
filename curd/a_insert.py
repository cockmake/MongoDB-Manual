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

# $set | $addFields | $project 字段
# collection_name = "scores"
# db[collection_name].insert_many(
#     [
#         {
#             "_id": 1,
#             "student": "Maya",
#             "homework": [10, 5, 10],
#             "quiz": [10, 8],
#             "extraCredit": 0
#         },
#         {
#             "_id": 2,
#             "student": "Ryan",
#             "homework": [5, 6, 5],
#             "quiz": [8, 8],
#             "extraCredit": 8
#         }
#     ]
# )


# $bucket 分组筛选
# collection_name = "artists"
# db.artists.insert_many([
#     {"_id": 1, "last_name": "Bernard", "first_name": "Emil", "year_born": 1868, "year_died": 1941,
#      "nationality": "France"},
#     {"_id": 2, "last_name": "Rippl-Ronai", "first_name": "Joszef", "year_born": 1861, "year_died": 1927,
#      "nationality": "Hungary"},
#     {"_id": 3, "last_name": "Ostroumova", "first_name": "Anna", "year_born": 1871, "year_died": 1955,
#      "nationality": "Russia"},
#     {"_id": 4, "last_name": "Van Gogh", "first_name": "Vincent", "year_born": 1853, "year_died": 1890,
#      "nationality": "Holland"},
#     {"_id": 5, "last_name": "Maurer", "first_name": "Alfred", "year_born": 1868, "year_died": 1932,
#      "nationality": "USA"},
#     {"_id": 6, "last_name": "Munch", "first_name": "Edvard", "year_born": 1863, "year_died": 1944,
#      "nationality": "Norway"},
#     {"_id": 7, "last_name": "Redon", "first_name": "Odilon", "year_born": 1840, "year_died": 1916,
#      "nationality": "France"},
#     {"_id": 8, "last_name": "Diriks", "first_name": "Edvard", "year_born": 1855, "year_died": 1930,
#      "nationality": "Norway"}
# ])
# $facet 多通道操作
# collection_name = "artwork"
# db[collection_name].insert_many([
#     {"_id": 1, "title": "The Pillars of Society", "artist": "Grosz", "year": 1926, "price": 199.99},
#     {"_id": 2, "title": "Melancholy III", "artist": "Munch", "year": 1902, "price": 280.00},
#     {"_id": 3, "title": "Dancer", "artist": "Miro", "year": 1925, "price": 76.04},
#     {"_id": 4, "title": "The Great Wave off Kanagawa", "artist": "Hokusai", "price": 167.30},
#     {"_id": 5, "title": "The Persistence of Memory", "artist": "Dali", "year": 1931, "price": 483.00},
#     {"_id": 6, "title": "Composition VII", "artist": "Kandinsky", "year": 1913, "price": 385.00},
#     {"_id": 7, "title": "The Scream", "artist": "Munch", "year": 1893},
#     {"_id": 8, "title": "Blue Flower", "artist": "O'Keefe", "year": 1918, "price": 118.42}
# ])


# $count对文档流结果进行统计
# collection_name = "scores"

# db[collection_name].insert_many(
#     [
#         {"_id": 1, "subject": "History", "score": 88},
#         {"_id": 2, "subject": "History", "score": 92},
#         {"_id": 3, "subject": "History", "score": 97},
#         {"_id": 4, "subject": "History", "score": 71},
#         {"_id": 5, "subject": "History", "score": 79},
#         {"_id": 6, "subject": "History", "score": 83}
#     ]
# )

# $fill 对缺少或null字段进行填充
# 填充常量
# collection_name = "dailySales"
# db[collection_name].insert_many(
#     [
#         {
#             "date": datetime.datetime.fromisoformat("2022-02-02"),
#             "bootsSold": 10,
#             "sandalsSold": 20,
#             "sneakersSold": 12
#         },
#         {
#             "date": datetime.datetime.fromisoformat("2022-02-03"),
#             "bootsSold": 7,
#             "sneakersSold": 18
#         },
#         {
#             "date": datetime.datetime.fromisoformat("2022-02-04"),
#             "sneakersSold": 5
#         }
#     ]
# )
# 线性填充
# collection_name = "stock"
# db[collection_name].insert_many(
#     [
#         {
#             'time': datetime.datetime.fromisoformat("2021-03-08 09:00:00"),
#             'price': 500
#         },
#         {
#             'time': datetime.datetime.fromisoformat("2021-03-08 10:00:00"),
#         },
#         {
#             'time': datetime.datetime.fromisoformat("2021-03-08 11:00:00"),
#             'price': 515
#         },
#         {
#             'time': datetime.datetime.fromisoformat("2021-03-08 12:00:00")
#         },
#         {
#             'time': datetime.datetime.fromisoformat("2021-03-08 13:00:00")
#         },
#         {
#             'time': datetime.datetime.fromisoformat("2021-03-08 14:00:00"),
#             'price': 485
#         }
#     ]
# )
# 观察的上一个结果填充
# collection_name = "restaurantReviews"
# db[collection_name].insert_many(
#     [
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-08"),
#             'score': 90
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-09"),
#             'score': 92
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-10")
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-11")
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-12"),
#             'score': 85
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-13")
#         }
#     ]
# )

# 将所要填充的数据进行分区
# collection_name = "restaurantReviewsMultiple"
# db[collection_name].insert_many(
#     [
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-08"),
#             'restaurant': "Joe's Pizza",
#             'score': 90
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-08"),
#             'restaurant': "Sally's Deli",
#             'score': 75
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-09"),
#             'restaurant': "Joe's Pizza",
#             'score': 92
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-09"),
#             'restaurant': "Sally's Deli"
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-10"),
#             'restaurant': "Joe's Pizza"
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-10"),
#             'restaurant': "Sally's Deli",
#             'score': 68
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-11"),
#             'restaurant': "Joe's Pizza",
#             'score': 93
#         },
#         {
#             'date': datetime.datetime.fromisoformat("2021-03-11"),
#             'restaurant': "Sally's Deli"
#         }
#     ]
# )

# $lookup 连接查询
# 等值连接
# collection_name = "orders"
# db[collection_name].insert_many([
#     {"_id": 1, "item": "almonds", "price": 12, "quantity": 2},
#     {"_id": 2, "item": "pecans", "price": 20, "quantity": 1},
#     {"_id": 3}
# ])
# for item in db[collection_name].find():
#     print(item)
#
# collection_name = "inventory"
# db[collection_name].insert_many([
#     {"_id": 1, "sku": "almonds", "description": "product 1", "instock": 120},
#     {"_id": 2, "sku": "bread", "description": "product 2", "instock": 80},
#     {"_id": 3, "sku": "cashews", "description": "product 3", "instock": 60},
#     {"_id": 4, "sku": "pecans", "description": "product 4", "instock": 70},
#     {"_id": 5, "sku": None, "description": "Incomplete"},
#     {"_id": 6}
# ])
# 数组连接
# collection_name = "classes"
# db[collection_name].insert_many([
#     {'_id': 1, 'title': "Reading is ...", 'enrollmentlist': ["giraffe2", "pandabear", "artie"],
#      'days': ["M", "W", "F"]},
#     {'_id': 2, 'title': "But Writing ...", 'enrollmentlist': ["giraffe1", "artie"], 'days': ["T", "F"]}
# ])
# for item in db[collection_name].find():
#     print(item)
# collection_name = "members"
# db[collection_name].insert_many([
#     {'_id': 1, 'name': "artie", 'joined': datetime(2016, 5, 1), 'status': "A"},
#     {'_id': 2, 'name': "giraffe", 'joined': datetime(2017, 5, 1), 'status': "D"},
#     {'_id': 3, 'name': "giraffe1", 'joined': datetime(2017, 10, 1), 'status': "A"},
#     {'_id': 4, 'name': "panda", 'joined': datetime(2018, 10, 11), 'status': "A"},
#     {'_id': 5, 'name': "pandabear", 'joined': datetime(2018, 12, 1), 'status': "A"},
#     {'_id': 6, 'name': "giraffe2", 'joined': datetime(2018, 12, 1), 'status': "D"}
# ])
# for item in db[collection_name].find():
#     print(item)

# $lookup 与 $mergeObjects
# $mergeObjects接受一个列表参数 返回值以列表中后出现的值为主

# collection_name = "orders"
# db[collection_name].insert_many([
#     {"_id": 1, "item": "almonds", "price": 12, "quantity": 2},
#     {"_id": 2, "item": "pecans", "price": 20, "quantity": 1}
# ])
# for item in db[collection_name].find():
#     print(item)
#
# collection_name = "items"
# db[collection_name].insert_many([
#     {"_id": 1, "item": "almonds", 'description': "almond clusters", "instock": 120},
#     {"_id": 2, "item": "bread", 'description': "raisin and nut bread", "instock": 80},
#     {"_id": 3, "item": "pecans", 'description': "candied pecans", "instock": 60}
# ])
# for item in db[collection_name].find():
#     print(item)

# 简洁关联子查询案例
# 1. 判断订单可以从哪个数量足够的仓库发货
# collection_name = "orders"
# db[collection_name].insert_many([
#     {"_id": 1, "item": "almonds", "price": 12, "ordered": 2},
#     {"_id": 2, "item": "pecans", "price": 20, "ordered": 1},
#     {"_id": 3, "item": "cookies", "price": 10, "ordered": 60}
# ])
# for item in db[collection_name].find():
#     print(item)
#
# collection_name = "warehouses"
# db[collection_name].insert_many([
#     {"_id": 1, "stock_item": "almonds", 'warehouse': "A", "instock": 120},
#     {"_id": 2, "stock_item": "pecans", 'warehouse': "A", "instock": 80},
#     {"_id": 3, "stock_item": "almonds", 'warehouse': "B", "instock": 60},
#     {"_id": 4, "stock_item": "cookies", 'warehouse': "B", "instock": 40},
#     {"_id": 5, "stock_item": "cookies", 'warehouse': "A", "instock": 80}
# ])
# for item in db[collection_name].find():
#     print(item)


# 2. 获取员工请假日所在年份的所有节假日
# collection_name = "absences"
# db[collection_name].insert_many([
#     {"_id": 1, "student": "Ann Aardvark", 'sickdays': [datetime.datetime.fromisoformat("2018-05-01"),
#                                                        datetime.datetime.fromisoformat("2018-08-23")]},
#     {"_id": 2, "student": "Zoe Zebra", 'sickdays': [datetime.datetime.fromisoformat("2018-02-01"),
#                                                     datetime.datetime.fromisoformat("2018-05-23")]},
# ])
# for item in db[collection_name].find():
#     print(item)
#
# collection_name = "holidays"
# db[collection_name].insert_many([
#     {"_id": 1, "year": 2018, "name": "New Years", "date": datetime.datetime.fromisoformat("2018-01-01")},
#     {"_id": 2, "year": 2018, "name": "Pi Day", "date": datetime.datetime.fromisoformat("2018-03-14")},
#     {"_id": 3, "year": 2018, "name": "Ice Cream Day", "date": datetime.datetime.fromisoformat("2018-07-15")},
#     {"_id": 4, "year": 2017, "name": "New Years", "date": datetime.datetime.fromisoformat("2017-01-01")},
#     {"_id": 5, "year": 2017, "name": "Ice Cream Day", "date": datetime.datetime.fromisoformat("2017-07-16")}
# ])
# for item in db[collection_name].find():
#     print(item)
