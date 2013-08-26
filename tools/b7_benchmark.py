import ah_config;
import benchmark;
import os.path;
import shutil;
import sys;

directory = 'tmp/'

if (len(sys.argv) < 2):
  print ("This script requires at least one parameter, namely the benchmark\n" +
    "you want to run, which is either prodcon or seqalt.")
  exit()

application = sys.argv[1]

if (len(sys.argv) >= 3):
  directory = sys.argv[2]

if (not directory.endswith('/')) :
  directory = directory + '/'

outputDir = directory
if (not directory.startswith('/')) :
  outputDir = '/mnt/local_homes/ahaas/{directory}'.format(directory = directory)

if not os.path.exists(outputDir):
  os.makedirs(outputDir)

queues = ah_config.allQueues
#queues = ['tsstutterlist' 
#             , 'tsstutterarray'
#             , 'tsatomiclist'  
#             , 'tsatomicarray' 
#             , 'tshwlist'      
#             , 'tshwarray']
works = [250, 2000]
maxThreads = ah_config.maxThreadsB7
threads = [1, 4, 8, 12, 16, 20, 24]

if application == "prodcon":
  threads = [1, 2, 4, 6, 8, 10, 12]

if application in ah_config.templates:
  benchmark.runBenchmark(
                     template = ah_config.templates[application],
                     filenameTemplate = ah_config.filenameTemplates[application],
                     queues = queues, 
                     works = works, 
                     threads = threads, 
                     maxThreads = maxThreads, 
                     directory = outputDir, 
                     prefill = 0, 
                     performance = True)
else:
  print "The benchmark {benchmark} does not exist".format(benchmark = sys.argv[1])

