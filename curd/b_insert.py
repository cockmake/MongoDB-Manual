from a_mongo import client
from bson import ObjectId
from collections import OrderedDict
from datetime import datetime
# 7. merge 聚合
# 1.
# db_name = 'zoo'
# db = client[db_name]
# collection_name = 'salaries'
# db[collection_name].insert_many([
#     {"_id": 1, "employee": "Ant", "dept": "A", "salary": 100000, "fiscal_year": 2017},
#     {"_id": 2, "employee": "Bee", "dept": "A", "salary": 120000, "fiscal_year": 2017},
#     {"_id": 3, "employee": "Cat", "dept": "Z", "salary": 115000, "fiscal_year": 2017},
#     {"_id": 4, "employee": "Ant", "dept": "A", "salary": 115000, "fiscal_year": 2018},
#     {"_id": 5, "employee": "Bee", "dept": "Z", "salary": 145000, "fiscal_year": 2018},
#     {"_id": 6, "employee": "Cat", "dept": "Z", "salary": 135000, "fiscal_year": 2018},
#     {"_id": 7, "employee": "Gecko", "dept": "A", "salary": 100000, "fiscal_year": 2018},
#     {"_id": 8, "employee": "Ant", "dept": "A", "salary": 125000, "fiscal_year": 2019},
#     {"_id": 9, "employee": "Bee", "dept": "Z", "salary": 160000, "fiscal_year": 2019},
#     {"_id": 10, "employee": "Cat", "dept": "Z", "salary": 150000, "fiscal_year": 2019}
# ])

# 2.
# db_name = 'zoo'
# db = client[db_name]
# collection_name = 'salaries'
# db[collection_name].insert_many([
#     {"_id": 11, "employee": "Wren", "dept": "Z", "salary": 100000, "fiscal_year": 2019},
#     {"_id": 12, "employee": "Zebra", "dept": "A", "salary": 150000, "fiscal_year": 2019},
#     {"_id": 13, "employee": "headcount1", "dept": "Z", "salary": 120000, "fiscal_year": 2020},
#     {"_id": 14, "employee": "headcount2", "dept": "Z", "salary": 120000, "fiscal_year": 2020}
# ])

# 3. 仅插入新数据
# db_name = 'reporting'
# db = client[db_name]
# collection_name = 'orgArchive'
# db[collection_name].insert_many([
#     {"_id": ObjectId("5cd8c68261baa09e9f3622be"), "employees": ["Ant", "Gecko"], "dept": "A", "fiscal_year": 2018},
#     {"_id": ObjectId("5cd8c68261baa09e9f3622bf"), "employees": ["Ant", "Bee"], "dept": "A", "fiscal_year": 2017},
#     {"_id": ObjectId("5cd8c68261baa09e9f3622c0"), "employees": ["Bee", "Cat"], "dept": "Z", "fiscal_year": 2018},
#     {"_id": ObjectId("5cd8c68261baa09e9f3622c1"), "employees": ["Cat"], "dept": "Z", "fiscal_year": 2017}
# ])
# db[collection_name].create_index(
#     {
#         'dept': 1,
#         'fiscal_year': 1
#     },
#     unique=True
# )


