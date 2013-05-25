source /home/workspace-django/virtualenvs/ironika-fondstamp/bin/activate
cd /home/workspace-django/projects/ironika-fondstamp/fondstamp/
fab live prepare_deploy
fab live deploy
deactivate
