from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return ('Hello, World!')


# (lưu ý là 2 dấu gạch dưới _ ở mỗi vị trí name và main)
if __name__ == "__main__":
    app.run()


