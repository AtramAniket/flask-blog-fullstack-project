from flask import Blueprint, render_template, url_for, redirect
from app.extensions import db

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/')
def home():
	return '<p>Hello World</p>'