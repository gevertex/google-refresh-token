**What is this**
  This is a web application designed to make generating google refresh tokens much easier than before.  This will work for any refresh token, but it is specifically aimed at those wanting to generate refresh tokens for verifying IAP receipts for their apps.  It works and it's easy to use.  Enjoy.

**How to Use**

* Install google cloud engine @ https://cloud.google.com/sdk/docs/
* cd to the app's root directory
* run the app in developer mode
* sudo dev_appserver.py --port=80 .
* In your browser, go to: http://localhost
  
  
Disclaimer:  This is a dirty hack.  It works, but it's dirty.  Feel free to contribute.  I originally intended this to run in google app engine, but since Google doesn't allow Android Client IDs to redirect anywhere but localhost (or an app), we need to run as localhost.
