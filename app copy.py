from flask import Flask, render_template
from datetime import datetime

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static'
)


@app.route('/')
def hello_world():
    now = datetime.now()
    return f'Hello, World! {now.strftime("%Y%m/%d %H:%M:%S")}'


@app.route('/home')
def my_home():
    myVar = "test from my home"
    return render_template('test.html', page_var=myVar)

# if __name__ == '__main__':
#     app.run()
