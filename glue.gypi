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
  ]
}
