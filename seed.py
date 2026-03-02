from app import create_app
from app.extensions import db
from app.models.post import Post

app = create_app()

first_post = Post(
	title="My first post",
	subtitle="This is my forst post added to test API",
	body="Hello there. I am first blog post. I hope you are having a great time",
	author="Aniket Atram",
	img_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpaperaccess.com%2Ffull%2F31193.jpg&f=1&nofb=1&ipt=709cc8ab8592a2cc2a1ef595570efa79d67a389d716869170a70efd6ef432e79")

second_post = Post(
	title="This is my second post",
	subtitle="How about this one ayeh!",
	body="Well what can I say, it's just another post. Deal with it",
	author="Aniket Atram",
	img_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpaperaccess.com%2Ffull%2F36322.jpg&f=1&nofb=1&ipt=3e747b471f44c1826c125b1e7e32294d5434a785c90d7617e381f1f801d85f7e")

third_post = Post(
	title="Third Post",
	subtitle="I feel ALIVE!",
	body="Ok OK I'll stop now.",
	author="Aniket Atram",
	img_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapers.com%2Fimages%2Fhd%2Friver-mountain-most-beautiful-nature-hdb30wtkjbn08xlf.jpg&f=1&nofb=1&ipt=d565c208c0dddd96060a6f963695516068df4839bbc7583b4001b1df0f0a635a")

with app.app_context():

	db.session.query(Post).delete()
	db.session.add(first_post)
	db.session.add(second_post)
	db.session.add(third_post)
	db.session.commit()
	print("Data added successfully")