#!/bin/bash

PARALLEL=${1}
DOPAR=""
if [ "${PARALLEL}" == "1" ]; then
    DOPAR="&"
fi
for i in `find ../Rui_ilc/ -maxdepth 2 -type d -name 'run_*' | grep Events`
    do
        python GenAnalysis.py -b -i ${i} ${DOPAR}
    done

for i in `find ../Rui_cepc/ -maxdepth 2 -type d -name 'run_*' | grep Events`
    do
        python GenAnalysis.py -b -i ${i} ${DOPAR}
    done
exit 0
