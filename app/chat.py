import gevent


class Chat(object):
    def __init__(self, app=None):
        self.clients = []
        if app:
            self.app = app
            self.init_app(app)

    def init_app(self, app):
        if not getattr(app, 'extensions', None):
            app.extensions = {}
        app.extensions['chat'] = self
        self.pubsub = app.redis.pubsub()
        self.pubsub.subscribe(app.config['REDIS_CHANNEL'])

    @property
    def messages(self):
        for message in self.pubsub.listen():
            data = message.get('data')
            if message['type'] == 'message':
                yield data

    def register(self, client):
        self.clients.append(client)

    def send(self, client, data):
        client.send(data)

    def run(self):
        for data in self.messages:
            for client in self.clients:
                gevent.spawn(self.send, client, data)

    def start(self):
        gevent.spawn(self.run)
