from flask import Flask
import os
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  environment = str(os.environ.get('ENVIRONMENT'))
  return "Hello World!\n" + environment


if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
