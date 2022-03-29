from app import app


@app.route("/product/add")
def padd():
    return "This is product add page"


if __name__ == '__main__':
    app.run(debug=True)