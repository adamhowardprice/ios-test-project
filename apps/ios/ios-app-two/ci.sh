#!/usr/bin/env bash

set -o pipefail

xcodebuild \
    -project TestIOSProjectTwo.xcodeproj \
    -scheme TestIOSProjectTwo \
    -destination "platform=iOS Simulator,name=iPhone X,OS=12.1" \
    clean test
