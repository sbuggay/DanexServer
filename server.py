# DAN-EX server

import sys, os, web, time, json

urls = (
	'/options', 'options',
	'/jobs', 'get_jobs',
	'/jobs/add', 'add_job',
	'/jobs/edit', 'edit_job',
	'/jobs/delete', 'delete_job',
	'/equipment', 'get_equipment',
	'/validate', 'validate'
	)

app = web.application(urls, globals())
db = web.database(dbn='sqlite', db='danex.db')

class options:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return json.dumps(urls)

# Get all jobs
class get_jobs:
	def GET(self):
		web.header('Content-Type', 'application/json')
		try:
			return json.dumps({'status': 'success', 'jobs': db.select('jobs').list()})
		except:
			e = sys.exc_info()[0]
			return json.dumps({'status': 'error', 'message': 'Error: %s' % e})

# Add a job, defaults are None
class add_job:
	def GET(self):
		web.header('Content-Type', 'application/json')
		g = web.input(name="None", address="None", phone="", notes="", lastUpdated=None)
		db.insert('jobs', job=g.name, address=g.address, phone=g.phone, notes=g.notes, lastUpdated=g.lastUpdated)
		return json.dumps({'status': 'success'})

# Get a specific job by name
class get_job:
	def GET(self, job):
		web.header('Content-Type', 'application/json')
		try:
			return json.dumps(db.select('jobs', where="name=\"" + job + "\"").list())
		except:
			e = sys.exc_info()[0]
			return json.dumps({'status': 'error', 'message': 'Error: %s' % e})

# Edit a job by name, cannot change the name
class edit_job:
	def GET(self): #alter the job by id
		web.header('Content-Type', 'application/json')
		g = web.input(name, address, phone, notes, lastUpdated, id)
		print g.id, g.name
		try:
			db.delete('jobs', where="id=\"" + g.id + "\"")
			db.insert('jobs', id=g.id, job=g.name, address=g.address, phone=g.phone, notes=g.notes, lastUpdated=g.lastUpdated)
			return json.dumps({'status': 'success'})
		except:
			return json.dumps({'status': 'error'})


# Delete a job by name
class delete_job:
	def GET(self):
		web.header('Content-Type', 'application/json')
		g = web.input(id=-1)
		print "deleting: " + g.id
		try:
			db.delete('jobs', where="id=\"" + g.id + "\"")
			return json.dumps({'status': 'success'})
		except:
			return json.dumps({'status': 'error'})

class get_equipment:
	def GET(self):
		web.header('Content-Type', 'application/json')
		try:
			return json.dumps(db.select('equipment').list())
		except:
			return json.dumps({'status': 'error'})

class validate:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'status': 'success'})


if __name__ == "__main__":
	app.run()

