#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>

#define __STDC_FORMAT_MACROS
#include <inttypes.h>

#include "operation.h"
#include "fifoExecuterLowerBound.h"
#include "fifoExecuterUpperBound.h"
#include "histogram.h"

void enable_frequency_scaling() {
  int result = system("for i in  /sys/devices/system/cpu/cpu? /sys/devices/system/cpu/cpu??; do sudo sh -c \"echo ondemand > $i/cpufreq/scaling_governor\"; done");
  if (result) {
    printf("frequency scaling error");
  }
}

void disable_frequency_scaling() {
  int result = system("for i in  /sys/devices/system/cpu/cpu? /sys/devices/system/cpu/cpu??; do sudo sh -c \"echo performance > $i/cpufreq/scaling_governor\"; done");
  if (result) {
    printf("frequency scaling error");
  }
}

int main(int argc, char** argv) {
  if (argc < 7) {
    fprintf(stderr, "usage: ./analyzer <logfilename> <fifo|lifo> <operations> <mode> <debug|sum|histogram|sumparam> <param>\n");
    return 1;
  }

  char* filename = argv[1];
  char* datastructure = argv[2];
  int operations = atoi(argv[3]);
  int bound = atoi(argv[4]); //0 lower bound, 1 upper bound
  char* mode = argv[5];
  int param = atoi(argv[6]);

  disable_frequency_scaling();

  FILE* input = fopen(filename, "r");
  Operations ops(input, operations);
  fclose(input);
  ops.CalculateOverlaps();

  FifoExecuter *executer;
  if (bound == 0) {
    executer = new FifoExecuterLowerBound(&ops);
  } else {
    executer = new FifoExecuterUpperBound(&ops);
  }
  Histogram histogram;
  executer->execute(&histogram);
  if (strcmp(datastructure, "fifo") == 0) {
    if (strcmp(mode, "histogram") == 0) {
      histogram.print();
    } else if (strcmp(mode, "sum") == 0) {
      printf("%" PRIu64 "\n", histogram.commulativeError());
    } else if (strcmp(mode, "sumparam") == 0) {
      printf("%d %" PRIu64 " %" PRIu64 " %f %f\n", param, histogram.commulativeError(), histogram.max(), histogram.mean(), histogram.stdv());
    } else {
      printf("wrong mode\n");
    }
  } else {
    printf("Fatal Error: datastructure not supported\n");
    enable_frequency_scaling();
    exit(2);
  }
  enable_frequency_scaling();
  return 0;
}
