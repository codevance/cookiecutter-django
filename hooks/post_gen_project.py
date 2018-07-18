import os

os.system("mv {{ cookiecutter.directory_name }}/* .")
os.system("mv {{ cookiecutter.directory_name }}/.* .")
os.system("rmdir {{ cookiecutter.directory_name }}")