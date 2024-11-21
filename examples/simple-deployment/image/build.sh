#!/bin/bash
set -exuo pipefail

docker build -t simpledeployment:1.0 .
kind load docker-image simpledeployment:1.0
