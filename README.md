Task-2-EVO-Python-Lab-2022


[Link to Demo](https://say-hi-evo-python-lab-2022.herokuapp.com/)
==============

To run locally
==============

1. Install and activate environment
2. Install requirements using this command: `pip install -r requirements.txt`
3. Create file `.env` with the following structure:

```
SECRET_KEY=yoursecret
```

4. Run migrations: `python manage.py migrate`
5. Run application: `python manage.py runserver`

Deployment
==========

Install the Heroku CLI

__Download and install the Heroku CLI.__

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```
$ heroku login
```

__Clone the repository__

Use Git to clone say-hi-evo-python-lab-2022's source code to your local machine.

```
$ heroku git:clone -a say-hi-evo-python-lab-2022$ cd say-hi-evo-python-lab-2022
```

__Deploy your changes__

Make some changes to the code you just cloned and deploy them to Heroku using Git.

```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
