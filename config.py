from flask import Flask, render_template, request, redirect
from pony.orm import *
from datetime import datetime

db = Database()
app = Flask(__name__)
