// Copyright (c) 2012, the Scal project authors.  Please see the AUTHORS file
// for details. All rights reserved. Use of this source code is governed by a
// BSD-style license that can be found in the LICENSE file.

#ifndef SCAL_BENCHMARK_COMMON_H_
#define SCAL_BENCHMARK_COMMON_H_

#include <inttypes.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

namespace scal {

class Benchmark {
 public:
  Benchmark(uint64_t num_threads,
            uint64_t thread_prealloc_size,
            uint64_t histogram_size,
            void *data);
  void run(void);

  inline uint64_t execution_time(void) {
    return global_end_time_ - global_start_time_;
  }

 protected:
  virtual ~Benchmark() {}

  void *data_;

  virtual void bench_func(void) = 0;
  uint64_t thread_id(void);

 private:
  static void *pthread_start_helper(void *thiz) {
    reinterpret_cast<Benchmark*>(thiz)->startup_thread();
    return NULL;
  }

  pthread_barrier_t start_barrier_;
  pthread_t *threads_;
  uint64_t num_threads_;
  uint64_t global_start_time_;
  uint64_t global_end_time_;
  uint64_t thread_prealloc_size_;

  void startup_thread(void);
};

}  // namespace scal

#endif  // SCAL_BENCHMARK_COMMON_H_
