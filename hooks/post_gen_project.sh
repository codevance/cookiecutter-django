mv {{ cookiecutter.directory_name }}/* . >> /tmp/cookiecutter_post_gen.log 2>> /tmp/cookiecutter_post_gen.log
mv {{ cookiecutter.directory_name }}/.* . >> /tmp/cookiecutter_post_gen.log 2>> /tmp/cookiecutter_post_gen.log
rmdir {{ cookiecutter.directory_name }} >> /tmp/cookiecutter_post_gen.log 2>> /tmp/cookiecutter_post_gen.log