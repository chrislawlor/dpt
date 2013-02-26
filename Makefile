#
# Compile LESS to CSS. Requires lessc (npm install -g less)
#
build:
	lessc -x --verbose --line-numbers=comments static/assets/less/style.less > static/assets/css/style.css

#
# Collect static files to STATIC_ROOT
#
collect:
	python apps/manage.py collectstatic --noinput --ignore *.less

#
# Clean up prior builds
#
clean:
	rm -rf static/_build*
	rm static/assets/css/style.css

#
# Watch LESS files. Requires watchr ( gem install watchr )
#
watch:
	echo "Watching less files...."; \
	watchr -e "watch('static/assets/less/.*\.less') { system 'make' }"

#
# Run Unit tests
#
test:
	coverage run apps/manage.py test --settings=project.settings.test; \
	coverage html --include="./apps/*" --omit="admin.py,./apps/project/settings/*"; \
	echo "Open htmlcov/index.html to see the test coverage report.";

#
# Shell
#
shell:
    python apps/manage.py shell_plus --settings=project.settings.local

#
# Run syncdb
#
db:
    python apps/manage.py syncdb --migrate --settings=project.settings.local

#
# Run the devserver
#
server:
    python apps/manage.py runserver --settings=project.settings.local


.PHONY : clean static build watch test db server