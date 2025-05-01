#!/bin/bash

# Load .env
set -a
. .env
set +a

# Check: show loaded vars
echo "SSH_HOST=$SSH_HOST"
echo "SSH_PORT=$SSH_PORT"
echo "SSH_USER=$SSH_USER"
echo "SSH_TARGET_DIR=$SSH_TARGET_DIR"


# Pass them into Make
make "$@" \
  SSH_HOST="$SSH_HOST" \
  SSH_PORT="$SSH_PORT" \
  SSH_USER="$SSH_USER" \
  SSH_TARGET_DIR="$SSH_TARGET_DIR" \

