{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'libscal',
      'type': 'static_library',
      'sources': [
        'src/util/atomic_value128.h',
        'src/util/atomic_value64_base.h',
        'src/util/atomic_value64_no_offset.h',
        'src/util/atomic_value64_offset.h',
        'src/util/atomic_value.h',
        'src/util/atomic_value_new.h',
        'src/util/allocation.h',
        'src/util/allocation.cc',
        'src/util/barrier.h',
        'src/util/bitmap.h',
        'src/util/malloc-compat.h',
        'src/util/operation_logger.h',
        'src/util/platform.h',
        'src/util/random.h',
        'src/util/random.cc',
        'src/util/threadlocals.h',
        'src/util/threadlocals.cc',
        'src/util/time.h',
        'src/util/workloads.h',
        'src/util/workloads.cc',
      ],
    },
    {
      'target_name': 'prodcon-base',
      'type': 'static_library',
      'sources': [
        'src/benchmark/common.cc',
        'src/benchmark/prodcon/prodcon.cc',
      ],
    },
    {
      'target_name': 'prodcon-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ms',
      ],
    },
    {
      'target_name': 'prodcon-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:treiber',
      ],
    },
    {
      'target_name': 'prodcon-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:kstack',
      ],
    },
    {
      'target_name': 'prodcon-ll-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-kstack',
      ],
    },
    {
      'target_name': 'prodcon-dq-1random-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:dq-1random-ms',
      ],
    },
    {
      'target_name': 'prodcon-dq-1random-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:dq-1random-treiber',
      ],
    },
    {
      'target_name': 'prodcon-fc',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:fc',
      ],
    },
    {
      'target_name': 'prodcon-rd',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:rd',
      ],
    },
    {
      'target_name': 'prodcon-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:us-kfifo',
      ],
    },
    {
      'target_name': 'prodcon-ll-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-us-kfifo',
      ],
    },
  ]
}
