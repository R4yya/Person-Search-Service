import os

venv_path = "presonsearchenv"
activate_this = os.path.join(venv_path, "bin", "activate_this.py")


# Активация виртуального окружения
def activate_myvenv():
    exec(open(activate_this).read(), {'__file__': activate_this})
