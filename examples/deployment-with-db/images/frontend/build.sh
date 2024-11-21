#!/bin/bash
set -exuo pipefail

docker build -t frontend-db-deployment:1.0 .
kind load docker-image frontend-db-deployment:1.0
