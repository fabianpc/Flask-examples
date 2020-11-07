from app import create_app

app = create_app('development')

@app.route('/')
def hello():
    return 'Hello, World!'