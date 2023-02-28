from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://dajung:sparta@cluster0.nea13z3.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    image = soup.select_one('meta[property="og:image"]')['content']
    title = soup.select_one('meta[property="og:title"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    count = list(db.movie.find({}, {'_id' : False}))
    num = len(count) + 1

    doc= {
        'title' : title,
        'image' : image,
        'desc' : desc,
        'star' : star_receive,
        'comment' : comment_receive,
        'num' : num
    }
    db.moviesf.insert_one(doc)


    return jsonify({'msg':'저장완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    movie_list = list(db.moviesf.find({}, {'_id': False}))
    return jsonify({'movies':movie_list})


@app.route("/movie/delete", methods=['POST'])
def movie_delete():
    num_receive = request.form['num_give']

    db.moviesf.delete_one({"num": int(num_receive)})

    return jsonify({'msg' : 'delete'})

# @app.route('/movie/modify', methods=["POST"])
# def movie_modify():
#     num_receive = request.form['modify_num_give']
#     url_receive = request.form['modify_url_give']
#     # image_receive = request.form['modify_image_give']
#     # desc_receive = request.form['modify_desc_give']
#     star_receive = request.form['modify_star_give']
#     comment_receive = request.form['modify_comment_give']
#     # print(num_receive, url_receive, star_receive, comment_receive)
#     # print(type(num_receive))
#     # print(type(title_receive))
#     # print(type(comment_receive))
#     db.moviesf.update_one({"num": int(num_receive)}, {'$set':{'url': url_receive}})
#     # db.moviesf.update_one({"num": int(num_receive)}, {'$set':{'image': image_receive}})
#     # db.moviesf.update_one({"num": int(num_receive)}, {'$set':{'desc': desc_receive}})
#     db.moviesf.update_one({"num": int(num_receive)}, {'$set':{'star': star_receive}})
#     db.moviesf.update_one({"num": int(num_receive)}, {'$set':{'comment':comment_receive}})
#     return jsonify({'msg': 'modify'})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)