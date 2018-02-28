
import os
from flask import Flask, url_for, redirect, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from DB import object_map, departmentize_db
# from ramsay_util import RamsayEntryModel






sample_entry = {'title': 'Awl', 'description': 'Awls are spiked tools with knob-like handles. These can be used for marking, stitching, or making holes. The tip is pushed into a material and then twisted in order to achieve the desired result.', 'image': 'Awl.jpg', 'materials': 'Illustration', 'dimensions': '', 'distance': '', 'collection': 'Pearson Scott Foresman via Wikimedia Commons', 'link': 'https://commons.wikimedia.org/wiki/File:Awl_2_%28PSF%29.png', 'page': '166', 'department': 'Tool', 'pounds': '6 pence per dozen', 'dollars': '5.6', 'license': 'Public Domain', 'artifact': 'Illustration of an Awl', 'date': '', 'origin': '', 'analytics': 'The databases record six purchases of awls. They were sold by the dozen and their prices range from five to six pence.', 'customer': 'Samuel Smith', 'ledger': 'AwlLedger.jpg', 'unit': '1 dozen', 'author': 'James M. Gaynor and Nancy L. Hagedorn,', 'book': 'Tools: Working Wood in Eighteenth-Century America', 'publisher': '(Williamsburg, VA: The Colonial Williamsburg Foundation, 1993).', 'author2': '', 'book2': '', 'publisher2': '', 'origin2': 'While tools could be produced by local blacksmiths, the availability of raw materials and skilled labor limited the large-scale production of tools in the American colonies. Specialized tools were typically imported from British production centers in London, Birmingham, and Sheffield.', 'link2': 'https://en.wikipedia.org/wiki/Public_domain', 'self': 'Awl', 'thumbnail': 'AwlThumbnail.jpg', 'Thumb1': 'Rum', 'Thumb2': 'Sugar', 'Thumb3': 'Shot', 'Thumb4': 'Linen', 'Thumb5': 'Garter', 'Thumb6': 'Cotton', 'Thumb7': 'Indigo','production1':'moo', 'production2':'moo', 'materials2':'moo','materials1':'moo','pounds1':'pounds1', 'pounds2':'pounds2', 'New_Description':'', 'Notes':'', 'Notes2':'Notes2'}






app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)






@app.route('/')
def home():
    return render_template('home.html')

@app.route('/title/')
@app.route('/title/<title>/')
def title(title=None):
    entry = object_map[title]

    return render_template('ItemEntries.html', entry=entry)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/departments/')
def departments():
    def title_row(row):
        return row['title']
    dept_db = departmentize_db(object_map.values())
    return render_template('departments.html', departments=dept_db,
                           sorted=sorted, title_row=title_row)

@app.route('/wishlists/')
def wishlists():
    return render_template('wishlists.html')

@app.route('/documents/')
def documents():
    return render_template('documents.html')


class RamsayEntryModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    artifact = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(120), unique=True, nullable=False)
    thumbnail = db.Column(db.String(120), unique=True, nullable=False)
    materials = db.Column(db.String(120), unique=True, nullable=False)
    dimensions = db.Column(db.String(120), unique=True, nullable=False)
    date = db.Column(db.String(120), unique=True, nullable=False)
    origin = db.Column(db.String(120), unique=True, nullable=False)
    distance = db.Column(db.String(120), unique=True, nullable=False)
    collection = db.Column(db.String(120), unique=True, nullable=False)
    link = db.Column(db.String(120), unique=True, nullable=False)
    license = db.Column(db.String(120), unique=True, nullable=False)
    link2 = db.Column(db.String(120), unique=True, nullable=False)
    ledger = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(120), unique=True, nullable=False)
    customer = db.Column(db.String(120), unique=True, nullable=False)
    page = db.Column(db.String(120), unique=True, nullable=False)
    origin2 = db.Column(db.String(120), unique=True, nullable=False)
    production1 = db.Column(db.String(120), unique=True, nullable=False)
    production2 = db.Column(db.String(120), unique=True, nullable=False)
    materials2 = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)
    book = db.Column(db.String(120), unique=True, nullable=False)
    publisher = db.Column(db.String(120), unique=True, nullable=False)
    author2 = db.Column(db.String(120), unique=True, nullable=False)
    book2 = db.Column(db.String(120), unique=True, nullable=False)
    publisher2 = db.Column(db.String(120), unique=True, nullable=False)
    unit = db.Column(db.String(120), unique=True, nullable=False)
    pounds = db.Column(db.String(120), unique=True, nullable=False)
    pounds2 = db.Column(db.String(120), unique=True, nullable=False)
    dollars = db.Column(db.String(120), unique=True, nullable=False)
    analytics = db.Column(db.String(120), unique=True, nullable=False)
    Thumb1 = db.Column(db.String(120), unique=True, nullable=False)
    Thumb2 = db.Column(db.String(120), unique=True, nullable=False)
    Thumb3 = db.Column(db.String(120), unique=True, nullable=False)
    Thumb4 = db.Column(db.String(120), unique=True, nullable=False)
    Thumb5 = db.Column(db.String(120), unique=True, nullable=False)
    Thumb6 = db.Column(db.String(120), unique=True, nullable=False)
    Thumb7 = db.Column(db.String(120), unique=True, nullable=False)
    New_Description = db.Column(db.String(120), unique=True, nullable=False)
    Notes = db.Column(db.String(120), unique=True, nullable=False)
    Notes2 = db.Column(db.String(120), unique=True, nullable=False)




if __name__ == '__main__':
    app.run(debug=True)
