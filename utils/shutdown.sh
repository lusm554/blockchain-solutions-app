#!/bin/bash
docker-compose -p flask-app down
rm -rf pgdata
docker volume prune --force
