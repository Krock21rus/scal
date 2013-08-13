import os;
import ah_config;

pParameter = ah_config.pParameter
executables = ah_config.executables 

def runBenchmark(
    template
    , filenameTemplate
    , queues
    , works
    , threads
    , maxThreads
    , prefill = 0
    , directory=''
    , performance = True):

  perfParam = '-log_operations -noprint_summary'
  if performance:
    perfParam = '-nolog_operations -print_summary'


  for queue in queues:
      
      for work in works:

          for thread in threads:

              exe = queue
              if queue in executables:
                exe = executables[queue]

              command = ""
              if queue in pParameter:
                filename = filenameTemplate.format(directory = directory
                    , queue = queue
                    , thread = thread
                    , partials_param = '-' + pParameter[queue]
                    , partials = maxThreads
                    , work = work)

                # Cut off everything before the @.
                filename = filename[filename.find('@') + 1:]
                command = template.format(queue=queue,
                                                 exe=exe,
                                                 thread=thread, 
                                                 work=work, 
                                                 partials_param='-' + pParameter[queue], 
                                                 partials=maxThreads,
                                                 directory=directory,
                                                 perfParam=perfParam,
                                                 prefill = str(prefill),
                                                 filename = filename)
              else:

                filename = filenameTemplate.format(directory = directory
                    , queue = queue
                    , thread = thread
                    , partials = ''
                    , partials_param = ''
                    , work = work)

                filename = filename[filename.find('@') + 1:]

                command = template.format(queue=queue,
                                            exe = exe,
                                            thread=thread, 
                                            work=work, 
                                            partials_param='', 
                                            partials='',
                                            directory=directory,
                                            perfParam = perfParam,
                                            prefill = str(prefill),
                                            filename = filename)

              if os.path.exists(filename):
                os.remove(filename)
              command = command[command.find('@') + 1:]
              print command
              os.system(command)
