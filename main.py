import webapp2
import urllib


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.redirect("index.html?" + urllib.urlencode(self.request.params))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
