#!/bin/bash

name="Asantewa"

echo "Hello, $name"
echo "Current date and time: $(date)"

mkdir -p session_logs

logfile="session_logs/$(date +%F).log"

echo "Name: $name" >> "$logfile"
echo "Note: Workspace setup run completed." >> "$logfile"

echo "Setup complete!"
