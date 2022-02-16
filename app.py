from flask import *
from captcha.image import ImageCaptcha
import json, random, string
from lib2to3.pygram import Symbols

app = Flask(__name__)  
app.config["DEBUG"] = True  

length = int(10)
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

ALL = upper + symbols + num
ALPHABETS = upper
NUMBERS = num
SYMBOLS = symbols

app = Flask(__name__)
@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
      <h1 class="project-name">Welcome to Captcha Changing Image API 🤖</h1>
      <h2 class="project-tagline">An API returns random Captcha Images</h2
<h2 id="usage">Usage:</h2>
<ul>
<p>These Are The Endpoints Of The API</p>
  <li><code class="language-plaintext highlighter-rouge">/all</code> will return Captcha Image with the mix of ALPHABETS,SYMBOLS,NUMBERS at length of 10</li>
  <li><code class="language-plaintext highlighter-rouge">/alphabets</code> will return Captcha Image filled with ALPHABETS only</li>
      <li><code class="language-plaintext highlighter-rouge">/numbers</code> will return Captcha Image filled with NUMBERS only</li>
    <li><code class="language-plaintext highlighter-rouge">/symbols</code> will return Captcha Image filled with SYMBOLS only</li>
</ul>
    </main>
  </body>
</html>
 '''

@app.route('/all', methods=['GET'])
def all_pic():
    temp = random.sample(ALL,length)
    password = "".join(temp)
    image = ImageCaptcha(width = 300, height = 100)
    captcha_text =  password
    data = image.generate(captcha_text) 
    image.write(captcha_text, 'CAPTCHA.png')
    file = f'CAPTCHA.png'
    return send_file(file, mimetype='jpg')

@app.route('/alphabets', methods=['GET'])
def alphabets_pic():
    temp = random.sample(ALPHABETS,length)
    password = "".join(temp)
    image = ImageCaptcha(width = 300, height = 100)
    captcha_text =  password
    data = image.generate(captcha_text) 
    image.write(captcha_text, 'CAPTCHA.png')
    file = f'CAPTCHA.png'
    return send_file(file, mimetype='jpg')

@app.route('/numbers', methods=['GET'])
def numbers_pic():
    temp = random.sample(NUMBERS,length)
    password = "".join(temp)
    image = ImageCaptcha(width = 300, height = 100)
    captcha_text =  password
    data = image.generate(captcha_text) 
    image.write(captcha_text, 'CAPTCHA.png')
    file = f'CAPTCHA.png'
    return send_file(file, mimetype='jpg')

@app.route('/symbols', methods=['GET'])
def symbols_pic():
    temp = random.sample(SYMBOLS,length)
    password = "".join(temp)
    image = ImageCaptcha(width = 300, height = 100)
    captcha_text =  password
    data = image.generate(captcha_text) 
    image.write(captcha_text, 'CAPTCHA.png')
    file = f'CAPTCHA.png'
    return send_file(file, mimetype='jpg')

if __name__ == '__main__':
	app.run(threaded=True, port=5000)