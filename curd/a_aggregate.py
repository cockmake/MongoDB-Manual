from a_mongo import client
db = client.t
import datetime
# 聚合操作处理多个文档并返回计算结果。
collection_name = "orders"

# 例子
# 1. 按照名称分组并计算每个名称的订单总数
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


for item in db[collection_name].aggregate(pipeline):
    print(item)