from flask import Flask
from datetime import datetime

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='template'
)


@app.route('/')
def hello_world():
    now = datetime.now()
    return f'Hello, World! {now.strftime("%Y%m/%d %H:%M:%S")}'


if __name__ == '__main__':
    app.run()
