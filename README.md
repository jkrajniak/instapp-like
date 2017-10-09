Instlike app
============

App build with Django 1.11.

Libraries:
 - Django 1.11
 - Google Vision

How to use it

```
$ python3 -m venv vision
$ cd vision
$ source bin/activate
$ git clone https://github.com/MrTheodor/instapp-like.git
$ cd instapp-like
$ pip install -r requirements.txt
$ cd project
$ ./manage.py migrate
```

To run you need [Google credentials](https://developers.google.com/identity/protocols/application-default-credentials).

```
$ export GOOGLE_APPLICATION_CREDENTIALS=<path to json file with credentials>
```

finally you can run test server
```
$ ./manage.py runserver
```
