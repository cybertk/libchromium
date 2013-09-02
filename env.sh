#!/bin/sh

GYP_DEFINES="OS=ios"
GYP_GENERATORS=

export GYP_DEFINES
export GYP_GENERATORS

CHROMIUM_PATH=`pwd`/chromium/tools/depot_tools

# Clear the path first
PATH=${PATH/$CHROMIUM_PATH:/}

# Setup
export PATH=$CHROMIUM_PATH:$PATH
