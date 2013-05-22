from fabric.api import *
from fabric.contrib import project

"""
In order to deploy, run "fab <env> deploy"
"""

# Config. Adjust these settings according to your server
# If you need to specify a file system path, please add a trailing slash
config = {
    'live': {
        'server': 'root@cmbhosting.no-ip.biz',
        'django': {
            'site_dir_name': 'ironika-fondstamp-live',
            'site_root': '/opt/django/sites/ironika-fondstamp-live/',
            'project_dir_name': 'fondstamp',
            'project_root': '/opt/django/sites/ironika-fondstamp-live/fondstamp/',
            'settings_module': 'fondstamp.settings.live'
        },
        'virtualenv': {
            'path': '/opt/django/virtualenvs/ironika-fondstamp-live/',
            'requirements_file': '/opt/django/sites/ironika-fondstamp-live/requirements/requirements_live.txt',
        },
        'git': {
            'server_name': 'origin',
            'branch_name': 'live',
        },
        'webserver': {
            'touch_file': '/opt/django/sites/ironika-fondstamp-live/uwsgi/live/django_wsgi.py'
        }
    },
    'stage': {
        'server': 'root@cmbhosting.no-ip.biz',
        'django': {
            'site_dir_name': 'ironika-fondstamp',
            'site_root': '/opt/django/sites/ironika-fondstamp-stage/',
            'project_dir_name': 'fondstamp',
            'project_root': '/opt/django/sites/ironika-fondstamp-stage/fondstamp/',
            'settings_module': 'fondstamp.settings.stage'
        },
        'virtualenv': {
            'path': '/opt/django/virtualenvs/ironika-fondstamp-stage/',
            'requirements_file': '/opt/django/sites/ironika-fondstamp-stage/requirements/requirements_live.txt',
        },
        'git': {
            'server_name': 'origin',
            'branch_name': 'stage',
        },
        'webserver': {
            'touch_file': '/opt/django/sites/ironika-fondstamp-stage/uwsgi/stage/django_wsgi.py'
        }
    }
}

# Environments. Add as much as you defined in "config"
def stage():
    env.environment = 'stage'
    env.hosts = [config[env.environment]['server']]

def live():
    env.environment = 'live'
    env.hosts = [config[env.environment]['server']]

### Fab Tasks

def prepare_deploy():
    with lcd('/home/workspace-django/projects/ironika-fondstamp/fondstamp'):
		local("python2 ./manage.py test main")
    with lcd('/home/workspace-django/projects/ironika-fondstamp'):
		local("git checkout master")
		local("git add -A && git commit")
		local("git push")
		local("git checkout live")
		local("git merge master")
		local("git push")
		local("git checkout master")
    
def deploy():
    """
    Deploy, migrate, collect static files, restart webserver
    """
    _git_pull()
    _migrate()
    _collect_static_files()
    _restart_webserver()

# Install requirements
def install_requirements():
    """
    This is basically the same as deployment, but additionally
    installs the requirements.
    Important: Migrations are executed too!
    """
    _git_pull()
    _install_requirements()
    _syncdb()
    _migrate()
    _restart_webserver()


### Helpers

def __activate():
    return 'export LANG=it_IT.UTF-8 && source {0}bin/activate && export DJANGO_SETTINGS_MODULE={1} && export PYTHONPATH={2}'.format(
        config[env.environment]['virtualenv']['path'],
        config[env.environment]['django']['settings_module'],
        config[env.environment]['django']['site_root'],
        )

def __deactivate():
    return 'deactivate'

def _git_pull():
    with cd(config[env.environment]['django']['site_root']):
        # git reset --hard HEAD
        run('git pull {0} {1}'.format(
            config[env.environment]['git']['server_name'],
            config[env.environment]['git']['branch_name'])
        )

def _migrate():
    with cd(config[env.environment]['django']['project_root']):
        run(
            __activate() + \
            '&& django-admin.py migrate && ' + \
            __deactivate()
        )

def _syncdb():
    with cd(config[env.environment]['django']['project_root']):
        run(
            __activate() + \
            '&& django-admin.py syncdb && ' + \
            __deactivate()
        )

def _collect_static_files():
    with cd(config[env.environment]['django']['project_root']):
        run(
            __activate() + \
            '&& django-admin.py collectstatic --noinput && ' + \
            __deactivate()
        )

def _restart_webserver():
    run('touch {0}'.format(config[env.environment]['webserver']['touch_file']))

def _install_requirements():
    with cd(config[env.environment]['django']['site_root']):
        run(
            __activate() + \
            '&& pip install -r {0} && '.format(config[env.environment]['virtualenv']['requirements_file']) + \
            __deactivate()
        )
