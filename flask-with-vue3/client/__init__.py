from flask import Blueprint, render_template

client = Blueprint('client', __name__,  # 'Client Blueprint'
                   template_folder='templates',  # Required for our purposes
                   static_folder='static',  # Again, this is required
                   static_url_path='/client/static'  # Flask will be confused if you don't do this
                   )


@client.route('/')
def index():
    return render_template('index.html')
