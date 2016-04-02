#!/usr/bin/env python
#http://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running

import subprocess
import sys

def execute(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() != None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()

    output = process.communicate()[0]
    exitCode = process.returncode

    if (exitCode == 0):
        return output
    else:
        raise ProcessException(command, exitCode, output)

execute("while true; do echo 'wait' ; sleep 5 ; done")
