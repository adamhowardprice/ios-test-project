# Glob for all files called "ci-mapping.json"
# Use them to run the following command
# env git --no-pager diff --name-only HEAD~1 ${BUILDKITE_COMMIT}" | \
#     grep -vE "${exclude_regex}" | \
#     grep -E "${include_regex}" > /dev/null
#
# If any of them return exit code 0,
# Run their script in that directory
