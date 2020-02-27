from flask import Flask


app = Flask(__name__)

# POST - used to receive data
# Get - used to send data back only
@app.route('/')
def home():
   pass

app.run(port=5000)