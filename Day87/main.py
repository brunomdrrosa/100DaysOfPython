from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL1', "sqlite:///cafes.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.VARCHAR(250), unique=True, nullable=False)
    map_url = db.Column(db.VARCHAR(500), nullable=False)
    img_url = db.Column(db.VARCHAR(500), nullable=False)
    location = db.Column(db.VARCHAR(500), nullable=False)
    has_sockets = db.Column(db.BOOLEAN, nullable=False)
    has_toilet = db.Column(db.BOOLEAN, nullable=False)
    has_wifi = db.Column(db.BOOLEAN, nullable=False)
    can_take_calls = db.Column(db.BOOLEAN, nullable=False)
    seats = db.Column(db.VARCHAR(250), nullable=False)
    coffee_price = db.Column(db.VARCHAR(250), nullable=False)


# db.create_all()


@app.route("/")
def home():
    all_cafes = Cafe.query.order_by(Cafe.id).all()
    for i in range(len(all_cafes)):
        all_cafes[i].ranking = len(all_cafes) - i
    db.session.commit()

    counter = 0
    cafes_to_append = []
    all_cafes_three_list = []
    # create lists of three cafes inside a big list:
    for _ in all_cafes:
        cafes_to_append.append(all_cafes[counter])
        counter += 1
        if len(cafes_to_append) % 3 != 0:
            continue
        else:
            all_cafes_three_list.append(cafes_to_append)
            cafes_to_append = []
    # if there are leftovers in cafes_to_append, add them to the list as well:
    if len(cafes_to_append) > 0:
        all_cafes_three_list.append(cafes_to_append)
    return render_template("index.html", all_cafes=all_cafes_three_list)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == 'POST':
        cafe_name = request.form['name']
        map_url = request.form['map_url']
        img_url = request.form['img_url']
        location = request.form['location']
        has_sockets = int(request.form['has_sockets'])
        has_toilet = int(request.form['has_toilet'])
        has_wifi = int(request.form['has_wifi'])
        can_take_calls = int(request.form['can_take_calls'])
        seats = request.form['seats']
        coffee_price = request.form['coffee_price']

        new_cafe = Cafe(name=cafe_name,
                        map_url=map_url,
                        img_url=img_url,
                        location=location,
                        has_sockets=has_sockets,
                        has_toilet=has_toilet,
                        has_wifi=has_wifi,
                        can_take_calls=can_take_calls,
                        seats=seats,
                        coffee_price=coffee_price)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_cafe.html")


@app.route("/delete")
def delete():
    cafe_id = request.args.get('id')
    cafe = Cafe.query.get(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect('/#coffee-shops')


if __name__ == '__main__':
    app.run()