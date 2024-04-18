from a_mongo import client

db = client.t

# 1. 按照名称分组并计算每个名称的订单总数
# collection_name = "orders"
# pipeline = [
#     # Filter pizza order documents by pizza size
#     {
#         "$match": {'size': 'medium'},
#     },
#     # Group remaining documents by pizza name and calculate total quantity
#     {
#         '$group': {'_id': '$name', 'totalQuantity': {'$sum': '$quantity'}}
#     }
# ]
# 2.计算订单总值和平均订单数量
# pipeline = [
#     {
#         '$match':
#             {'date': {'$gte': datetime.datetime(2020, 1, 30), '$lte': datetime.datetime(2022, 1, 30)}}
#     },
#     {
#         '$group':
#             {
#                 '_id': {'$dateToString': {'format': '%Y-%m-%d', 'date': '$date'}},
#                 'total_order_value': {'$sum': {'$multiply': ['$price', '$quantity']}},
#                 'average_order_quantity': {'$avg': '$quantity'}
#             }
#     },
#     {
#         '$sort': {'totalOrderValue': -1}
#     }
# ]

# 通道操作带有自动优化具体就是在$match操作会被拆分，然后放在可能得操作之前
# 核心思想是让流过管道的文档数量尽可能的少

# 1. $set | $addFields | $project 字段
# $set alias $addFields
# 现有字段会被覆盖
# $concatArrays 数组连接函数

# collection_name = "scores"
# pipeline = [
#     {
#         '$addFields': {
#             'totalHomework': {
#                 '$sum':
#                     {'$concatArrays': ['$homework', [20, 20], [50]]}
#             },
#             'totalQuiz': {'$sum': '$quiz'}
#         }
#     },
#     {
#         '$set': {
#             'totalScore': {'$add': ['$totalHomework', '$totalQuiz', '$extraCredit']}
#         }
#     },
#     {
#         '$project': {
#             'homework': 0,
#             'quiz': 0,
#             'extraCredit': 0
#         }
#     }
# ]

# 2. $bucket
# 参数 groupBy, boundaries, default, output
# collection_name = "artists"
# pipeline = [
#     {
#         '$bucket': {
#             'groupBy': "$year_born",  # Field to group by
#             'boundaries': [1840, 1850, 1860, 1870, 1880],  # Boundaries for the buckets
#             'default': 'Other',  # Bucket ID for documents which do not fall into a bucket
#             'output': {
#                 'count': {'$sum': 1},  # {'$sum': 1}将该字段声明为自动字段
#                 'artists': {
#                     '$push': {
#                         'name': {'$concat': ['$first_name', "·", '$last_name']},
#                         'year_born': "$year_born"
#                     }
#                 }
#             }
#
#         }
#     },
#     {
#         '$match': {
#             'count': {'$gte': 2}
#         }
#     }
# ]

# $facet 允许在单个聚合阶段中执行多个独立的聚合操作对每个字段单独进行声明
collection_name = "artwork"
pipeline = [
    {
        '$facet': {
            "price": [
                # 通道操作
                {
                    '$bucket': {
                        'groupBy': '$price',
                        'boundaries': [0, 200, 400],
                        'default': 'Other',
                        'output': {
                            'number': {'$sum': 1},
                            'artwork': {
                                '$push': {'title': '$title', 'price': '$price'}
                            },
                            'averagePrice': {'$avg': '$price'}
                        }
                    }
                }
            ],
            "year": [
                # 通道操作
                {
                    '$bucket': {
                        'groupBy': '$year',
                        'boundaries': [1890, 1910, 1920, 1940],
                        'default': 'unknown',
                        'output': {
                            'count': {'$sum': 1},
                            'artwork': {
                                '$push': {
                                    'artist': '$artist',
                                    'title': '$title', 'year': '$year'
                                }
                            }
                        }
                    }
                }
            ]
        }
    }
]
for item in db[collection_name].aggregate(pipeline):
    print(item)
