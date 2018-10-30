from flask import Flask

import flask_admin as admin


# Create custom admin view
class MyAdminView(admin.BaseView):
    @admin.expose('/')
    def index(self):
        return self.render('myadmin.html')


class AnotherAdminView(admin.BaseView):
    @admin.expose('/')
    def index(self):
        return self.render('anotheradmin.html')

    @admin.expose('/test/')
    def test(self):
        return self.render('test.html')


# Create flask app


# Flask views
@app.route('/')


# Create admin interface



if __name__ == '__main__':

    # Start app
    app.run()
