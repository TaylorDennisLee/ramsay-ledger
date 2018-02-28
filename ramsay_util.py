import csv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


sample_entry = {'title': 'Awl', 'description': 'Awls are spiked tools with knob-like handles. These can be used for marking, stitching, or making holes. The tip is pushed into a material and then twisted in order to achieve the desired result.', 'image': 'Awl.jpg', 'materials': 'Illustration', 'dimensions': '', 'distance': '', 'collection': 'Pearson Scott Foresman via Wikimedia Commons', 'link': 'https://commons.wikimedia.org/wiki/File:Awl_2_%28PSF%29.png', 'page': '166', 'department': 'Tool', 'pounds': '6 pence per dozen', 'dollars': '5.6', 'license': 'Public Domain', 'artifact': 'Illustration of an Awl', 'date': '', 'origin': '', 'analytics': 'The databases record six purchases of awls. They were sold by the dozen and their prices range from five to six pence.', 'customer': 'Samuel Smith', 'ledger': 'AwlLedger.jpg', 'unit': '1 dozen', 'author': 'James M. Gaynor and Nancy L. Hagedorn,', 'book': 'Tools: Working Wood in Eighteenth-Century America', 'publisher': '(Williamsburg, VA: The Colonial Williamsburg Foundation, 1993).', 'author2': '', 'book2': '', 'publisher2': '', 'origin2': 'While tools could be produced by local blacksmiths, the availability of raw materials and skilled labor limited the large-scale production of tools in the American colonies. Specialized tools were typically imported from British production centers in London, Birmingham, and Sheffield.', 'link2': 'https://en.wikipedia.org/wiki/Public_domain', 'self': 'Awl', 'thumbnail': 'AwlThumbnail.jpg', 'Thumb1': 'Rum', 'Thumb2': 'Sugar', 'Thumb3': 'Shot', 'Thumb4': 'Linen', 'Thumb5': 'Garter', 'Thumb6': 'Cotton', 'Thumb7': 'Indigo','production1':'moo', 'production2':'moo', 'materials2':'moo','materials1':'moo','pounds1':'pounds1', 'pounds2':'pounds2', 'New_Description':'', 'Notes':'', 'Notes2':'Notes2'}



def create_database():
    db.create_all()


def sample_load_entry():
    new_entry = RamsayEntryModel(
            title = sample_entry['title'],
            artifact = sample_entry['artifact'],
            image = sample_entry['image'],
            thumbnail = sample_entry['thumbnail'],
            materials = sample_entry['materials'],
            dimensions = sample_entry['dimensions'],
            date = sample_entry['date'],
            origin = sample_entry['origin'],
            distance = sample_entry['distance'],
            collection = sample_entry['collection'],
            link = sample_entry['link'],
            license = sample_entry['license'],
            link2 = sample_entry['link2'],
            ledger = sample_entry['ledger'],
            department = sample_entry['department'],
            customer = sample_entry['customer'],
            page = sample_entry['page'],
            origin2 = sample_entry['origin2'],
            production1 = sample_entry['production1'],
            production2 = sample_entry['production2'],
            materials2 = sample_entry['materials2'],
            description = sample_entry['description'],
            author = sample_entry['author'],
            book = sample_entry['book'],
            publisher = sample_entry['publisher'],
            author2 = sample_entry['author2'],
            book2 = sample_entry['book2'],
            publisher2 = sample_entry['publisher2'],
            unit = sample_entry['unit'],
            pounds = sample_entry['pounds'],
            pounds2 = sample_entry['pounds2'],
            dollars = sample_entry['dollars'],
            analytics = sample_entry['analytics'],
            Thumb1 = sample_entry['Thumb1'],
            Thumb2 = sample_entry['Thumb2'],
            Thumb3 = sample_entry['Thumb3'],
            Thumb4 = sample_entry['Thumb4'],
            Thumb5 = sample_entry['Thumb5'],
            Thumb6 = sample_entry['Thumb6'],
            Thumb7 = sample_entry['Thumb7'],
            New_Description = sample_entry['New_Description'],
            Notes = sample_entry['Notes'],
            Notes2 = sample_entry['Notes2']
            )

    # new_entry = RamsayEntryModel(title='Moose',description='Candy')
    db.session.add(new_entry)
    db.session.commit()



def sample_load_database_from_csv():
    object_map = getObjectMapFile()
    for row_key in object_map:
        print(row_key)
        print(object_map[row_key])



def database(csv_rows, object_map):
    """
    takes rows from csv_rows and imports the object database for the    
    Ramsay website
    """


class LedgerItem(object):
    def __init__(self, title, description, image, materials, dimensions, distance, collection, link, page, department, pounds, dollars, license=None, artifact=None, date=None, origin=None, analytics=None, customer=None, ledger=None, Unit=None, author=None, book=None, publisher=None, author2=None, book2=None, publisher2=None, origin2=None, link2=None):
        self.title = title
        self.description = description
        self.image = image
        self.materials = materials
        self.dimensions = dimensions
        self.distance = distance
        self.collection = collection
        self.link = link
        self.page = page
        self.department = department
        self.unit = unit
        self.pounds = pounds
        self.dollars = dollars
        self.license = license
        self.artifact = artifact
        self.date = date
        self.origin = origin
        self.analytics = analytics
        self.customer = customer
        self.ledger = ledger
        self.author = author
        self.book = book
        self.publisher = publisher
        self.author2 = author2
        self.book2 = book2
        self.publisher2 = publisher2
        self.origin2 = origin2
        self.link2 = link2






def getObjectMapFile():
    object_map = {}
    with open("NewLedgerDB.csv") as object_map_file:
        reader = csv.DictReader(object_map_file)
        for row in reader:
            object = row["self"]
            object_map[object] =    {"title": row["title"],
                                    "description": row["description"],
                                    "image": row["image"],
                                    "materials": row["materials"],
                                    "dimensions": row["dimensions"],
                                    "distance": row["distance"],
                                    "collection": row["collection"],
                                    "link": row["link"],
                                    "page": row["page"],
                                    "department": row["department"],
                                    "pounds": row["pounds"],
                                    "dollars": row["dollars"],
                                    "license": row["license"],
                                    "artifact": row["artifact"],
                                    "date": row["date"],
                                    "origin": row["origin"],
                                    "analytics": row["analytics"],
                                    "customer": row["customer"],
                                    "ledger": row["ledger"],
                                    "unit": row["unit"],
                                    "author": row["author"],
                                    "book": row["book"],
                                    "publisher": row["publisher"],
                                    "author2": row["author2"],
                                    "book2": row["book2"],
                                    "publisher2": row["publisher2"],
                                    "origin2": row["origin2"],
                                    "link2": row["link2"],
                                    "self": row["self"],
                                    "thumbnail": row["thumbnail"],
                                    "Thumb1": row["Thumb1"],
                                    "Thumb2": row["Thumb2"],
                                    "Thumb3": row["Thumb3"],
                                    "Thumb4": row["Thumb4"],
                                    "Thumb5": row["Thumb5"],
                                    "Thumb6": row["Thumb6"],
                                    "Thumb7": row["Thumb7"]}
    return object_map


def departmentize_db(db):
    departments = {}
    for row in db:
        dept = row["department"]
        if not dept in departments:
            departments[dept] = []
        departments[dept].append(row)
    return departments


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





def main():
    sample_load_entry()

if __name__ == '__main__':
    main()
