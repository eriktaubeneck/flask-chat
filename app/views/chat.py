import gevent
import json


def register_chat_routes(app, sockets):
    chat = app.extensions['chat']

    @sockets.route('/submit')
    def submit(ws):
        while ws is not None:
            gevent.sleep()
            message = ws.receive()

            if message:
                print 'message: {}'.format(message)
                app.redis.publish(app.config['REDIS_CHANNEL'], message)
                app.redis.lpush(app.config['REDIS_CHANNEL'], message)

    @sockets.route('/receive')
    def receive(ws):
        chat.register(ws)

        while ws is not None:
            gevent.sleep()

    @app.route('/past_chats')
    def past_chats():
        past_chats = app.redis.lrange(app.config['REDIS_CHANNEL'], 0, 10)
        return json.dumps(past_chats[::-1])
