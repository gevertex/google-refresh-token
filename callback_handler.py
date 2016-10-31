import webapp2
import json

class CallbackHandler(webapp2.RequestHandler):
    def get(self):
        state = self.request.GET['state']
        code = self.request.GET['code']
        self.response.headers['Content-Type'] = 'text/html'
        state_dict = json.loads(state)
        self.response.write('State: ' + state_dict['client_id'])
        self.response.write('\nCode: ' + code)

app = webapp2.WSGIApplication([
    ('/.*', CallbackHandler),
], debug=True)