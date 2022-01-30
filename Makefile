constraints:
	pip freeze --all > constraints.txt

format:
	./pants tailor --check update-build-files
	./pants fmt ::

lint:
	./pants tailor --check update-build-files --check
	./pants lint ::

test:
	./pants test ::