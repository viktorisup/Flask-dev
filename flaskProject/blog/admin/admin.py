from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from blog import models
from blog.models.database import db


class CustomAdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))


class CustomAdminIndexView(AdminIndexView):

    @expose()
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for('auth.login'))
        return super().index()


admin = Admin(index_view=CustomAdminIndexView(), name='Blog Admin Panel', template_mode='bootstrap4')


class TagAdminView(CustomAdminView):
    column_searchable_list = ('name', )
    column_list = ('name', 'articles', )
    create_modal = True
    edit_modal = True


class ArticleAdminView(CustomAdminView):
    column_list = ('id', 'author', 'title', 'text', 'created_at', 'updated_at', 'tags')
    form_columns = ('author', 'title', 'text', 'created_at', 'updated_at', 'tags')
    can_export = True
    column_filters = ('author_id',)
    export_types = ('csv', 'xlsx')


class UserAdminView(CustomAdminView):
    column_exclude_list = ('password', )
    column_details_exclude_list = ('password', )
    column_export_exclude_list = ('password', )
    form_columns = ('first_name', 'last_name', 'is_staff')
    can_delete = False
    can_create = False
    can_view_details = False
    column_editable_list = ('first_name', 'last_name', 'is_staff', )




admin.add_view(TagAdminView(models.Tag, db.session, category='Models'))
admin.add_view(ArticleAdminView(models.Article, db.session, category='Models'))
admin.add_view(UserAdminView(models.User, db.session, category='Models'))