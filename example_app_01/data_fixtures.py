# -*- coding: utf-8 -*-


from example_app_01 import db
from example_app_01.models import Author, Book, Tag, AVAILABLE_LANGUAGES
import random
import datetime


AUTHORS = (
    ("Grant", "Faultless", "gfaultless@example.com"),
    ("Janet", "Forger", "jforger@example.com"),
    ("Branston", "Oldman", "boldman@example.com"),
    ("Super", "Rude", "srude@example.com"),
    ("Kate", "Ziggy", "kziggy@example.com"),
)

BOOKS = (
    ("Balcony of Bliss", "Three friends attend the symphony over half a century.", 1),
    (
        "Edge Case",
        "What to do when people just starting pressing buttons you didn’t want them to press.",
        2,
    ),
    (
        "Feng Shui Stacks",
        "A renegade staff member welcomes fresh energy into her library by removing all the books.",
        3,
    ),
    ("Getting Meta", "A reflection on forty years of cataloguing.", 4),
    (
        "The Stars Are Beautiful Tonight",
        "A tired system administrator takes stock in the wee hours between starting long-running scripts.",
        2,
    ),
    (
        "Where Is the Virtual Bathroom?",
        "Service provision in 21st-century libraries.",
        4,
    ),
    (
        "Whoops! IT Did It Again",
        "A business analyst tries to stay productive in the public sector.",
        0,
    ),
    (
        "Why #8f8f8f is Nicer than #6f6f6f",
        "The original web developer bad boy pulls no punches in this controversial take on css stylesheets.",
        0,
    ),
)

TAGS = (
    "arid",
    "bold",
    "brooding",
    "comprehensive",
    "droll",
    "exciting",
    "leaden",
    "riotous",
    "scandalous",
    "scintillating",
    "shocking",
    "tense",
    "visionary",
)


def recreate_db():
    """
    Create an empty version of the example_app_01 sqlite database.
    """

    db.drop_all()
    db.create_all()


def add_data_fixtures():
    """
    Populate the example_app_01 sqlite database with some initial sample data.
    """

    author_list = []
    for author in AUTHORS:
        new_author = Author()
        new_author.first_name = author[0]
        new_author.last_name = author[1]
        new_author.email = author[2]
        new_author.website = "https://www.example.com"
        author_list.append(new_author)
        db.session.add(new_author)

    tag_list = []
    for tag in TAGS:
        new_tag = Tag()
        new_tag.name = tag
        tag_list.append(new_tag)
        db.session.add(new_tag)

    for book in BOOKS:
        new_book = Book()
        new_book.title = book[0]
        new_book.description = book[1]
        new_book.language = random.choice(AVAILABLE_LANGUAGES)[0]
        random_no = int(1000 * random.random())
        new_book.publ_date = datetime.datetime.now() - datetime.timedelta(
            days=random_no
        )
        new_book.author = author_list[book[2]]
        new_book.tags = random.sample(tag_list, 3)
        db.session.add(new_book)

    db.session.commit()
    return
