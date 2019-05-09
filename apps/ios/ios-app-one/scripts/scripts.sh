#!/usr/bin/env bash

set -o pipefail

xcodebuild \
    -project TestIOSProject.xcodeproj \
    -scheme TestIOSProject \
    -destination "platform=iOS Simulator,name=iPhone X,OS=12.1" \
    clean test