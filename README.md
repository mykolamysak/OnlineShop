# **FASTAPI BEST PRACTICE PROJECT STRUCTURE.**

Generate the backend using python, including interactive API documentation.

# **Interactive API documentation**

![img_3.png](static/ApiEndPoint.png)

# **Alternative API documentation**

![img_1.png](static/redocs.png)

# Features
  
* **Fast**:      Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
* **Intuitive**: Great editor support. Completion everywhere. Less time debugging.
* **Easy**:      Designed to be easy to use and learn. Less time reading docs.
* **Short**:     Minimize code duplication. Multiple features from each parameter declaration.
* **Robust**:    Get production-ready code. With automatic interactive documentation.
* **Standards-based**: Based on (and fully compatible with) the open standards for APIs: OpenAPI and JSON Schema.
* Many other features incStandards-basedluding automatic validation, serialization, interactive documentation, authentication with OAuth2
* JWT tokens, etc.

* **Secure password** use bcrypt.
* **JWT token** authentication.
* **SQLAlchemy** models
* **Alembic** migrations.
* **PGAdmin for PostgreSQL** database, you can modify it to use PHPMyAdmin and MySQL easily.

# **~~How to use it**~~
- Dependencies are provided in `requirements.txt`
- You can run the server by going into `/fastapi_best_practice` and running `python3 main.py`

# **Project Structure**

This is the folder/file structure we have.

![](static/project_structure_page.jpg)

# **Overview of project structure**

Root folder flask-best-practices-sample that contains the project specific file under my_project
directory plus the files which are for deployment, virtual environment, .gitignore, .env, etc.

#### **my_project**
**1. constants.py [file]**
* The App level constants are defined in here, right now we preferred to put all string constants in the single file so if we need to do multilingual app it can be useful to have all strings in single place.

**2. language.py [file]**
* This file contains common methods to create the JSON response for success and failure cases.

**3. exception.py [file]**
* This file contains common exception methods for generate the errors.

**4. config.py [file]**
* In config file we have to set the all project configuration into the setting pydantic model.
* By default, the project run in a development mode, if you want to run in product mode then simply
  update the server set variable into the config class.
* Also, the logging related setting added on logging pydentic model.
* Mail configuration class.

**5. utils.py [file]**
* This file contains the collection of small Python functions and classes which make common 
  patterns shorter and easier. 
* It is by no means a complete collection but it has served me quite a bit in the past and I will keep extending it. 
* For, example one of the method make in this is sendmail.

**6. Module folders [folder/s]**
* All the modules must have there own package which works as an abstraction for itself.In this project there is a two module.
1. User Module
    -- contains the use Register/Login related APIs.
2. Blog Module 
    -- contains the blog create, update, delete and read APIs.

* We are using router to manage the modular structure and to avoid app instance sharing among several
  modules and cyclic dependencies
* There can be list of modules in any project but it should have it's own package.

**7 tests [folder]**
* Right now all the test cases are written in single file, it too can be modular but really need some Advice on that!

# **Module level files**

The internal dependency and calling hierarchy should be like this. 
* Module will be devised mostly into five to six different layer. 

## 1. Views Layer:

### **routes.py**
* This file code should be just having the API end points and nothing else.
* It's prior responsibility is to have all the routes for that module.
* This file only interact with service.py.

## 2. Database Layer:
### **models.py**
* This layer is only communicate with the service layer.
* All database models are defined here
* All queries or operation which required DB interaction should define here

## 3. Service Layer:
### **service.py**
* This file is the middleware between views and all other layers.
* This file Just call the other layer's file methods or functions and send the result according.
* For example,we have the requirement of fetch user from database
  so, for that validation layer not direct communicate with the database layer. validation layer first request to the service layer for the user data
  and then service layer communicate with the database layer to fetch the user data from the database
  and then service layer send that user data to the validation layer.


## 4. Language Layer:
### **language.py**
* This layer is only communicate with the service layer.
* Processing the client request APIs data into the simple object like dict if needed, and send response according to the requirement to the client.
* For example, convert response data according to schema, send success/fail response etc.This all kind
  of methods we have performed in this layer.

## 5. Validation Layer:
### **validation.py**
* This layer is only communicate with the service layer.
* This file code should be just having the different-different validations methods or function.
* Here we didn't require this layer(mainly because we have validated data in schemas only) , but if required we need to create it.

## 6. Third-Party Layer:
### **authentication.py**
* This layer is only communicate with the service layer.
* For example, In User module we have used the fastapi-jwt-token and bcrypt module for the password-hash. 
# **Project setup**
## **Linux**
* $ git clone REPOSITORY_URL
* $ cd FOLDER_NAME
* $ python3 -m venv myenv
* $ source myenv/bin/activate
* $ pip3 install -r requirements.txt
* $ python3 main.py

**It should throw errors for database as we have not yet integrated database with it. So let's do that.**

**1. Install Postgres**

* sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
* wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add 
* sudo apt-get update
* sudo apt-get -y install postgresql # You can define specific version here

