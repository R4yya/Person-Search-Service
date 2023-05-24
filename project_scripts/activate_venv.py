import os

venv_path = "presonsearchenv"
activate_this = os.path.join(venv_path, "bin", "activate_this.py")

# Активация виртуального окружения
exec(open(activate_this).read(), {'__file__': activate_this})
