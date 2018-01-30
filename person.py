# install ORM
# pip install peewee
import peewee

#peewee.MySQLDatabase
#peewee.PostgresqlDatabase
database = peewee.SqliteDatabase('database.db')

class Person(peewee.Model):
    name = peewee.TextField()
    age = peewee.IntegerField()

    def to_dictionary(self):
        return { 'id': self.id, 'name': self.name, 'age': self.age }

    class Meta:
        database = database

try:
    if not Person.table_exists():
        Person.create_table()
        database.create_table(Person)
except Exception as e:
    pass