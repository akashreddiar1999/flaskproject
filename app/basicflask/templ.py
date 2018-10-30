from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
      user={'username':'dhiraj'}
      posts=[
            {
                  'author':{'username':'daneil'},
                  'body': 'beautiful day'
                  },
            {
                  'author': {'username':'amar'},
                  'body': 'tiger zinda hai was a good movie'
                  }
            ]
      
      return render_template('tmp.html',user=user,posts=posts)
if __name__=='__main__':
      app.run(debug=True)
                             
