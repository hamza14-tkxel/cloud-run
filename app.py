from flask import Flask
import os
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  print(os.environ)
  return 'Hello World!\n'


if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