# 4. 合并多个集合的结果
# db_name = 't'
# db = client[db_name]
# collection_name = 'purchaseorders'
# db[collection_name].insert_many([
#     {"_id": 1, "quarter": "2019Q1", "region": "A", "qty": 200, "reportDate": datetime.fromisoformat("2019-04-01")},
#     {"_id": 2, "quarter": "2019Q1", "region": "B", "qty": 300, "reportDate": datetime.fromisoformat("2019-04-01")},
#     {"_id": 3, "quarter": "2019Q1", "region": "C", "qty": 700, "reportDate": datetime.fromisoformat("2019-04-01")},
#     {"_id": 4, "quarter": "2019Q2", "region": "B", "qty": 300, "reportDate": datetime.fromisoformat("2019-07-01")},
#     {"_id": 5, "quarter": "2019Q2", "region": "C", "qty": 1000, "reportDate": datetime.fromisoformat("2019-07-01")},
#     {"_id": 6, "quarter": "2019Q2", "region": "A", "qty": 400, "reportDate": datetime.fromisoformat("2019-07-01")},
# ])
# db[collection_name].create_index(
#     OrderedDict({
#         'quarter': 1,
#         'region': 1
#     }),
#     unique=True
# )
# collection_name = 'reportedsales'
# db[collection_name].insert_many([
#     {"_id": 1, "quarter": "2019Q1", "region": "A", "qty": 400, "reportDate": datetime.fromisoformat("2019-04-02")},
#     {"_id": 2, "quarter": "2019Q1", "region": "B", "qty": 550, "reportDate": datetime.fromisoformat("2019-04-02")},
#     {"_id": 3, "quarter": "2019Q1", "region": "C", "qty": 1000, "reportDate": datetime.fromisoformat("2019-04-05")},
#     {"_id": 4, "quarter": "2019Q2", "region": "B", "qty": 500, "reportDate": datetime.fromisoformat("2019-07-02")},
# ])

# 4. 使用自定义管道和自定义变量进行合并
# db_name = 't'
# db = client[db_name]
# collection_name = 'votes'
# db[collection_name].insert_many([
#     {"date": datetime.fromisoformat("2019-05-01"), "thumbsup": 1, "thumbsdown": 1},
#     {"date": datetime.fromisoformat("2019-05-02"), "thumbsup": 3, "thumbsdown": 1},
#     {"date": datetime.fromisoformat("2019-05-03"), "thumbsup": 1, "thumbsdown": 1},
#     {"date": datetime.fromisoformat("2019-05-04"), "thumbsup": 2, "thumbsdown": 2},
#     {"date": datetime.fromisoformat("2019-05-05"), "thumbsup": 6, "thumbsdown": 10},
#     {"date": datetime.fromisoformat("2019-05-06"), "thumbsup": 13, "thumbsdown": 16}
# ])
# collection_name = 'monthlytotals'
# db[collection_name].insert_one(
#     {"_id": "2019-05", "thumbsup": 0, "thumbsdown": 0}
# )

# 8. redact 聚合
# 1.
# $PRUNE $DESCEND $KEEP
# db_name = 't'
# db = client[db_name]
# collection_name = 'forecasts'
# db[collection_name].insert_one(
#     {
#         "_id": 1,
#         "title": "123 Department Report",
#         "tags": ["G", "STLW"],
#         "year": 2014,
#         "subsections": [
#             {
#                 "subtitle": "Section 1: Overview",
#                 "tags": ["SI", "G"],
#                 "content": "Section 1: This is the content of section 1."
#             },
#             {
#                 "subtitle": "Section 2: Analysis",
#                 "tags": ["STLW"],
#                 "content": "Section 2: This is the content of section 2."
#             },
#             {
#                 "subtitle": "Section 3: Budgeting",
#                 "tags": ["TK"],
#                 "content": {
#                     "text": "Section 3: This is the content of section 3.",
#                     "tags": ["HCS"]
#                 }
#             }
#         ]
#     }
# )
# 2.
# db_name = 't'
# db = client[db_name]
# collection_name = 'accounts'
# db[collection_name].insert_one(
#     {
#         "_id": 1,
#         "level": 1,
#         "acct_id": "xyz123",
#         "cc": {
#             "level": 5,
#             "type": "yy",
#             "num": 000000000000,
#             "exp_date": datetime.fromisoformat("2015-11-01T00:00:00.000Z"),
#             "billing_addr": {
#                 "level": 5,
#                 "addr1": "123 ABC Street",
#                 "city": "Some City"
#             },
#             "shipping_addr": [
#                 {
#                     "level": 3,
#                     "addr1": "987 XYZ Ave",
#                     "city": "Some City"
#                 },
#                 {
#                     "level": 3,
#                     "addr1": "PO Box 0123",
#                     "city": "Some City"
#                 }
#             ]
#         },
#         "status": "A"
#     }
# )
# for item in db[collection_name].find():
#     print(item)
