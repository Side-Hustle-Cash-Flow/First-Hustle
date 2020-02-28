from flask import Flask, render_template, request


app = Flask(__name__)

# POST - used to receive data
# Get - used to send data back only


@app.route('/')
def home():
   username = request.args.get('name')
   return render_template('base.html', name=username)




if __name__ =="__main__":
   app.run(port=5000)