# -*- coding: utf-8 -*-


from example_app_01 import app, db
from example_app_01.models import AVAILABLE_LANGUAGES, Author, Book, Tag

from wtforms import validators

import flask_admin as admin
from flask_admin.base import MenuLink
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters


class AuthorAdmin(sqla.ModelView):
    """The representation of the Author model in the Admin."""

    column_list = [
        "first_name",
        "last_name",
        "email",
        "website",
    ]
    column_searchable_list = [
        "first_name",
        "last_name",
        "email",
    ]
    column_default_sort = [
        ("last_name", False),
        ("first_name", False),
    ]


class BookAdmin(sqla.ModelView):
    """The representation of the Book model in the Admin."""

    form_choices = {
        "language": AVAILABLE_LANGUAGES,
    }
    form_widget_args = {"id": {"readonly": True}}
    action_disallowed_list = [
        "delete",
    ]
    can_view_details = True
    column_display_pk = True
    column_list = [
        "id",
        "author",
        "title",
        "publ_date",
        "language",
        "tags",
        "record_created",
        "record_modified",
    ]
    column_details_list = [
        "id",
        "author",
        "title",
        "publ_date",
        "description",
        "language",
        "tags",
        "record_created",
        "record_modified",
    ]
    column_default_sort = ("publ_date", True)
    column_editable_list = ["language"]
    column_sortable_list = [
        "id",
        "title",
        "publ_date",
        ("author", ("author.last_name", "author.first_name"),),
    ]
    column_searchable_list = [
        "title",
        "tags.name",
        "author.first_name",
        "author.last_name",
    ]
    column_labels = {
        "title": "Title",
        "publ_date": "Publication Date",
        "tags.name": "Tags",
        "author.first_name": "Author's first name",
        "author.last_name": "Last name",
    }
    column_filters = [
        "author.last_name",
        "record_created",
        "record_modified",
        "title",
        "publ_date",
        "tags",
        filters.FilterLike(
            Book.title,
            "Common Title Words",
            options=(("library", "Library"), ("service", "Service")),
        ),
    ]
    can_export = True
    export_max_rows = 1000
    export_types = ["csv", "ods", "xlsx"]
    create_modal = True
    edit_modal = True
    form_columns = [
        "id",
        "author",
        "title",
        "publ_date",
        "description",
        "language",
        "tags",
        "record_created",
        "record_modified",
    ]
    form_args = {
        "description": dict(
            label="Book Description", validators=[validators.DataRequired()]
        )
    }
    form_widget_args = {"description": {"rows": 5}}

    form_ajax_refs = {
        "author": {"fields": (Author.first_name, Author.last_name)},
        "tags": {
            "fields": (Tag.name,),
            "minimum_input_length": 0,
            "placeholder": "Please select",
            "page_size": 5,
        },
    }

    def __init__(self, session):
        super(BookAdmin, self).__init__(Book, session)


admin = admin.Admin(
    app, name="Desktop Database Application", template_mode="bootstrap3"
)
admin.add_view(AuthorAdmin(Author, db.session))
admin.add_view(BookAdmin(db.session))
admin.add_view(sqla.ModelView(Tag, db.session))
admin.add_sub_category(name="Links", parent_name="Other")
admin.add_link(MenuLink(name="Admin Home", url="/admin", category="Links"))
admin.add_link(
    MenuLink(
        name="Library and Archives Canada",
        url="https://www.bac-lac.gc.ca/eng/Pages/home.aspx",
        category="Links",
    )
)
admin.add_link(
    MenuLink(name="Library of Congress", url="https://loc.gov/", category="Links")
)
