from flask import Flask
import os
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  env = str(os.environ['ENVIRONMENT'])
  return 'Hello World!\n'


if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
