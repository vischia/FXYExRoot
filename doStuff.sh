#!/bin/bash


if [ "$1" = "rootize" ]; then
    cd ../
    sh rootize.sh Rui_cepc_bb/
    sh rootize.sh Rui_ilc_bb/
    sh rootize.sh Rui_cepc_gg/
    sh rootize.sh Rui_ilc_gg/
    sh rootize.sh Rui_cepc_mumu/
    sh rootize.sh Rui_ilc_mumu/
    sh rootize.sh Rui_cepc_smbb/
    sh rootize.sh Rui_cepc_smmumu/
    sh rootize.sh Rui_ilc_smbb/
    sh rootize.sh Rui_ilc_smmumu/
    cd -
elif  [ "$1" = "getxsec" ]; then
    echo "ILC bb " > xsecs.log
    python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_ilc_bb/crossx.html >> xsecs.log
    echo "CEPC bb " >> xsecs.log
    python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_cepc_bb/crossx.html >> xsecs.log
    echo "ILC gg " >> xsecs.log
    python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_ilc_gg/crossx.html >> xsecs.log
    echo "CEPC gg " >> xsecs.log
    python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_cepc_gg/crossx.html >> xsecs.log
    echo "CEPC mumu " >> xsecs.log
    python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_cepc_mumu/crossx.html >> xsecs.log
    echo "ILC mumu " >> xsecs.log
    python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_ilc_mumu/crossx.html >> xsecs.log
    echo "CEPC smbb " >> xsecs.log
    python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_cepc_smbb/crossx.html >> xsecs.log
    echo "CEPC smmumu " >> xsecs.log
    python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_cepc_smmumu/crossx.html >> xsecs.log
    echo "ILC smbb " >> xsecs.log
    python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_ilc_smbb/crossx.html >> xsecs.log
    echo "ILC smmumu " >> xsecs.log
    python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_ilc_smmumu/crossx.html >> xsecs.log
elif  [ "$1" = "runbatch" ]; then
    python runBatch.py -c cepc_bb -n 4 
    python runBatch.py -c ilc_bb  -n 4 
    python runBatch.py -c cepc_gg -n 4 
    python runBatch.py -c ilc_bb  -n 4 
    python runBatch.py -c cepc_mumu   -n 4 
    python runBatch.py -c ilc_mumu    -n 4 
    python runBatch.py -c cepc_smbb   -n 4 
    python runBatch.py -c cepc_smmumu -n 4
    python runBatch.py -c ilc_smbb    -n 4
    python runBatch.py -c ilc_smmumu  -n 4 
elif  [ "$1" = "display" ]; then
    python GenDisplay.py -o plots/ -c cepc -b -z bb -t 2
    python GenDisplay.py -o plots/ -c ilc  -b -z bb -t 2
    python GenDisplay.py -o plots/ -c cepc -b -z bb -t 5
    python GenDisplay.py -o plots/ -c ilc  -b -z bb -t 5
    python GenDisplay.py -o plots/ -c cepc -b -z bb -t 10
    python GenDisplay.py -o plots/ -c ilc  -b -z bb -t 10
    python GenDisplay.py -o plots/ -c cepc -b -z bb -t 50
    python GenDisplay.py -o plots/ -c ilc  -b -z bb -t 50

    python GenDisplay.py -o plots/ -c cepc -b -z mumu -t 2
    python GenDisplay.py -o plots/ -c ilc  -b -z mumu -t 2
    python GenDisplay.py -o plots/ -c cepc -b -z mumu -t 5
    python GenDisplay.py -o plots/ -c ilc  -b -z mumu -t 5
    python GenDisplay.py -o plots/ -c cepc -b -z mumu -t 10
    python GenDisplay.py -o plots/ -c ilc  -b -z mumu -t 10
    python GenDisplay.py -o plots/ -c cepc -b -z mumu -t 50
    python GenDisplay.py -o plots/ -c ilc  -b -z mumu -t 50

elif  [ "$1" = "plotxsec" ]; then
    python plotXsec.py -b 
fi
