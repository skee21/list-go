from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'sudhanshu suar ke chodal'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

api = os.environ['api_key']