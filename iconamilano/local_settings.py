# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "-jby10ycjm5cbc$ncp4xs0gfq#=hd(@&u7-9z-8rx$vo^%qmln"
NEVERCACHE_KEY = "i^#!889g-s+#+7krwdt1&tb!77z6(v6t&fcixlmw4o__!yzqm1"

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
ALLOWED_HOSTS = ["*"]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}