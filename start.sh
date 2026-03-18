#!/bin/bash
set -e
echo "Starting AI-Powered Health Diagnosis Assistant..."
uvicorn app:app --host 0.0.0.0 --port 9054 --workers 1
