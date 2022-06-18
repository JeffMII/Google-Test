from flask import Flask, request

app = Flask(__name__)

@app.get('/check')
def check():
  
  return { 'hello': 'world!' }

if __name__ == '__main__':
  
  app.run(port=7777)