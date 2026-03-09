from flask import Blueprint, render_template, url_for, redirect
from app.extensions import db
from app.models.post import Post
from app.forms.post_form import PostForm
from flask_login import logout_user, current_user, login_required

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/')
@login_required
def home():
	all_posts = db.session.execute(db.select(Post)).scalars().all()
	print(all_posts)
	return render_template("index.html", posts=all_posts)

@posts_bp.route('/create_post', methods=["GET", "POST"])
@login_required
def create_new_post():

	create_new_post_form = PostForm()
	
	create_new_post_form.submit.label.text = 'Create New Blog Post'

	if create_new_post_form.validate_on_submit():
		
		title = create_new_post_form.title.data
		subtitle = create_new_post_form.subtitle.data
		body = create_new_post_form.body.data
		img_url = create_new_post_form.img_url.data
		author = "Aniket Atram"
		
		new_post = Post(title=title, subtitle=subtitle, body=body, img_url=img_url, author=author)
		db.session.add(new_post)
		db.session.commit()

		return redirect(url_for("posts.home"))

	return render_template("post_form.html", form = create_new_post_form)

@posts_bp.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
	pass