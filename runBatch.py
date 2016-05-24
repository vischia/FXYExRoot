import os
import sys
import optparse
import pickle
import json
import subprocess

"""
Wrapper to be used when run in parallel
"""
def RunMethodPacked(args):
    inputDir=args
    try:
        print 'Processing directory {inputDir}'.format(inputDir=inputDir)
        os.system('python GenAnalysis.py -b -i {inputDir}'.format(inputDir=inputDir))
    except :
        print 50*'<'
        print "  Problem  (%s) with %s continuing without"%(sys.exc_info()[1],inF)
        print 50*'<'
        return False
    return True

"""
"""
def main():


    #configuration
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('-c', '--collider',    dest='collider',    help='collider [ilc, cepc]',              default=None,       type='string')
    # Deactivated madspin
    #parser.add_option('-g', '--gluons',       dest='gluons',       help='h to gluons',                     default=False, action='store_true')
    parser.add_option('-n', '--njobs',       dest='njobs',       help='# jobs to run in parallel',                              default=0,           type='int')
    parser.add_option('-d', '--debug',       dest='debug',       help='Run in debug mode: verbosity verbosity verbosity',       default=False, action='store_true')

    (opt, args) = parser.parse_args()

    onlyList=[]
    try:
        onlyList=opt.only.split(',')
    except:
        pass


    # Redundant, task_list can be dirList
    task_list= []
    #dirList = subprocess.Popen(["find", "../Rui_{collider}/ -maxdepth 2 -type d -name 'run_*' | grep Events".format(collider=opt.collider)], stdout=subprocess.PIPE).communicate()[0]
    ###initList = os.listdir('../Rui_{collider}/Events/'.format(collider=opt.collider))

    initialDirectory='../'
    initList = os.listdir('{initialDirectory}Rui_{collider}/Events/'.format(initialDirectory=initialDirectory,collider=opt.collider))


    # Deactivated madspin
    #dirList = []
    #if opt.gluons:
    #    dirList = [x for x in initList if x.find("run") is not -1 ]
    #else:
    #    dirList = [x for x in initList if x.find("decayed") is not -1 ]
    dirList = [x for x in initList if x.find("run") is not -1 ]
    
    listCommand=""
    for inputDir in dirList:
        if inputDir.find('02') == -1 and inputDir.find('31') == -1 and inputDir.find('05') == -1 and inputDir.find('34') == -1 and inputDir.find('10') == -1 and inputDir.find('39') == -1 and inputDir.find('30') == -1 and inputDir.find('59') == -1 and inputDir.find('01') == -1:
            continue
        task_list.append( ('{initialDirectory}Rui_{collider}/Events/{inputDir}'.format(initialDirectory=initialDirectory,collider=opt.collider, inputDir=inputDir)) )


    #run the analysis jobs
    from multiprocessing import Pool
    pool = Pool(opt.njobs)
    pool.map(RunMethodPacked, task_list)



"""
for execution from another script
"""
if __name__ == "__main__":
    sys.exit(main())
