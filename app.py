from flask import Flask, request

app = Flask(__name__)

@app.get('/check')
def check():
  args = request.args
  return { 'hello': args["something"] }

if __name__ == '__main__':
  
  app.run(port=7777)
