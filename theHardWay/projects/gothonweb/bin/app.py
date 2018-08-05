# actually exercise 50
import web
from gothonweb import map

# urls = ('/hello', 'Index')
urls = (
    '/', 'Index',
    '/game', 'GameEngine',
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

# db = web.database(dbn='postgres', user='Dreams', pw='abc', db='mydb')

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

class Index:
    def GET(self):
        # this is used to "setup" the session with starting values
        session.room = map.START
        print(session.room)
        web.seeother("/game")


        # return render.hello_form()
        # form = web.input(name="Nobady", resource=None, action="download")
        # if from.resource:
        #     greeting = 'Hello %s, Please %s the %s' % (form.name, form.action, form.resource)
        #     return render.index(greeting=greeting)
        # else:
        #     return "ERROR: resource is required."

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = '%s, %s' % (form.greet, form.name)
        return render.index(greeting=greeting)

class GameEngine(object):
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            # why is there here? do you need it?
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, fix it
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")


if __name__ == "__main__":
    app.run()
