#!/bin/bash
set -exuo pipefail

docker build -t backend-db-deployment:1.0 .
kind load docker-image backend-db-deployment:1.0