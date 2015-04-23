import web

from gothonweb import map

urls = (
	"/game", "GameEngine",
	"/", "Index"
)

app = web.application(urls, locals())


# If _session does not exist yet,
# create a new session stored in 'sessions',
# create a new session wherein room=None, and
# set the created session as the _session in config.
# Else, set the config _session as the current session
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, 
								initializer={'room': None})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/', base="layout")

class Index(object):
	def GET(self):
		# this is used to setup the session with starting values
		session.room = map.START 
		web.seeother("/game")


class GameEngine(object):

	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			return render.you_died()

	def POST(self):
		form = web.input(action=None)

		# there's a bug here
		if session.room and form.action:
			session.room = session.room.go(form.action)

		web.seeother("/game")


if __name__ == "__main__":
	app.run()
