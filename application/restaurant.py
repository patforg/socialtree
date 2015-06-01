#####
# Author: NuclearBanane
# Contributors : 
# Date : 2015/02/12
# Version : v0.2
#####

import tornado.ioloop   #Basic imports for the tornado library
import tornado.web      #
import dbhandler

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHandler(BaseHandler):
    def get(self):
        # Information fed to make the page dynamic
        page = dict()
        
        #Test to see if the visitor has ever visted the website.
        #relavent to both registered and none registered users
        if self.get_cookie("guestviewer")!='true':
            #If they have never visited they will be redirected to the splash page
            self.redirect("/Splash")
            return
        # This is to see if there is a cookie that represents the User Data
        # If there is then we want to feed this information to the page
        elif self.current_user : 
            page['authenticated']='true'
            page['Name']= tornado.escape.xhtml_escape(self.current_user)
        else :
            page['authenticated']='false'

        self.render("assets/frontpage.html",mest=page) 

class LoginHandler(BaseHandler):
    def get(self):
        self.render("assets/login.html") 

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.set_cookie("guestviewer", "true")
        self.redirect("/")

class SignupHandler(BaseHandler):
    def get(self):
        self.render("assets/signup.html") 
    def post(self):
        #In all seriouness, I made password plain text because I lacked the time
        newusr=dict()
        newusr['userName']=self.get_argument("username")
        newusr['firstname']=self.get_argument("firstname")
        newusr['lastname']=self.get_argument("lastname")
        newusr['email']=self.get_argument("email")
        newusr['password']=self.get_argument("password")
        if dbhandler.addUsr(newusr):
            self.set_secure_cookie("user", self.get_argument("name"))
            self.set_cookie("guestviewer", "true")
            self.redirect("/")
        else:
            print 'lol' 
            #implement other logic

class SplashHandler(BaseHandler):
    def get(self):
        self.render("assets/splash.html")

class GuestHandler(BaseHandler):
    def get(self):
        self.set_cookie("guestviewer", "true")
        self.redirect("/")
        return

class ProfileHandler(BaseHandler):
    def get(self):
        self.write('<html><body> <p>making this soon</p></body></html>')

####
# Tornado uses 'handlers' to take care of requests to certain URLs
# This makes certain API requests from a web page or such an easy to handle
# Unfortunatly it means we need to be very granular with our handlers
####

application = tornado.web.Application(
	[
		(r'/',              MainHandler),
        (r'/Splash',        SplashHandler),
        (r'/Login',         LoginHandler),
        (r'/Signup',        SignupHandler),
        (r'/Guest',         GuestHandler),
        (r'/Profile',       ProfileHandler),

		(r'/(favicon.ico)', tornado.web.StaticFileHandler, {'path': 'assets/'        }),
        (r'/images/(.*)',   tornado.web.StaticFileHandler, {'path': 'assets/images/' }),
        (r'/fonts/(.*)',    tornado.web.StaticFileHandler, {'path': 'assets/fonts/'  }),
		(r'/css/(.*)',      tornado.web.StaticFileHandler, {'path': 'assets/css/'    }),
        (r'/js/(.*)',       tornado.web.StaticFileHandler, {'path': 'assets/js/'     })
	],cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")

####
# When you run python restaurant.py, this runs and starts the tornado listner
####
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
