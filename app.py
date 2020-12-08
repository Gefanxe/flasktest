from flask import Flask
app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='template'
)


@app.route('/')
def hello_world():
    myName = 'Andersen'
    return f'Hello, World! {myName}'


if __name__ == '__main__':
    app.run()
