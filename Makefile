mongodatabase = shamester

test: mongo_test
	@coverage run --branch `which nosetests` -vv --with-yanc -s shamester_api/tests/
	@coverage report -m --fail-under=80
	@cd shamester-web && grunt test

setup:
	@pip install -U -e .\[tests\]

drop_mongo:
	@rm -rf /tmp/$(mongodatabase)/mongodata

kill_mongo:
	@ps aux | awk '(/mongod/ && $$0 !~ /awk/){ system("kill -9 "$$2) }'

mongo: kill_mongo
	@mkdir -p /tmp/$(mongodatabase)/mongodata
	@mongod --dbpath /tmp/$(mongodatabase)/mongodata --logpath /tmp/$(mongodatabase)/mongolog --port 6666 --quiet &
	@sleep 3

restore_mongo:
	@mongorestore --port 6666 ../dump

kill_mongo_test:
	@ps aux | awk '(/mongod.+test/ && $$0 !~ /awk/){ system("kill -9 "$$2) }'

mongo_test: kill_mongo_test
	@rm -rf /tmp/$(mongodatabase)/mongotestdata && mkdir -p /tmp/$(mongodatabase)/mongotestdata
	@mongod --dbpath /tmp/$(mongodatabase)/mongotestdata --logpath /tmp/$(mongodatabase)/mongotestlog --port 6667 --quiet &
	@sleep 6

run: mongo
	@honcho start
