from flask import Flask, render_template

app = Flask(__name__)

# Mock data for blog posts _test_
posts = [
    {
        'title': 'First post',
        'content': 'This is the content of the first post.'
    },
    {
        'title': 'Second post',
        'content': 'This is the content of the second post.'
    }
]

# Route to display blog posts
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

