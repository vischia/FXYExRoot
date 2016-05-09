cd ../
sh rootize.sh Rui_cepc_bb/
sh rootize.sh Rui_ilc_bb/
sh rootize.sh Rui_cepc_gg/
sh rootize.sh Rui_ilc_gg/
cd -

python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_ilc_bb/crossx.html
python getXsecs.py -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_cepc_bb/crossx.html

python getXsecs.py -g -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_ilc_gg/crossx.html
python getXsecs.py -g -u file:///home/junzi/workarea/production/Production/MG5_aMC_v2_3_3/Rui_cepc_gg/crossx.html

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

