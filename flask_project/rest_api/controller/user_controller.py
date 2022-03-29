from app import app
from model.user_model import user_contoller_model
from flask import request

obj = user_contoller_model()


@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()


@app.route("/user/addone", methods=["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form)


@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    print(request.form)
    return obj.user_update_model(request.form)


@app.route("/user/delete/<id>", methods=["DELETE"])
def user_delete_controller(id):
    print(request.form)
    print(id)
    return obj.user_delete_model(id)


if __name__ == '__main__':
    app.run(debug=True)
