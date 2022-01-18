from flask import Flask

app = Flask(__name__)


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return f"Blog Number {postID}"


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return f"Revision Number {revNo}"


if __name__ == '__main__':
    app.run()
