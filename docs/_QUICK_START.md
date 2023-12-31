## Table of contents

1. How to create an empty database
2. How to create your models
3. How to add endpoints
4. Using the /admin

## Creating a Database

1. Login in into your mysql terminal:
```sh
$ mysql
```
2. Once inside, create the database (if needed)
```sql
CREATE DATABASE example;
```
Note: you can delete the previous database using the drop command

## Coding a typical CRUD operation

As an example we are going to create a small API to manage a Person

### Adding an Model

For each `model` you will have to declare a class with the model properties and a method `serialize` that returns a dictionary representation of the class

```py
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }

```

### Adding an endpoint

For each endpoint you will need to have:
1. One `@APP` decorator that specifies the path for the expoint.
    - You can have parameters in the url like this `<int:person_id>`
    - You can specify what methods can be called on that endpoint like this `methods=['PUT', 'GET']`
2. The method what will execute when that endpoint is called (in this case `get_sinde_person`), the name of the method does not matter.
3. Inside the method you can speficy what logic to execute of each type of request using `if request.method == 'PUT'`
4. You have to return always a json and a status code (200,400,404, etc.)

```py
@APP.route('/person/<int:person_id>', methods=['PUT', 'GET'])
def get_single_person(person_id):
    """
    Single person
    """
    body = request.get_json()
    if request.method == 'PUT':
        user1 = Person.query.get(person_id)
        user1.username = body.username
        db.session.commit()
        return jsonify(user1.serialize()), 200
    if request.method == 'GET':
        user1 = Person.query.get(person_id)
        return jsonify(user1.serialize()), 200

    return "Invalid Method", 404
```

### Using the admin

You can add your models to the admin, that way you will be able to manage them without any extra code.

To add a new model into the admin, just open the `src/admin.py` file and add this line inside the `setup_admin` function.

```python
admin.add_view(ModelView(YourModelName, db.session))
```

Note: Make sure you import the model on the top of the file

You can read [more about the admin here](https://github.com/4GeeksAcademy/flask-rest-hello/blob/main/docs/ADMIN.md).
