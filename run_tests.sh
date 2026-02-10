#!/usr/bin/env bash

set -e

echo "Activating virtual environment..."
source venv/Scripts/activate

echo "Ensuring ChromeDriver is available..."

# Get driver path using webdriver-manager

DRIVER_PATH=$(python - <<END
from webdriver_manager.chrome import ChromeDriverManager
print(ChromeDriverManager().install())
END
)

# Add directory to PATH

export PATH="$PATH:$(dirname "$DRIVER_PATH")"

echo "Running tests..."
pytest

RESULT=$?

if [ $RESULT -eq 0 ]; then
echo "✅ Tests passed"
exit 0
else
echo "❌ Tests failed"
exit 1
fi
