from a_mongo import client
db = client.t

print("删除前：")
for item in db.inventory.find(
        {}
):
    print(item)

db.inventory.delete_many(
    {
        # "item": {"$exists": False}
        "item": "123"  # 和查询操作一样，该操作将查询的结果删除
    }
)

print("删除后：")
for item in db.inventory.find(
        {}
):
    print(item)