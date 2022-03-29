from app import app


@app.route("/product/category/add")
def pcat_add():
    return "This is product category page"


if __name__ == '__main__':
    app.run(debug=True)