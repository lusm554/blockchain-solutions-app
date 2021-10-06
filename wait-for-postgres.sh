#!/bin/sh
# wait-for-postgres.sh

set -e
  
host="$1"
shift
  
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U "postgres" -c "\q"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "Server starting in $QUART_ENV mode"
if [ "$QUART_ENV" == "production" ]; then
  hypercorn main:app -b 0.0.0.0:80
  exit 0
fi

quart run --host 0.0.0.0 --port 80
