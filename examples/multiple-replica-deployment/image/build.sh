#!/bin/bash
set -exuo pipefail

docker build -t multiple-replica-deployment:1.0 .
kind load docker-image multiple-replica-deployment:1.0