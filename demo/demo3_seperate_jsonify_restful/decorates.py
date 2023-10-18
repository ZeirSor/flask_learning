from functools import wraps

from flask import redirect, url_for, request, g

# def login_required(func):
#     """
#     Decorator to check if the user is logged in.
#     """
#     @wraps(func)
#     def inner(*args, **kwargs):
#         if g.user:
#             return func(*args, **kwargs)
#         else:
#             return redirect(url_for('auth.login'))
#     return inner


# @login_required
# def public_question(quesiton_id):
#     pass
# login_required(public_question)(question_id)
