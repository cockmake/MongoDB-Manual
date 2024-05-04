from a_mongo import client

# 7. merge 聚合
# 1.
# db_name = 'zoo'
# db = client[db_name]
# collection_name = 'salaries'
# pipeline = [
#     {
#         '$group': {
#             '_id': {
#                 'fiscal_year': '$fiscal_year',
#                 'dept': '$dept'
#             },
#             'salaries': {'$sum': '$salary'}
#         }
#     },
#     {
#         '$merge': {
#             'into': {
#                 'db': 'reporting',
#                 'coll': 'budgets'
#             },
#             'on': '_id',
#             'whenMatched': 'replace',
#             'whenNotMatched': 'insert'
#         }
#     }
# ]

# 2.
# db_name = 'zoo'
# db = client[db_name]
# collection_name = 'salaries'
# pipeline = [
#     {
#         '$match': {
#             'fiscal_year': {'$gte': 2019}
#         },
#     },
#     {
#         '$group': {
#             '_id': {
#                 'fiscal_year': '$fiscal_year',
#                 'dept': '$dept'
#             },
#             'salaries': {'$sum': '$salary'},
#         },
#     },
#     {
#         '$merge': {
#             'into': {
#                 'db': 'reporting',
#                 'coll': 'budgets'
#             },
#             'on': '_id',
#             'whenMatched': 'replace',
#             'whenNotMatched': 'insert'
#         }
#     }
# ]

# 3. 仅插入新数据
# db_name = 'zoo'
# db = client[db_name]
# collection_name = 'salaries'
# pipeline = [
#     {
#         '$match': {
#             'fiscal_year': {'$gte': 2019}
#         }
#     },
#     {
#         '$group': {
#             '_id': {
#                 'fiscal_year': '$fiscal_year',
#                 'dept': '$dept'
#             },
#             'employees': {'$push': '$employee'}
#         }
#     },
#     {
#         '$project': {
#             'dept': '$_id.dept',
#             'fiscal_year': '$_id.fiscal_year',
#             '_id': 0,
#             'employees': 1
#         }
#     },
#     {
#         '$merge': {
#             'into': {
#                 'db': 'reporting',
#                 'coll': 'orgArchive'
#             },
#             'on': ['dept', 'fiscal_year'],
#             'whenMatched': 'keepExisting',
#             # 'fail' 会失败并进行回滚
#             # 'replace' 会执行替换操作不会报错
#             'whenNotMatched': 'insert'
#         }
#     }
# ]

# 4. 合并多个集合的结果
# 方法一：使用merge
# 需要多次合并到同一个文档中
# db_name = 't'
# db = client[db_name]
# collection_name = 'purchaseorders'
# pipeline = [
#     {
#         '$group': {
#             '_id': '$quarter',
#             'purchased': {'$sum': '$qty'}
#         }
#     },
#     {
#         '$merge': {
#             'into': 'quarterlyreport',
#             'on': '_id',
#             'whenMatched': 'merge',  # 会添加字段
#             'whenNotMatched': 'insert'
#         }
#     }
# ]
# db[collection_name].aggregate(pipeline)
# collection_name = 'reportedsales'
# pipeline = [
#     {
#         '$group': {
#             '_id': '$quarter',
#             'sales': {'$sum': '$qty'}
#         }
#     },
#     {
#         '$merge': {
#             'into': 'quarterlyreport',
#             'on': '_id',
#             'whenMatched': 'merge',  # 不存在的会添加字段，存在的字段会被替代
#             'whenNotMatched': 'insert'
#         }
#     }
# ]
# db[collection_name].aggregate(pipeline)
# for item in db['quarterlyreport'].find():
#     print(item)

# 方法二：使用lookup
