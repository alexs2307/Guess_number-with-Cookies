import random

from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    secret_number = request.cookies.get("secret_number")
    response = make_response(render_template("index.html"))
    if not secret_number:
        guess_number = random.randint(1, 30)
        response.set_cookie("secret_number", str(guess_number))

    return response

@app.route("/result", methods=["POST"])
def result():
    user_guess = int(request.form.get("user_guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if user_guess == None:
        return make_response(render_template("index.html"))

    if secret_number == user_guess:
        message = f"Bingo! The secret number is {secret_number}."
        response = make_response(render_template("result.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))

        return response
    if secret_number < user_guess:
        message = "Wrong! Try smaller!"
        response = make_response(render_template("result.html", message=message))
        return response

    if secret_number > user_guess:
        message = "Wrong! Try bigger!"
        response = make_response(render_template("result.html", message=message))
        return response

    if __name__ == '__main__':
        app.run(use_reloader=True)
@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        print(user_name)

        return render_template("about.html", name=user_name)
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)

        return response

if __name__ == '__main__':
    app.run(use_reloader=True)
