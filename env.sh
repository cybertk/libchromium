#!/bin/sh

# Get script dir.
SCRIPT_DIR=`pwd -P`/libchromium

if [ ! -d $SCRIPT_DIR ];
then
    echo 'Error: Invoke ". libchromium/env.sh" in top dir.'
    return
fi

GYP_DEFINES=
GYP_GENERATORS=

GYP_DEFINES+=" OS=ios"

export GYP_DEFINES
export GYP_GENERATORS

CHROMIUM_PATH=$SCRIPT_DIR/depot_tools

# Enable gyp syntax check.
export CHROMIUM_GYP_SYNTAX_CHECK=1

# Clear the path first
PATH=${PATH/$CHROMIUM_PATH:/}

# Setup
export PATH=$CHROMIUM_PATH:$PATH
