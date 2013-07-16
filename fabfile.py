import posixpath
from fabric.api import env, run, cd, prefix, require
from contextlib import contextmanager as _contextmanager


def develop():
    env.hosts = ['example.com']
    env.directory = "/home/username/webapps/{{ project_name }}/src/"

    venv_root = "/home/username/.virtualenvs/{{ project_name }}/"
    env.venv_activate = posixpath.join(venv_root, 'bin', 'activate')
    env.env_vars = posixpath.join(venv_root, 'bin', 'postactivate')

    env.restart_appserver_script = '/home/username/webapps/{{ project_name }}/apache2/bin/restart'
    env.user = 'username'


TARGETS = ['develop']


@_contextmanager
def env_vars():
    require('env_vars', provided_by=TARGETS)
    with prefix("source %(env_vars)s" % env):
        yield


@_contextmanager
def virtualenv():
    require('directory', 'venv_activate', provided_by=TARGETS)
    with cd(env.directory):
        with prefix("source %(venv_activate)s" % env):
            with env_vars():
                yield


def checkout_head():
    """
    Checkout the specified revision, or HEAD
    """
    require('directory', provided_by=TARGETS)
    with cd(env.directory):
        run("git pull")


def restart_appserver():
    """
    Restart the application server.
    """
    require('restart_appserver_script', provided_by=TARGETS)
    with virtualenv():
        run(env.restart_appserver_script)


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
    restart_appserver()


def quick_deploy():
    """
    Just do a fresh checkout and restart the appserver.
    """
    checkout_head()
    restart_appserver()
