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
    # faire functionalite pour recuperer les infos et envoyer email
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    recipients = ['zivtav@gmail.com']
    return name + " " + email + message


# user contact form
@app.route("/contact_form", methods=["GET", "POST"])
def contact_form():
    message = Message(
        subject=(request.form['Email'] + " want to contact you via web"),
        sender=request.form['Email'],
        recipients=['zivtav@gmail.com'],
        body=request.form['Message']
    )

# configurer email


def create_email(name, email, message):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = zivtav@gmail.com
    app.config['MAIL_PASSWORD'] = xxxxx
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)
