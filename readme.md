# Mirror Park
*The app so fresh you with you'd thought of it first.*

---

Mirror Park is a small sample Flask app that integrates:

- [Flask-Security](https://pythonhosted.org/Flask-Security)
- [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy)
- [Flask-Admin](http://flask-admin.readthedocs.org/en/latest)
- [Flask-Script](http://flask-script.readthedocs.org/en/latest)
- [Ordbok](https://github.com/alphaworksinc/ordbok)


---

## Setup

Clone the repo, replacing `new-project` with the name of your new project:

```
git clone https://github.com/eriktaubeneck/mirror-park.git new-project
cd new-project
```

Setup the environment (if you don't have [`virtualenv`](http://virtualenv.readthedocs.org/en/latest/) installed, install it):

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Database

Mirror Park requires a relational database. I recommend Postgres, however any of the [SQLAlchemy Engine Configuration](http://docs.sqlalchemy.org/en/latest/core/engines.html) will work. This needs to be included with the `SQLALCHEMY_DATABASE_URI`. This can either be included in `app/config/config.yml` or `app/config/local_config.yml`. (The later has the advantage of being ignored by git, so that you don't accidentally check in your secret keys and passwords.)

Quick start in memory sqlite database setup:

```
SQLALCHEMY_DATABASE_URI: 'sqlite://'
```
