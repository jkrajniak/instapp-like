Instlike app
============

App build with Django 1.11.

Libraries:
 - Django 1.11 & sqlite
 - Google Vision
 - Twitter bootstrap

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


Screenshots
==============

Main:

![Main](https://dl.dropboxusercontent.com/s/oxhhy6s8qw9w8r6/screen1.png?dl=0 "Main page")

Adding image:
![Adding](https://dl.dropboxusercontent.com/s/sczjfascfib700d/screen2.png?dl=0 "Main page")

Image details
![Details](https://dl.dropboxusercontent.com/s/tl9xzfq9j4h9dpi/screen3.png?dl=0 "Main page")
