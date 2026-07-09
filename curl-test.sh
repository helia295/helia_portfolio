#!/usr/bin/env bash

set -euo pipefail

BASE_URL="${BASE_URL:-http://127.0.0.1:5001}"
TIMESTAMP="$(date +%s)"
RANDOM_SUFFIX="${RANDOM}-${TIMESTAMP}"
NAME="curl-test-${RANDOM_SUFFIX}"
EMAIL="curl-test-${RANDOM_SUFFIX}@example.com"
CONTENT="Timeline API curl test created at ${TIMESTAMP}"

echo "Testing timeline API at ${BASE_URL}"

POST_RESPONSE="$(
    curl -sS -X POST "${BASE_URL}/api/timeline_post" \
        -d "name=${NAME}" \
        -d "email=${EMAIL}" \
        -d "content=${CONTENT}"
)"

POST_ID="$(
    python3 -c 'import json, sys; print(json.load(sys.stdin)["id"])' <<< "${POST_RESPONSE}"
)"

echo "Created timeline post ${POST_ID}"

GET_RESPONSE="$(curl -sS "${BASE_URL}/api/timeline_post")"

python3 - "${GET_RESPONSE}" "${POST_ID}" "${NAME}" "${EMAIL}" "${CONTENT}" <<'PY'
import json
import sys

response = json.loads(sys.argv[1])
post_id = int(sys.argv[2])
name = sys.argv[3]
email = sys.argv[4]
content = sys.argv[5]

for post in response["timeline_posts"]:
    if (
        post["id"] == post_id
        and post["name"] == name
        and post["email"] == email
        and post["content"] == content
    ):
        print(f"Verified timeline post {post_id} appears in GET response")
        break
else:
    raise SystemExit(f"Timeline post {post_id} was not found in GET response")
PY

DELETE_RESPONSE="$(curl -sS -X DELETE "${BASE_URL}/api/timeline_post/${POST_ID}")"

python3 - "${DELETE_RESPONSE}" "${POST_ID}" <<'PY'
import json
import sys

response = json.loads(sys.argv[1])
post_id = int(sys.argv[2])

if response["id"] != post_id:
    raise SystemExit(f"Expected DELETE response for {post_id}, got {response['id']}")

print(f"Deleted timeline post {post_id}")
PY

FINAL_GET_RESPONSE="$(curl -sS "${BASE_URL}/api/timeline_post")"

python3 - "${FINAL_GET_RESPONSE}" "${POST_ID}" <<'PY'
import json
import sys

response = json.loads(sys.argv[1])
post_id = int(sys.argv[2])

if any(post["id"] == post_id for post in response["timeline_posts"]):
    raise SystemExit(f"Timeline post {post_id} still exists after DELETE")

print("Cleanup verified")
PY

echo "Timeline API curl test passed"
