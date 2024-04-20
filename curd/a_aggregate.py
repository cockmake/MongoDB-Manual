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

# 3. $facet 允许在单个聚合阶段中执行多个独立的聚合操作对每个字段单独进行声明
# collection_name = "artwork"
# pipeline = [
#     {
#         '$facet': {
#             "price": [
#                 # 通道操作
#                 {
#                     '$bucket': {
#                         'groupBy': '$price',
#                         'boundaries': [0, 200, 400],
#                         'default': 'Other',
#                         'output': {
#                             'number': {'$sum': 1},
#                             'artwork': {
#                                 '$push': {'title': '$title', 'price': '$price'}
#                             },
#                             'averagePrice': {'$avg': '$price'},
#                         }
#                     },
#                 },
#             ],
#             "year": [
#                 # 通道操作
#                 {
#                     '$bucket': {
#                         'groupBy': '$year',
#                         'boundaries': [1890, 1910, 1920, 1940],
#                         'default': 'unknown',
#                         'output': {
#                             'count': {'$sum': 1},
#                             'artwork': {
#                                 '$push': {
#                                     'artist': '$artist',
#                                     'title': '$title', 'year': '$year'
#                                 }
#                             }
#                         }
#                     }
#                 }
#             ]
#         }
#     }
# ]

# 4. $count结果数量统计，一般用于统计上个文档流的数量与{$sum: 1}的筛选然后累加不一样
# collection_name = "scores"
# pipeline = [
#     {
#         '$match': {
#             'score': {'$gte': 80},
#         }
#     },
#     {
#         '$count': 'passing_score'  # 不能直接使用len的原因是mongodb的结果在需要的时候才加入内存中
#     }
# ]


# 5. $fill 填充文档中的 null 和缺失的字段值
# 5.1 填充常量
# collection_name = "dailySales"
# pipeline = [
#     {
#         '$fill': {
#             'output': {
#                 "bootsSold": {'value': 0},  # value是表达式 如果该字段没有值就用表达式的结果进行填充
#                 "sandalsSold": {'value': 0},
#                 "sneakersSold": {'value': 0}
#             }
#         }
#     }
# ]
# 5.2 linear 线性填充 需要对填充的字段进行排序
# collection_name = "stock"
# pipeline = [
#     {
#         '$fill': {
#             'sortBy': {'time': -1},
#             'output': {
#                 "price": {'method': "linear"}
#             }
#         }
#     }
# ]
# 5.3 locf 代表观察的上一个结果 需要对填充的字段进行排序
# collection_name = "restaurantReviews"
# pipeline = [
#     {
#         '$fill': {
#             'sortBy': {'date': 1},
#             'output': {
#                 'score': {'method': 'locf'}
#             }
#         }
#     }
# ]
# 5.4 将数据进行分区然后再执行填充方法
collection_name = "restaurantReviewsMultiple"
pipeline = [
    {
        '$fill': {
            'sortBy': {'date': 1},
            'partitionBy': {'restaurant': "$restaurant"},  # 根据表达式结果分组
            # 'partitionByFields': ['restaurant'],  # 根据字段来分组
            'output': {
                'score': {'method': 'locf'}
                # locf在上一个为空的时候当前这个值也会为空
                # linear在只有一个值的时候无法进行插值计算

            }
        }
    }
]
# 5.5区分是插入值还是原始值
# 可以在$fill操作之前使用$set为文档添加额外的字段
# collection_name = "restaurantReviews"
# pipeline = [
#     {
#         '$set': {
#             'fieldExistsFlag': {
#                 # 方法一
#                 '$ne': [{'$type': '$score'}, 'missing']  # 不 缺失的值就是True
#                 # 方法二
#                 # '$ifNull': [
#                 #     {'$toBool': {'$toString': '$score'}},  # 防止把数值0转换为False所以使用了toString
#                 #     False
#                 # ]
#                 # ifNull如果存在就返回第一个参数对应的值，None或者不存在就返回第二个参数
#
#             }
#         }
#     }
# ]
result = db[collection_name].aggregate(pipeline)
for item in result:
    print(item)
