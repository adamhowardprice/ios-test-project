#!/usr/bin/env python

import os
import fnmatch
import json
import subprocess
import argparse

# Glob for all files called "ci-mapping.json"
# Use them to run the following command
# env git --no-pager diff --name-only HEAD~1 ${BUILDKITE_COMMIT}" | \
#     grep -vE "${exclude_regex}" | \
#     grep -E "${include_regex}" > /dev/null
#
# Note: base commit comes from: git ls-remote origin -h refs/heads/master
#
# If any of them return exit code 0,
# Run their script in that directory


def get_default_base():
    output = subprocess.check_output(
        "git ls-remote origin -h refs/heads/master | cut -f 1", shell=True)
    return output.replace('\n', '')


def get_default_head():
    output = subprocess.check_output("git log -1 --format=%H", shell=True)
    return output.replace('\n', '')


def is_affected(directory, includes, excludes, base, head):
    cmd = "git --no-pager diff --name-only {0}..{1}".format(base, head)
    for e in excludes:
        cmd = cmd + " | grep -rvE {0}".format(os.path.join(directory, e))
    for i in includes:
        cmd = cmd + " | grep -rE {0}".format(os.path.join(directory, i))
    exit_code = subprocess.call(cmd, shell=True)
    return exit_code != 0


def run_script_if_affected(directory, project, includes, excludes,
                           script, base, head):
    if is_affected(directory, includes, excludes, base, head):
        print("Found changes in " + directory +
              ", running {0}/{1}".format(directory, script))
        subprocess.call(script, cwd=directory)


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-b", "--base",
                        help="The base commit", action="store_true",
                        default=get_default_base())
    parser.add_argument("-h", "--head",
                        help="The head commit", action="store_true",
                        default=get_default_head())
    args = parser.parse_args()

    for root, dirnames, filenames in os.walk('.'):
        for filename in fnmatch.filter(filenames, 'ci-mapping.json'):
            directory = str(root.split("./")[1])
            with open(os.path.join(root, filename)) as j:
                m = json.load(j)
                for project, mapping in m.items():
                    includes = mapping.get('includes')
                    excludes = mapping.get('excludes')
                    script = mapping.get('script')
                    run_script_if_affected(directory, project, includes,
                                           excludes, script, args.base,
                                           args.head)

if __name__ == '__main__':
    main()
