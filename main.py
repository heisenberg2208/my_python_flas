import base64
import numpy as np
from PIL import Image
import requests
import io
import matplotlib.pylab as plb
from keras.models import load_model
from flask import request, jsonify, Flask
app = Flask(__name__)



@app.route('/')
def hello_world():
  return 'Hey its Python Flask application!'

if __name__ == '__main__':
  app.run()
