from app.chat import Chat
from flask.ext.security import Security
from flask_sockets import Sockets

security = Security()
sockets = Sockets()
chat = Chat()
