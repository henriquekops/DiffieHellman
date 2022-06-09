#!/bin/bash

check_command() {
    command_name=$1
    
    echo -n "checking for '$command_name'..."
    if command -v $command_name >/dev/null 2>&1
    then
        echo  'ok'
    else
        echo "failed: '$command_name' not installed!"
        exit 0
    fi
}

check_command $@
