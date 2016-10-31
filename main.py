import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.redirect("/static/index.html")
        # self.response.headers['Content-Type'] = 'text/html'
        # self.response.write('Hello, World! 123')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
