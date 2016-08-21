#!/usr/bin/python
from app.views import app
import app.models
# from gevent.wsgi import WSGIServer
# http_server = WSGIServer(('', 5000), app)
# http_server.serve_forever()

# start the server
if __name__ == "__main__":
    models.initialize()
    try:
        models.User.create_user(
            username='harrisonkamau',
            email='kamauharry@yahoo.com',
            password='password',
        )
    except ValueError:
        pass
app.run(debug=True)
