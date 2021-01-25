from app import app
from flask import request, render_template

@app.route('/', methods=['post', 'get'])
def home():
    message = ''
    print(123)
    if request.method == 'POST':
        # регистрация
        if 'do_reg' in request.form:
            name = request.form.get('namereg')  # запрос к данным формы
            mail_reg = request.form.get('mailreg')
            password1 = request.form.get('passreg')
            password2 = request.form.get('passreg2')
            print(1)
        # вход
        elif 'do_login' in request.form:
            mail_auth = request.form.get('logauth')
            password_auth = request.form.get('passauth')
            print(2)

    return render_template('index.html')