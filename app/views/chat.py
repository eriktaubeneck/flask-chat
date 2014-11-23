import gevent


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

    @sockets.route('/receive')
    def receive(ws):
        chat.register(ws)

        while ws is not None:
            gevent.sleep()
