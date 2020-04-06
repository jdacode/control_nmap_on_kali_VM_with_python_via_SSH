from flask import Flask
from nmap import Nmap

app = Flask(__name__)


# Main Page Route
@app.route('/')
def index():
    return """<html><body>
  <h2>kali SSH!</h2>
    <p>NMAP: <br>""" + nmap1.run_nmap() + " </p></body></html>"



if __name__ == '__main__':
    nmap1 = Nmap()
    app.run()









