"""
Decorator that configures the template to auto-render a dictionary with a specific view with its associated data

example:
@app.route('/')
@response(template_file='home/index.html')

def index():
    # .....
    return {'packages': top_ten_list}
"""
from functools import wraps

import flask
import werkzeug
import werkzeug.wrappers


def response(*, mimetype: str = None, template_file: str = None):
    def response_inner(f):
        # print("Wrapping in response {}".format(f.__name__), flush=True)

        @wraps(f)
        def view_method(*args, **kwargs):
            response_val = f(*args, **kwargs)

            if isinstance(response_val, werkzeug.wrappers.Response):
                return response_val

            if isinstance(response_val, flask.Response):
                return response_val

            if isinstance(response_val, dict):
                model = dict(response_val)
            else:
                model = dict()

            if template_file and not isinstance(response_val, dict):
                raise Exception(
                    "Invalid return type {}, we expected a dict as the return value.".format(type(response_val)))

            if template_file:
                response_val = flask.render_template(template_file, **response_val)

            resp = flask.make_response(response_val)
            resp.model = model
            if mimetype:
                resp.mimetype = mimetype

            return resp

        return view_method

    return response_inner
