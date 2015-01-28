{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'ms',
      'type': 'static_library',
      'sources': [
        'src/benchmark/std_glue/glue_ms_queue.cc'
      ],
    },
    {
      'target_name': 'treiber',
      'type': 'static_library',
      'sources': [
        'src/benchmark/std_glue/glue_treiber_stack.cc'
      ],
    },
    {
      'target_name': 'kstack',
      'type': 'static_library',
      'sources': [
        'src/benchmark/std_glue/glue_kstack.cc'
      ],
    },
    {
      'target_name': 'll-kstack',
      'type': 'static_library',
      'cflags': [ '-DLOCALLY_LINEARIZABLE' ],
      'sources': [
        'src/benchmark/std_glue/glue_ll_kstack.cc'
      ],
    },
    {
      'target_name': 'dq-1random-ms',
      'type': 'static_library',
      'sources': [
        'src/benchmark/std_glue/glue_dq_1random_ms.cc'
      ],
    },
    {
      'target_name': 'dq-1random-treiber',
      'type': 'static_library',
      'sources': [
        'src/benchmark/std_glue/glue_dq_1random_treiber.cc'
      ],
    },
    {
      'target_name': 'fc',
      'type': 'static_library',
      'sources': [
        'src/benchmark/std_glue/glue_fc_queue.cc'
      ],
    },
    {
      'target_name': 'rd',
      'type': 'static_library',
      'sources': [
        'src/benchmark/std_glue/glue_rd_queue.cc'
      ],
    },
    {
      'target_name': 'us-kfifo',
      'type': 'static_library',
      'sources': [
        'src/benchmark/std_glue/glue_uskfifo.cc'
      ],
    },
    {
      'target_name': 'll-us-kfifo',
      'type': 'static_library',
      'cflags': [ '-DLOCALLY_LINEARIZABLE' ],
      'sources': [
        'src/benchmark/std_glue/glue_uskfifo.cc'
      ],
    },
    {
      'target_name': 'll-dq-ms',
      'type': 'static_library',
      'cflags': [ ],
      'sources': [
        'src/benchmark/std_glue/glue_ll_dq_ms.cc'
      ],
    },
    {
      'target_name': 'll-dq-treiber',
      'type': 'static_library',
      'cflags': [ ],
      'sources': [
        'src/benchmark/std_glue/glue_ll_dq_treiber.cc'
      ],
    },
    {
      'target_name': 'lcrq',
      'type': 'static_library',
      'cflags': [ ],
      'sources': [
        'src/benchmark/std_glue/glue_lcrq.cc'
      ],
      'dependencies': [
        'upstream.gypi:lcrq-base',
      ],
    },
    {
      'target_name': 'hc-ts-cas-stack',
      'type': 'static_library',
      'cflags': [ ],
      'sources': [
        'src/benchmark/std_glue/glue_hardcoded_ts_cas_stack.cc'
      ],
    },
    {
      'target_name': 'hc-ts-stutter-stack',
      'type': 'static_library',
      'cflags': [ ],
      'sources': [
        'src/benchmark/std_glue/glue_hardcoded_ts_stutter_stack.cc'
      ],
    },
    {
      'target_name': 'hc-ts-interval-stack',
      'type': 'static_library',
      'cflags': [ ],
      'sources': [
        'src/benchmark/std_glue/glue_hardcoded_ts_interval_stack.cc'
      ],
    },
    {
      'target_name': 'hc-ts-atomic-stack',
      'type': 'static_library',
      'cflags': [ ],
      'sources': [
        'src/benchmark/std_glue/glue_hardcoded_ts_atomic_stack.cc'
      ],
    },
    {
      'target_name': 'hc-ts-hardware-stack',
      'type': 'static_library',
      'cflags': [ ],
      'sources': [
        'src/benchmark/std_glue/glue_hardcoded_ts_hardware_stack.cc'
      ],
    },
  ]
}
