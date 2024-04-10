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

# 管道聚合更新

# db.students.insert_many(
#     [
#         {"_id": 1, "tests": {"yw": 90, "sx": 90, "yy": 90}, "modified": "2019-01-01T00:00:00Z"},
#         {"_id": 2, "tests": {"yw": 85, "sx": 88, "yy": 90}, "modified": "2019-01-01T00:00:00Z"},
#         {"_id": 3, "tests": {"yw": 88, "sx": 85, "yy": 90}, "modified": "2019-01-01T00:00:00Z"},
#         {"_id": 4, "tests": {"yw": 87, "sx": 87, "yy": 90}, "modified": "2019-01-01T00:00:00Z"},
#         {"_id": 5, "tests": {"yw": 86, "sx": 86, "yy": 90}, "modified": "2019-01-01T00:00:00Z"},
#     ]
# )

for item in db.students.find():
    print(item)
