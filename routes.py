from flask import Flask, render_template
import sys
import logging
 
app = Flask(__name__)      
 
@app.route('/')
def index():
  #return render_template('index.html')
  return 'ok!'

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

if __name__ == '__main__':
  app.run(debug=True)