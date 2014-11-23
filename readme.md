# Flask Chat
*A basic chat implementation using Flask-Sockets*

---

## Setup

Setup the environment (if you don't have [`virtualenv`](http://virtualenv.readthedocs.org/en/latest/) installed, install it):

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Message PubSub

Flask Chat uses [Redis](http://redis.io/) as a PubSub to facilitate chat and as a datastore to retain old chats. Do not use Redis if the longterm retension of the chats is important as Redis is designed to eject data as needed without warning. Alternatives like [RabbitMQ](http://www.rabbitmq.com/) can replace both functionalities that Redis is used for, and provide a bit more robust data retension, or the datastore portion can be replaced independently to a more traditional datastore such as a relational database or NoSQL database.

If you don't have redis, it can be installed on OS X with:

```
brew install redis
```

`brew` will present a few different ways to start `redis`. If you with not to have `redis` launch at startup, you can start it ondemand with:

```
redis-server /usr/local/etc/redis.conf
```

Configure to work the application by adding the following to `app/config.local_config.yml`

```
REDIS_URL: 'redis://localhost'
```

# Starting the Server

Start the server with:

```
gunicorn -k flask_sockets.worker server:app -b 127.0.0.1:4999 --debug
```

and visit [`http://localhost:4999`](http://localhost:4999). Open in multiple browsers to observer the action with multiple users.
