#!/bin/bash
docker-compose -p django-app down
rm -rf pgdata
docker volume prune --force
