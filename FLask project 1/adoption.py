import os
from forms import AddForm,DelForm,AddOwner
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)

app.config['SECRET_KEY']="mysecretkey"

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
app.db=db
Migrate(app,db)

####
class Puppy(db.Model):
    __tablename__='puppies'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    owner=db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f" Puppy name is {self.name}"
class Owner(db.Model):
    __tablename__='owners'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    puppy_id=db.Column(db.Integer,db.ForeignKey('puppies.id'))
    def __init__(self,name,puppy_id):
        self.name=name
        self.puppy_id=puppy_id
    def __repr__(self):
        return f" {self.name} is assigned to {self.puppy_id}"
    
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/addpuppy',methods=['GET','POST'])
def add_pup():
    form=AddForm()
    
    if form.validate_on_submit():
        name=form.name.data
        new_pup=Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('add.html',form=form)
@app.route('/list')
def list_pup():
    puppies=Puppy.query.all()
    owners=Owner.query.all()
    return render_template('list.html',puppies=puppies,owners=owners)

@app.route('/delpuppy',methods=['GET','POST'])
def del_pup():
    form=DelForm()
    if form.validate_on_submit():
        id=form.id.data
        pup=db.session.get(Puppy,id)
        if pup:
            db.session.delete(pup)
            db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form)

@app.route('/owner',methods=['GET','POST'])
def add_owner():
    form=AddOwner()

    if form.validate_on_submit():
        name=form.name.data
        id=form.id.data
        owner_n=Owner(name,id)
        db.session.add(owner_n)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('addowner.html',form=form)

if __name__=='__main__':
    app.run(debug='True')



