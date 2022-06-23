from flask import Flask
import os
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  return "Hello World! " + os.environ


if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
