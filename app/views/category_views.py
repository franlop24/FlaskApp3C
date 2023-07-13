from flask import Blueprint, render_template, redirect, url_for

from models.categories import Category

from forms.category_forms import CreateCategory

category_views = Blueprint('category', __name__)

@category_views.route('/categories/')
def categories():
    cats = Category.get_all()
    return render_template('category/categories.html',
                           cats=cats)

@category_views.route('/categories/create/', methods=('GET', 'POST'))
def create_cat():
    form = CreateCategory()
    if form.validate_on_submit():
        category = form.category.data
        description = form.description.data
        cat = Category(category, description)
        cat.save()
        return redirect(url_for('category.categories'))
    return render_template('category/create_cat.html', form=form)

@category_views.route('/categories/<int:id>/update/', methods=('GET', 'POST'))
def update_cat(id):
    return f"Vamos a editar con id { id }"

@category_views.route('/categories/<int:id>/delete/', methods=('POST',))
def delete_cat(id):
    cat = Category.get(id)
    cat.delete()
    return redirect(url_for('category.categories'))