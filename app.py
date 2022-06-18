from flask import Flask, request

app = Flask(__name__)

@app.get('/check')
def check(something):
  
  return { 'hello': something }

if __name__ == '__main__':
  
  app.run(port=7777)
