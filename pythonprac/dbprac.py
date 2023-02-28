from pymongo import MongoClient
client = MongoClient('mongodb+srv://dajung:sparta@cluster0.nea13z3.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))
# 0번째 결과값의 'name'을 보기
print(all_users[0]['name'])
# 반복문을 돌며 모든 결과값을 보기
for user in all_users:
    print(user)

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})