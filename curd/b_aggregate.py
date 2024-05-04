import datetime

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
# db_name = 't'
# db = client[db_name]
# collection_name = 'purchaseorders'
# pipeline = [
#     {
#         '$lookup': {
#             'from': 'reportedsales',
#             'let': {
#                 'a_quarter': '$quarter',
#                 'a_region': '$region',
#                 'a_purchase': '$qty'
#             },
#             'as': 'purchased_sales',
#             'pipeline': [
#                 {
#                     '$match': {
#                         '$expr': {
#                             '$and': [
#                                 {'$eq': ['$quarter', '$$a_quarter']},
#                                 {'$eq': ['$region', '$$a_region']}
#                             ]
#                         }
#                     }
#                 },
#                 {
#                     # $replaceWith和$replaceRoot的区别就是replaceRoot需要newRoot参数
#                     '$replaceWith': {
#                         'sales_qty': '$qty'
#                     }
#                 }
#             ]
#         }
#     },
#     {
#         '$set': {
#             'sales_qty': {
#                 '$ifNull': [
#                     {
#                         '$arrayElemAt': ['$purchased_sales', 0]
#                     },
#                     {
#                         'sales_qty': 0
#                     }
#                 ]
#             },
#         }
#     },
#     {
#         '$set': {
#             'sales_qty': '$sales_qty.sales_qty'
#         }
#     },
#     {
#         '$group': {
#             '_id': '$quarter',
#             'purchased_qty': {'$sum': '$qty'},
#             'sales_qty': {'$sum': '$sales_qty'}
#         }
#     },
#     {
#         '$merge': {
#             'into': 'quarterlyreport',
#             'on': '_id',
#             'whenMatched': 'replace',  # 不存在的会添加字段，存在的字段会被替代
#             'whenNotMatched': 'insert'
#         }
#     }
# ]

# 4. 使用自定义管道和自定义变量进行合并
# db_name = 't'
# db = client[db_name]
# collection_name = 'votes'
# pipeline = [
#     {
#         '$match': {
#             'date': datetime.datetime.fromisoformat("2019-05-06"),
#             # '$expr': {
#             #     '$eq': ['$date', datetime.datetime.fromisoformat("2019-05-06")]
#             # }
#         }
#     },
#     {
#         '$project': {
#             '_id': {'$dateToString': {'format': "%Y-%m", 'date': "$date"}},
#             'thumbsup': 1,
#             'thumbsdown': 1
#         }
#     },
#     {
#         '$merge': {
#             'into': 'monthlytotals',
#             'on': '_id',
#             # 和lookup一样let操作的是主表的变量
#             # 管道中要获取定义的变量需要使用$$
#             'let': {
#                 'lastUpdate': datetime.datetime.now()
#             },
#             # 管道操作以从表为主
#             # whenMatched和whenMatched支持一个管道操作
#             # $$new可以获取新插入的值
#             'whenMatched': [
#                 {
#                     '$set': {
#                         'thumbsup': {'$add': ['$thumbsup', '$$new.thumbsup']},
#                         'thumbsdown': {'$add': ['$thumbsdown', '$$new.thumbsdown']},
#                         'lastUpdate': '$$lastUpdate'
#                     }
#                 }
#             ],
#             'whenNotMatched': 'insert'
#         }
#     }
# ]
for item in db[collection_name].aggregate(pipeline):
    print(item)
