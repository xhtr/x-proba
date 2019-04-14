# Rennty

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

- Docker Community Edition (Docker Engine Community)

  *e.g: Docker Desktop (Mac), Docker Desktop (Windows)*

  [https://docs.docker.com/install/](https://docs.docker.com/install/)

  **You may need to create a dockerhub account to download docker.**

### Installing

A step by step series of examples that tell you how to get a development env running

1. Use `nginx-proxy`. It allows to have a load-balancer on your local machine listenning on port 80. The app will be behind nginx-proxy.

  ```
  git clone git@github.com:sovanna/nginx-proxy.git \
  && cd nginx-proxy \
  && docker network create nginx-proxy \
  && docker-compose up -d
  ```

2. Update your host file (e.g On MacOS)

  ```
  sudo vi /etc/hosts
  ```
  and put: `127.0.0.1 rennty-test.local`

  **The ensure at the end to have access to the project with [http://rennty-test.local](http://rennty-test.local)**

3. Clone the project

  ```
  git clone git@github.com:Rennty/x-proba.git rennty-test \
  && cd rennty-test
  ```

5. Start

  ```
  docker-compose up -d
  ```

### Verification

The app should be available, to check, you can:

- go to [http://rennty-test.local](http://rennty-test.local) and you should see a 404 Not Found

- `docker-compose logs -f server` should give you a line like `Listening at: http://0.0.0.0:8077`

- go to [http://rennty-test.local/ping](http://rennty-test.local/ping) and you should see a `pong`


### Database (postgres)

For now, we only have few data model describe in package `sxmodel`. You can look at it, it is related to `User`.


First, init database migration (this project use `Flask-migrate`)

- `docker-compose exec server flask db init`
- `docker-compose exec server flask db migrate`
- `docker-compose exec server flask db upgrade`


Now, tables `user`, `profile`, `contact` should be added to `Postgres`.


## Exercices

Note: We are going to use **Flask** [http://flask.pocoo.org/docs/1.0/](http://flask.pocoo.org/docs/1.0/)

You can also find help here [the flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

**First, take a look of each folders, files in the repository to see which packages etc.. this project have.**

### You can do exercices in following order for example: 1 / 4 / 2 / 5 / 3 / 6

### When finish or want to share, just make a pull-request

---

### 1 - Implements code that allows to create a user (focused on backend)

#### Guideline

- Create an endpoint on **index page** instead of seeing `Not Found`

	You can create the backend code in server/app/main/routes.py

	```
	- you need to create a function and return a template `index.html`
	- copy from ping function, make the necessary change
	- look to the documentation if you don't know how to render a html template
	```

	**see flask documentation for help** [http://flask.pocoo.org/docs/1.0/](http://flask.pocoo.org/docs/1.0/)

- In the index.html template, put a link that redirect to a page `/auth/register`

	```
	use to automatic function `url_for` in the template to generate the URL

	ex: <a href="{{ url_for('auth.register') }}">register</a>
	```

- Create an empty register.html page

- Create a register form  with only login and password field in the backend

	look at [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/quickstart.html)

- Display the form in the register.html page

	You can use `{{ wtf.quick_form(form) }}` from [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/forms.html)

- Complete the backend part to add a user


	ex:

	```
	from sxmodel.Users import User

	user = User(login=xx, password=xxx)
	```


**You can check the pgadmin to see if the user is well registered**
[http://localhost:8008/](http://localhost:8008/)
**don't forget to add a server from pgadmin to connect** (use .env file for the credentials)

---

### 2 - Implements code that allows to login a user (focused on backend)

#### Guideline

see [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)


---

### 3 - Improvements

Make any necessary changes that you think cool, important or logic

**Tips: url prefix, form validation, password encrypted, etc...**

---

### 4 - Frequencies part 1 (from adventofcode 2018)

If you go to [http://rennty-test.local/frequencies](http://rennty-test.local/frequencies)

you will see **0**

If you open the file at `server/app/main/frequencies.txt` you will see a bunch of numbers (positive/negative). They are frequencies. Starting from 0, when you see **+1** it means **increase by 1**, when you see **-4**, it means **decrease by 4**.

ex :

```
starting with frequency of 0

+1,
-2,
+3,
+1
```
**The final frequency will be 3**

Started from 0, what will be the final frequency with the values in `frequencies.txt`.

---

### 5 - Frequencies part 2 (from adventofcode 2018)

Find the first frequency it reaches twice.

ex :

```
starting with frequency of 0

+1,
-2,
+3,
+1
```

```
0 + 1 = 1
1 - 2 = -1
-1 + 3 = 2
2 + 1 = 3
HERE, we continue from the beginning
3 + 1 = 4
4 - 2 = 2 (2 was already seen)
```

**So the first frequency see twice is 2**

--- 

### 6 - BONUS

Make a beautiful login or register page using **React** directly in the .html page.

So, without complete frontend stack, **just React**.
without webpack, etc.