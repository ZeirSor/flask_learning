from werkzeug.serving import run_simple

class Flask(object):

    def __call__(self, *args, **kwargs):
        print("请求来了")
        return "Hello world"

app = Flask()


if __name__ == '__main__':
    run_simple('127.0.0.1', 5000, app)