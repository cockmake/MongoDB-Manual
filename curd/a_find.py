import pymongo

from a_mongo import client

db = client.t
# 查询指定字段

# for item in db.inventory.find(
#         {},  # 条件
#         {
#             "item": 1, "_id": 0, "size.uom": 1,  # 返回的字段 _id默认返回 0代表不返回 1代表返回
#             "instock.warehouse": 1,  # 数组中全部的warehouse字段
#             # "instock": {"$slice": -2},  # 返回数组中的负数就最后x个元素 正数就是前x个元素
#         }
# ):
#     print(item)

# 多条件查询

# for item in db.inventory.find(
#         # {"instock": {"warehouse": "A", "qty": 5}}
#         # {"instock": {"qty": 5, "warehouse": "A"}},  # 不含有$elemMatch的查询 会有顺序要求 所以不会查询到
#
#         # {"instock": {"$elemMatch": {"qty": 5, "warehouse": "A"}}},  # 含有$elemMatch的查询 字段属性无顺序要求

#         # {"instock.qty": {"$lte": 20}}, # 其中有一个元素的qty小于等于20 就可以返回
#         {"instock.0.qty": {"$gte": 10, "$lte": 20}},  # 要求instock数组中第一个元素的qty大于10小于等于20
#         {
#             "_id": 0,
#             "item": 1,
#             "instock": 1
#         }
# ):
#     print(item)

# 数组查询

# for item in db.inventory.find(
#         # {"tags": ["red", "blank"]},  # 查询tags字段中包含red和blank的数组 出现顺序要一致
#         # {"tags": {"$all": ["red", "blank"]}},  # 查询tags字段中包含red和blank的数组 顺序无要求
#
#         # {"dim_cm": {"$gt": 15, "$lt": 20}},  # 查询dim_cm数组字段中有一个元素大于15 另外一个元素（可以是本身）小于20
#         # 即整个数组符合条件有元素符合条件即可
#
#         # {"dim_cm": {"$elemMatch": {"$gt": 15, "$lt": 20}}},  # 查询dim_cm数组字段中有一个元素大于15并且小于20
#         # {"dim_cm.1": {"$gt": 15, "$lt": 20}},  # 查询dim_cm数组字段中第二个元素大于15并且小于20 对于单个元素的而言就是并且
#
#         # {"dim_cm": {"$size": 2}},  # 查询dim_cm数组字段中大于两个元素的数组
#         {"dim_cm": {'$exists': 1}, '$where': 'this.dim_cm.length >= 2'},
#         # 查询dim_cm数组字段存在并且大于等于两个元素的数组 条件判定是要以文档字段存在为基础的
#         {
#             "_id": 0
#         }
# ):
#     print(item)

# 查询空字段或缺少字段

# for it in db.inventory.find(
#         # {"item": None},  # 返回的是item字段为空或者不存在的
#         # {"item": {"$type": 10}}  # 仅返回item字段值为空的文档 type: 10就是代表空值
#
#         # {"item": {"$not": {"$type": 10}}},  # 返回不包含item字段的文档
#         # {"item": {"$exists": False}}  # 返回不包含item字段的文档
# ):
#     print(it)

# 执行文本搜索
collection_name = "stores"
# 首先要构建对某个字段的文本搜索索引

# s = db[collection_name].create_index(
#     {
#         'name': 'text',
#         'desc': 'text'
#     }
# )
# print(s)

for item in db[collection_name].find(
        {'$text': {'$search': 'coffee shop'}},  # 所有包含coffee或shop的文档 不区分大小写
        # {'$text': {'$search': 'java shop -coffee -hut'}},  # 包含java或shop但不包含coffee或hut的
        {'score': {'$meta': 'textScore'}},  # 获取匹配相关系数
).sort('score', -1):  # 按照某个字段排序
    print(item)
