#!/bin/bash
set -exuo pipefail

docker build -t postgres-db-deployment:1.0 .
kind load docker-image postgres-db-deployment:1.0