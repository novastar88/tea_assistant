#!/bin/sh

echo "Waiting for backend..."

while ! nc -z $NEXT_PUBLIC_API_URL $NEXT_PUBLIC_API_PORT; do
  sleep 0.1
done

echo "backend started"

exec "$@"
