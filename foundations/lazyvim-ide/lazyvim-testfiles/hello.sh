#!/usr/bin/env bash
# Test script for program runners.
# Safe, self-contained, and uses standard terminal output only.

echo "--- Program Runner Test Start ---"

# 1. Basic Output Test
echo "Status: Success"
echo "Bash Version: ${BASH_VERSION}"
echo "Unicode Check: ✅ 🚀"

# 2. Environment / Time Test
echo "Current Timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"

# 3. Simple Logic & Math Test
test_addition() {
  echo $(($1 + $2))
}

num1=5
num2=10
result=$(test_addition "$num1" "$num2")

echo "Math Check: ${num1} + ${num2} = ${result}"

if [ "$result" -eq 15 ]; then
  echo "Logic Check: PASSED"
else
  echo "Logic Check: FAILED"
fi

# Uncomment the next line to see how your runner shows an error.
# echo "Intentional test error" >&2; exit 1

echo "--- Program Runner Test End ---"
