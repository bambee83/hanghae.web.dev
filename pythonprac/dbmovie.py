from pymongo import MongoClient
client = MongoClient('mongodb+srv://dajung:sparta@cluster0.nea13z3.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

movie = db.movies.find_one({'title':'가버나움'})
star = movie['star']

all_movies = list(db.movies.find({'star':star},{'_id':False}))
for movie in all_movies:
    print(movie['title'])

# db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})


