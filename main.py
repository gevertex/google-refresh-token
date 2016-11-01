import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        # self.redirect("/static/index.html")
        self.response.headers['Content-Type'] = 'text/html'

        f = open('/static/index.html', 'r')
        self.response.write(f)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
