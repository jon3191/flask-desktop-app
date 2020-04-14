# -*- coding: utf-8 -*-


from datetime import datetime
from example_app_01 import db
from sqlalchemy_utils import ArrowType, ChoiceType, EmailType, URLType


AVAILABLE_LANGUAGES = [
    ("english", "English"),
    ("french", "French"),
    ("german", "German"),
    ("latin", "Latin"),
]


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(EmailType, unique=True, nullable=False)
    website = db.Column(URLType)
    books = db.relationship("Book", cascade="save-update, merge, delete")

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


book_tags_table = db.Table(
    "book_tags",
    db.Model.metadata,
    db.Column("book_id", db.Integer, db.ForeignKey("book.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    language = db.Column(ChoiceType(AVAILABLE_LANGUAGES), nullable=True)
    publ_date = db.Column(db.Date)
    record_created = db.Column(ArrowType, default=datetime.utcnow())
    record_modified = db.Column(
        ArrowType, default=datetime.utcnow(), onupdate=datetime.utcnow
    )
    author_id = db.Column(
        db.Integer, db.ForeignKey("author.id", ondelete="CASCADE"), nullable=False
    )
    author = db.relationship("Author", foreign_keys=[author_id])
    tags = db.relationship("Tag", secondary=book_tags_table)

    def __str__(self):
        return "{}".format(self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __str__(self):
        return "{}".format(self.name)