**Please refer these links for more information**

1. ​		https://www.postgresql.org/download/linux/ubuntu/
2. ​		https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

**2 .Creating a database**
* You should be able to create a database in postgres using createdb command, the database name you can keep it as you want. This database connection details is to be stored in .env file where we will store secrets.
* This file is in gitognore (What's the meaning of adding it in git, It's Top secret ;) )

* In that file there is this constant.

* **SQLALCHEMY_DATABASE_URL**='postgres://USERNAME:PASSWORD@localhost/DATABASE_NAME'

# Packages used

These are the packages which are most-commonly used in a fastapi project based on API.

### SQLAlchemy

**Package Link:** ​  https://docs.sqlalchemy.org/en/14/
* It provides support for SQLALCHEMY and ORM using database like sqlite, mysql, postgres,oracle.

### Alembic-Migrate

**Package Link:** ​ https://alembic.sqlalchemy.org/en/latest/tutorial.html
* It provides support for handles SQLALCHEMY database migration for FastApi application using alembic.
* here is the other YouTube video link from that you can learn how we can set the alembic library on fastapi
  project.
* `https://www.youtube.com/watch?v=gISf9AWAS7k&t=2100s&ab_channel=SumanshuNankana`

### passlib-Bcrypt

**Package Link:** ​ https://fastapi.tiangolo.com/pt/tutorial/security/oauth2-jwt/
* It provides support for handles password hashes for FastApi application using Bcrypt algorithm.


### python dot-env

**Package Link:** ​ https://pypi.org/project/python-dotenv/
* It would be annoying to set environment variables every time we open our terminal, so we can set environment variables in a local file called .env instead and grab those variables using a Python library like python-dotenv.

### class-base views

**Package Link:** ​ https://fastapi-utils.davidmontague.xyz/user-guide/class-based-views/
* As you create more complex FastAPI applications, you may find yourself frequently repeating the same dependencies in multiple related endpoints.
* A common question people have as they become more comfortable with FastAPI is how they can reduce the number of times they have to copy/paste the same dependency into related routes.
* fastapi_utils provides a “class-based view” decorator (@cbv) to help reduce the amount of boilerplate necessary when developing related routes.
* For example, In Blog module we have to perform blog create, update, delete and read apis routes point into the fastapi class base views package.
* **Package release date**: `on 10 Feb 2020`
* **Package start**: `1.1K`

### FastAPI-JWT Auth

**Package Link:**  ​ https://indominusbyte.github.io/fastapi-jwt-auth/
* FastAPI extension that provides JWT Auth support (secure, easy to use and lightweight), if you were familiar with flask-jwt-extended this extension suitable for you, cause this extension inspired by flask-jwt-extended 😀
* Access tokens and refresh tokens
* Freshness Tokens
* Revoking Tokens
* Support for WebSocket authorization
* Support for adding custom claims to JSON Web Tokens
* Storing tokens in cookies and CSRF protection

### FastAPI-Pydentic

**Package Link:** ​ https://pydantic-docs.helpmanual.io/
* Data validation and settings management using python type annotations.
* pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
* Define how data should be in pure, canonical python; validate it with pydantic.

# Database and Migrations in FASTAPI

For any SQL database connection in a fastapi application we can use SQLAlchemy Package. It also provide support for ORM.

SQLAlchemy

* `https://docs.sqlalchemy.org/en/14/`
* It provides support for sqlalchemy and ORM using SQL databases like sqlite, mysql, postgres, oracle.
* In fastapi, we create the engine and session into the database module.
* The whole database setting can be divided in below stape.
  1. set the current server config.
  2. create the sqlalchemy engine.
  3. create the session marker object.
  4. define the declarative base.


Alembic-Migrate
* `https://alembic.sqlalchemy.org/en/latest/tutorial.html`


* After adding changes to your models you can run these commands.

* #### **`alembic init migration`**
* #### `alembic revision -- autogenerate -m "added content`"
* #### **`alembic upgrade head`**

* For setting the current server database url on alembic.ini file we need to use configparser python package
* Handles SQLAlchemy database migrations for FASTAPI applications.

**Reference Link** : ​ https://stackoverflow.com/questions/8884188/how-to-read-and-write-ini-file-with-python3

* First command will create a directory named Migrations. That need to be on version control, to detect every change in future.
* Second command will create a python script that refers to the changes. That also needs to be on version control.
* Third will update the latest changes on to the database.
* The whole alembic database url setting int alembic.ini file can be divided in below stape.
  1. create the configparser instance.
  2. read the alembic.ini file.
  3. update the sqlalchemy.url variable.
* Alembic has some drawbacks. When you change type or size of any field  alembic migrate will not detect it. So, for that we have one solution.
* [https://stackoverflow.com/a/58539794](https://stackoverflow.com/a/58539794)
* We have to add **compare_type = True** in context.configure() of env.py inside migration folder in both function named run_migrations_online and run_migrations_offline. For example:

![img_2.png](static/migration.png)




  





