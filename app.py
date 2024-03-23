import os
import sys
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.absolute()

sys.path.insert(0, str(BASE_DIR / "lib"))
print(sys.path)

from bottle import route, run, SimpleTemplate

from peewee import *

db = SqliteDatabase('masjid.db')

def render(filename, **context):
    template_dir = BASE_DIR / "templates"
    template = SimpleTemplate(name=filename, lookup=[str(template_dir)])
    return template.render(context)

class Person(Model):
    name = CharField()
    birthday = DateField(null=True)

    class Meta:
        database = db

@route('/hello/<name>')
def index(name):
    try:
        person = Person.get(Person.name == name)
    except Person.DoesNotExist:
        person = Person(name=name)
        person.save()

    people = Person.select()
    return render("index.html", name=name, people=people)

if __name__ == "__main__":
    db.create_tables([Person])
    run(host='localhost', port=8080, server="cheroot")
