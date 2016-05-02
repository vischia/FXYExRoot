#!/bin/bash

PARALLEL=${1}
DOPAR=""

if [ ${PARALLEL} -eq 1 ]
   then
    DOPAR="&"
fi

echo "DOPAR IS ${DOPAR}"

for i in `find ../Rui_ilc/ -maxdepth 2 -type d -name 'run_*' | grep Events`
    do
        python GenAnalysis.py -b -i ${i} &
    done

for i in `find ../Rui_cepc/ -maxdepth 2 -type d -name 'run_*' | grep Events`
    do
        python GenAnalysis.py -b -i ${i} &
    done
exit 0
