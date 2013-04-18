from fabric.api import env, run, cd, sudo, prefix
from contextlib import contextmanager as _contextmanager


def staging():
    env.hosts = ['app.domain.com']
    env.directory = "/path/to/project/root/"
    env.activate = 'source /path/to/virtualenv/activate'
    env.user = 'ubuntu'


@_contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield


def checkout_head():
    """
    Checkout the specified revision, or HEAD
    """
    with cd(env.directory):
        run("git pull")
        

def restart_gunicorn():
    """
    Restart the gunicorn server.
    """
    with cd(env.directory):
        sudo("supervisorctl restart {{ project_name }}:gunicorn")


def collectstatic():
    with virtualenv():
        run("python apps/manage.py collectstatic --noinput")


def install_requirements():
    with virtualenv():
        run("pip install -r requirements.txt")


def run_migrations():
    with virtualenv():
        run("python apps/manage.py migrate")


def deploy():
    checkout_head()
    install_requirements()
    run_migrations()
    collectstatic()
    restart_gunicorn()
