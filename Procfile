redis:            redis-server ./redis.conf
api:              PYTHONPATH=$PYTHONPATH:. shamester-api --debug --conf=shamester_api/config/local.conf
web:              cd shamester-web && grunt server
