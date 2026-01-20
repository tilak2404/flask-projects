from flask import Blueprint,render_template,url_for,redirect
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprint=Blueprint('owners',__name__,
                            template_folder='templates/owners')

@owners_blueprint.route('/add',methods=['GET','POST'])
def add():
    form=AddForm()

    if form.validate_on_submit():
        name=form.name.data
        id=form.id.data
        owner_n=Owner(name,id)
        db.session.add(owner_n)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('addowner.html',form=form)
