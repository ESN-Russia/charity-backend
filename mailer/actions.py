from .base import send_message, render_message


def send_password(user, password):
    message = render_message("password.html", user_name=user.first_name, password=password)
    send_message(user.email, "Here is your password!", message)
