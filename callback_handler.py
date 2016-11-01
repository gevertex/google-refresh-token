import webapp2
import json
import urllib, urllib2

class CallbackHandler(webapp2.RequestHandler):
    def get(self):
        url = 'https://www.googleapis.com/oauth2/v4/token?'
        state = self.request.GET['state']
        code = self.request.GET['code']

        state_dict = json.loads(state)
        client_id = state_dict['client_id']

        params = {
            'code': code,
            'client_id': client_id,
            'redirect_uri': 'http://www.refreshtoken.com/static/index.html',
            'grant_type': 'authorization_code'
        }

        req = urllib2.Request(urllib2, urllib.urlencode(params))
        rsp = urllib2.urlopen(req)
        content = rsp.read()

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/.*', CallbackHandler),
], debug=True)