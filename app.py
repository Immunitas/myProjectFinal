from flask_mail import Mail, Message  # flask email config
from flask import Flask, request
app = Flask("logic")

# Define a function that reads and returns the content of an HTML file


def get_html(page_name):
    html_file = open('templates/HTML/' + page_name +
                     '.html')  # open an HTML file
    content = html_file.read()  # read the content of the HTML file
    html_file.close()  # closing the HTML file
    return content  # returning the content of the HTML file


@app.route("/")  # return the content of the index route
def homepage():
    return get_html("index")


@app.route("/projects")  # return the content of projects route
def projects():
    return get_html("projects")


@app.route("/activities")  # return the content of activities route
def activities():
    return get_html("activities")


@app.route("/publications")  # return the content of publications route
def publications():
    return get_html("publications")


@app.route("/contact")  # return the content of the contact route
def contact():
    return get_html("contact")


# send email
@app.route("/send_email", methods=['POST'])
def send_email():
    # functionalities to recuperate infos and send email
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    # we have extracted all the data from the POST request
    process_message(name, email, message)

    return "Thank you for your message"


def process_message(name, email, message):
    print("We received a new comment", name, email, message)
# Instead of print we could use the Flask logging framework
