source ~/cambieri.it/work/workspace-django/virtualenvs/ironika-fondstamp/bin/activate
cd ~/cambieri.it/work/workspace-django/projects/ironika-fondstamp/fondstamp/
fab live prepare_deploy
fab live deploy
deactivate
