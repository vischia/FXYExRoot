#!/bin/bash

for i in `find ../Rui_ilc/ -maxdepth 2 -type d -name 'run_*' | grep Events`
    do
        python GenAnalysis.py -i ${i}
    done

for i in `find ../Rui_cepc/ -maxdepth 2 -type d -name 'run_*' | grep Events`
    do
        python GenAnalysis.py -i ${i}
    done
exit 0
