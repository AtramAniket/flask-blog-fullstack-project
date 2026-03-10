from flask import Blueprint, render_template, url_for, redirect, request, flash
from app.extensions import db
from app.models.post import Post
from app.forms.post_form import PostForm
from app.forms.contact_form import ContactForm
from flask_login import logout_user, current_user, login_required

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/')
@login_required
def home():
	all_posts = Post.query.order_by(Post.created_at.desc()).limit(4)
	print(all_posts)
	return render_template("index.html", posts=all_posts)


@posts_bp.route('/create_post', methods=["GET", "POST"])
@login_required
def create_new_post():

	if current_user.role != "admin":
		return render_template('404.html')

	create_new_post_form = PostForm()
	
	create_new_post_form.submit.label.text = 'Create New Blog Post'

	if create_new_post_form.validate_on_submit():
		
		title = create_new_post_form.title.data
		subtitle = create_new_post_form.subtitle.data
		body = create_new_post_form.body.data
		img_url = create_new_post_form.img_url.data
		author = current_user.username
		
		new_post = Post(title=title, subtitle=subtitle, body=body, img_url=img_url, author=author)
		db.session.add(new_post)
		db.session.commit()

		return redirect(url_for("posts.home"))

	return render_template("post_form.html", form = create_new_post_form)

@posts_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def view_post(post_id):
	
	post = db.session.execute(db.select(Post).where(Post.id == post_id)).scalar()
	
	# Next post = next **older** post (smaller id)
	next_post = Post.query.filter(Post.id < post.id).order_by(Post.id.desc()).first()

	# Previous post = next **newer** post (larger id)
	previous_post = Post.query.filter(Post.id > post.id).order_by(Post.id.asc()).first()

	return render_template('post.html', post = post, previous_post = previous_post ,next_post = next_post )


@posts_bp.route('/delete/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    if current_user.role != "admin":
        render_template('404.html')

    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('posts.home'))



@posts_bp.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
	
	post = Post.query.get_or_404(post_id)
	
	form = PostForm(obj=post)

	if form.validate_on_submit():
		form.populate_obj(post)
		db.session.add(post)
		db.session.commit()
		flash("Post updated successfully", "success")
		return redirect(url_for('posts.view_post', post_id = post.id))

	return render_template("post_form.html", form = form)


@posts_bp.route('/about')
def about():
	return render_template("about_me.html")

@posts_bp.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	return render_template("contact.html", form=form)


@posts_bp.route('/all_posts')
def all_posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=5)
    return render_template("all_posts.html", posts=posts)