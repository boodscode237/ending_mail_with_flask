from flask import Flask
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # for gmail
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'Your_email_account'
app.config['MAIL_PASSWORD'] = 'Your_password'
app.config['MAIL_DEFAULT_SENDER'] = ("The_name_you_want_to_display", "Your_email_account")
app.config['MAIL_MAX_EMAILS'] = None
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

Bootstrap(app)

mail = Mail(app)

# mail = Mail()
# mail.init_app(app)

@app.route('/')
def index():
    msg = Message("Title", recipients=['recipient_email'])
    msg.add_recipient('another_way_to_add_email')
    msg.body = ' '
    msg.html = '<b>This is the body of the email sent from EKB no need to reply</b>'
    with app.open_resource('ninja.png') as ninja:
        msg.attach('ninja.png', 'image/png', ninja.read())

    mail.send(msg)

    msg = Message(
        subject='',
        recipients=[],
        body='',
        html='',
        sender='',
        cc=[],
        bcc=[],
        attachments=[],
        reply_to=[],
        date='date',
        charset='',
        extra_headers={'': ''},
        mail_options=[],
        rcpt_options=[]

    )

    return "message has been send"

@app.route('/bulk')
def bulk():
    users = [{
        'name': 'Recipient name',
        'email': 'recipient_email'
    }]

    with mail.connect() as conn:
        for user in users:
            msg = Message("Title_of_email", recipients=[user['email']])
            msg.body = 'Body of your email'
            conn.send(msg)

    return "message has been send"


if __name__ == '__main__':
    app.run(debug=True)
