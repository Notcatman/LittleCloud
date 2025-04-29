from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import ItemForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SECRET_KEY'] = 'Keyyf'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'
    
with app.app_context():
    db.create_all()

def index():
    items = Item.query.all()
    return render_template('index.html', items=items)


@app.route("/", methods=["GET", "POST"])
def index():
    form = ItemForm()
    if form.validate_on_submit():
        new_item = Item(name=form.name.data)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for("index"))
    items = Item.query.all()
    return render_template("index.html", form=form, items=items)

@app.route("/delete_all", methods=["POST"])
def delete_all():
    Item.query.delete() 
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=9999)

