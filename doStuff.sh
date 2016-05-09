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


python runBatch.py -c cepc_bb -n 8 
python runBatch.py -c ilc_bb  -n 8 

python runBatch.py -c cepc_gg -n 8 -g
python runBatch.py -c ilc_bb  -n 8 -g

python GenDisplay.py -o plots/ -c cepc -b -t 2
python GenDisplay.py -o plots/ -c ilc  -b -t 2

python GenDisplay.py -o plots/ -c cepc -b -t 5
python GenDisplay.py -o plots/ -c ilc  -b -t 5

python GenDisplay.py -o plots/ -c cepc -b -t 10
python GenDisplay.py -o plots/ -c ilc  -b -t 10

python GenDisplay.py -o plots/ -c cepc -b -t 50
python GenDisplay.py -o plots/ -c ilc  -b -t 50

python plotXsec.py -b 

