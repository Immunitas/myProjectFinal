from flask_mail import Mail, Message  # flask email config
from flask import Flask, request
app = Flask("logic")


def get_html(page_name):
    html_file = open('templates/HTML/' + page_name + '.html')
    content = html_file.read()
    html_file.close()
    return content


@app.route("/")
def homepage():
    return get_html("index")


@app.route("/projects")
def projects():
    return get_html("projects")


@app.route("/activities")
def activities():
    return get_html("activities")


@app.route("/publications")
def publications():
    return get_html("publications")


@app.route("/contact")
def contact():
    return get_html("contact")


# send email


@app.route("/send_email", methods=['POST'])
def send_email():
    # faire les functionalités pour recuperer les infos et envoyer email
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    # we have extracted all the data from the POST request
    process_message(name, email, message)

    return "Thank you for your message"


def process_message(name, email, message):
    print("We received a new comment", name, email, message)
# Use Flask logging framework
