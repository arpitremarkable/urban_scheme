### Requirements
- Python 2.7
- pip (curl https://bootstrap.pypa.io/get-pip.py | python)

#### Install
```sh
$ sudo pip install virtualenv
$ virtualenv .virtualenv
$ source .virtualenv/bin/activate
$ pip install -r requirements.txt
```

#### Create user
```sh
$ python manage.py createsuperuser
```

#### Run server
```sh
python manage.py migrate
python manage.py runserver
```

#### Open URL
```
http://localhost:8000/emi-schemes/?amount=1000
```

#### Update EMI Rates
```
http://localhost:8000/admin/emi/emirate/
```
