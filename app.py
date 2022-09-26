from flask import Flask, render_template, request, redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap




app = Flask(__name__)

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'MLXH243GssUWwKdTWS7FDhdwYF56wPj8'


# Flask-Bootstrap requires this line
Bootstrap(app)

# the name of the database; add path if necessary
db_name = 'pizza.db'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://edgsqtentxumxq:5a8815f18889fcbd5c6755b4a6269ae826215773abb8940af9de4f684a12e371@ec2-34-228-100-83.compute-1.amazonaws.com:5432/d20c58lko8m93n' #set databse URI at sqlite  #'sqlite:///site.db' # 


# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)



class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topping = db.Column(db.String)
    description = db.Column(db.String)


    def __init__(self,topping,description):
        self.topping = topping
        self.description = description


class Entry2(db.Model):
    id2 = db.Column(db.Integer, primary_key=True)
    pizza = db.Column(db.String)
    topping2 = db.Column(db.String)
    topping3 = db.Column(db.String)
    topping4 = db.Column(db.String)
    topping5 = db.Column(db.String)


    def __init__(self,pizza,topping2,topping3,topping4,topping5):
        self.pizza=pizza
        self.topping2 = topping2
        self.topping3 = topping3
        self.topping4 = topping4
        self.topping5 = topping5


# +++++++++++++++++++++++
# routes

@app.route('/')
def index():

    entries2 = [
        {
            'id': 1,
            'pizza': 'test title 1',
            'topping': 'test desc 1'
        }

    ]
    entries = Entry.query.all()
    entries2 = Entry2.query.all()
    message=""
    return render_template('index.html', entries=entries,entries2=entries2,message=message)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        topping = form.get('topping')
        description = form.get('description')
        if not topping or description:
            findrepeat = Entry.query.filter_by(topping=topping.lower()).all()

            if not findrepeat:
                entry = Entry(topping = topping.lower(), description = description)
                db.session.add(entry)
                db.session.commit()

            else:
                flash("Error: the topping is exist in the system")
            return redirect('/')

    return



@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            return render_template('update.html', entry=entry)

    return

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            form = request.form
            topping = form.get('topping')
            description = form.get('description')

            findrepeat = Entry.query.filter_by(topping=topping.lower()).all()

            if not findrepeat:
                entry.topping = topping.lower()
                entry.description = description
                db.session.commit()
            else:
                flash("Error: the pizza is exist in the system")


        return redirect('/')

    return



@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return





@app.route('/add2', methods=['Get','POST'])
def add2():
    if request.method == 'POST':
        form = request.form
        pizza = form.get('pizza')
        topping2 = form.get('topping2')
        topping3 = form.get('topping3')
        topping4 = form.get('topping4')
        topping5 = form.get('topping5')
        if not pizza or topping2:
            findrepeat = Entry2.query.filter_by(pizza=pizza.lower()).all()

            if not findrepeat :
                entry2 = Entry2(pizza.lower(), topping2,topping3,topping4,topping5)
                db.session.add(entry2)
                db.session.commit()
            else:
                flash("Error: the pizza is exist in the system")
            return redirect('/')

    return




@app.route('/update2/<int:id>')
def updateRoute2(id):
    if not id or id != 0:
        entry2 = Entry2.query.get(id)
        if entry2:
            return render_template('update2.html', entry2=entry2)

    return


@app.route('/update2/<int:id>', methods=['POST'])
def update2(id):
    if not id or id != 0:
        entry2 = Entry2.query.get(id)
        if entry2:
            form = request.form
            pizza = form.get('pizza')
            topping2 = form.get('topping2')
            topping3 = form.get('topping3')
            topping4 = form.get('topping4')
            topping5 = form.get('topping5')

            findrepeat = Entry2.query.filter_by(pizza=pizza.lower()).all()

            if not findrepeat:
                entry2.pizza = pizza.lower()
                entry2.topping2 = topping2.lower()
                entry2.topping3 = topping3.lower()
                entry2.topping4 = topping4.lower()
                entry2.topping5 = topping5.lower()
                db.session.commit()
            else:
                flash("Error: the pizza is exist in the system")

        return redirect('/')

    return


@app.route('/delete2/<int:id>')
def delete2(id):
    if not id or id != 0:
        entry = Entry2.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return


if __name__ == '__main__':
    #db.create_all()
    # entry = Entry("testing", "testing")
    # db.session.add(entry)
    # db.session.commit()
    # entry2 = Entry2("testing2","testing2")
    # db.session.add(entry2)
    # db.session.commit()

    app.run(host='127.0.0.1',port=8003)
