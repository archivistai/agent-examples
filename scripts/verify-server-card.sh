#!/usr/bin/env bash
set -euo pipefail

SERVER_CARD_URL="${SERVER_CARD_URL:-https://mcp.myarchivist.ai/.well-known/mcp/server-card.json}"
EXPECTED_MIN_TOOLS="${EXPECTED_MIN_TOOLS:-27}"

echo "Fetching server card from ${SERVER_CARD_URL}..."

if ! body="$(curl -fsSL "${SERVER_CARD_URL}")"; then
  echo "FAIL: Could not fetch server card"
  exit 1
fi

tool_count="$(echo "${body}" | python3 -c "import json,sys; print(len(json.load(sys.stdin).get('tools',[])))")"
echo "Tool count: ${tool_count}"

if [ "${tool_count}" -lt "${EXPECTED_MIN_TOOLS}" ]; then
  echo "FAIL: Expected at least ${EXPECTED_MIN_TOOLS} tools, found ${tool_count}"
  exit 1
fi

missing="$(echo "${body}" | python3 -c "
import json, sys
data = json.load(sys.stdin)
missing = []
for t in data.get('tools', []):
    name = t.get('name', '?')
    if not t.get('title'):
        missing.append(f'{name}: missing title')
    ann = t.get('annotations') or {}
    if not ann.get('readOnlyHint') and not ann.get('destructiveHint'):
        missing.append(f'{name}: missing readOnlyHint/destructiveHint')
if missing:
    print('\n'.join(missing))
")"

if [ -n "${missing}" ]; then
  echo "FAIL: Annotation issues:"
  echo "${missing}"
  exit 1
fi

auth="$(echo "${body}" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('authentication',{}))")"
echo "Authentication: ${auth}"

echo "PASS: Server card valid (${tool_count} tools, all annotated)"
