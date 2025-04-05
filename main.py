import os
from app import app
from auth import auth_bp
from routes import register_routes

# Configure the upload folder
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Register auth blueprint
app.register_blueprint(auth_bp)

# Register all routes
register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)