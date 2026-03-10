from app import create_app
from datetime import datetime

app = create_app()

# @app.context_processor
# def inject_current_year():
# 	return {'current_year': datetime.utcnow().year}

if __name__ == "__main__":

	app.run(debug=True)