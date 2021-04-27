cmake_minimum_required(VERSION 2.8.8 FATAL_ERROR)
cmake_policy(VERSION 2.8.8)
project(prodcon-bs-kfifo)
set(configuration "Release")
enable_language(ASM)
set(builddir "${CMAKE_CURRENT_BINARY_DIR}")
set(obj "${builddir}/obj")

set(CMAKE_C_OUTPUT_EXTENSION_REPLACE 1)
set(CMAKE_CXX_OUTPUT_EXTENSION_REPLACE 1)

set(CMAKE_NINJA_FORCE_RESPONSE_FILE 1)


#upstream.gyp:lcrq-base#target
set(TARGET "lcrq-base")
set(TOOLSET "target")
set(lcrq-base__c_srcs "../../src/datastructures/upstream/lcrq/lcrq.c")
add_library(lcrq-base STATIC ${lcrq-base__c_srcs})
set_target_properties(lcrq-base PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(lcrq-base PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(lcrq-base PROPERTIES PREFIX "lib")
set_target_properties(lcrq-base PROPERTIES ARCHIVE_OUTPUT_NAME "lcrq-base")
set_target_properties(lcrq-base PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/liblcrq-base.a PROPERTIES GENERATED "TRUE")
list(APPEND lcrq-base__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../../src/datastructures/upstream/sim-synch1.4"
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET lcrq-base APPEND PROPERTY INCLUDE_DIRECTORIES ${lcrq-base__include_dirs})
set_target_properties(lcrq-base PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(lcrq-base PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(lcrq-base PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(lcrq-base PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(lcrq-base PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(lcrq-base PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#glue.gyp:lcrq#target
set(TARGET "lcrq")
set(TOOLSET "target")
set(lcrq__cxx_srcs "../../src/benchmark/std_glue/glue_lcrq.cc")
add_library(lcrq STATIC ${lcrq__cxx_srcs})
set_target_properties(lcrq PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(lcrq PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(lcrq PROPERTIES PREFIX "lib")
set_target_properties(lcrq PROPERTIES ARCHIVE_OUTPUT_NAME "lcrq")
set_target_properties(lcrq PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/liblcrq.a PROPERTIES GENERATED "TRUE")
list(APPEND lcrq__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET lcrq APPEND PROPERTY INCLUDE_DIRECTORIES ${lcrq__include_dirs})
set_target_properties(lcrq PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(lcrq PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(lcrq PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(lcrq PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(lcrq PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(lcrq PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-base#target
set(TARGET "seqalt-base")
set(TOOLSET "target")
list(APPEND seqalt-base__cxx_srcs
  "../../src/benchmark/common.cc"
  "../../src/benchmark/seqalt/seqalt.cc")
add_library(seqalt-base STATIC ${seqalt-base__cxx_srcs})
set_target_properties(seqalt-base PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-base PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(seqalt-base PROPERTIES PREFIX "lib")
set_target_properties(seqalt-base PROPERTIES ARCHIVE_OUTPUT_NAME "seqalt-base")
set_target_properties(seqalt-base PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libseqalt-base.a PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-base__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-base APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-base__include_dirs})
set_target_properties(seqalt-base PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-base PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(seqalt-base PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-base PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-base PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-base PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-base#target
set(TARGET "prodcon-base")
set(TOOLSET "target")
list(APPEND prodcon-base__cxx_srcs
  "../../src/benchmark/common.cc"
  "../../src/util/allocation.cc"
  "../../src/util/threadlocals.cc"
  "../../src/util/workloads.cc"
  "../../src/benchmark/prodcon/prodcon.cc")
list(APPEND prodcon-base__other_srcs
  "../../src/benchmark/common.h"
  "../../src/util/allocation.h"
  "../../src/util/threadlocals.h"
  "../../src/util/workloads.h")
add_library(prodcon-base STATIC ${prodcon-base__cxx_srcs} ${prodcon-base__other_srcs})
set_target_properties(prodcon-base PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_source_files_properties(${prodcon-base__other_srcs} PROPERTIES HEADER_FILE_ONLY "TRUE")
set_target_properties(prodcon-base PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(prodcon-base PROPERTIES PREFIX "lib")
set_target_properties(prodcon-base PROPERTIES ARCHIVE_OUTPUT_NAME "prodcon-base")
set_target_properties(prodcon-base PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libprodcon-base.a PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-base__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-base APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-base__include_dirs})
set_target_properties(prodcon-base PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-base PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(prodcon-base PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-base PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-base PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-base PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:mm-harness#target
set(TARGET "mm-harness")
set(TOOLSET "target")
list(APPEND mm-harness__cxx_srcs
  "../../src/benchmark/common.cc"
  "../../src/util/allocation.cc"
  "../../src/util/threadlocals.cc"
  "../../src/util/workloads.cc"
  "../../src/benchmark/mm/mm.cc")
list(APPEND mm-harness__other_srcs
  "../../src/benchmark/common.h"
  "../../src/util/allocation.h"
  "../../src/util/threadlocals.h"
  "../../src/util/workloads.h")
add_executable(mm-harness ${mm-harness__cxx_srcs} ${mm-harness__other_srcs})
set_target_properties(mm-harness PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_source_files_properties(${mm-harness__other_srcs} PROPERTIES HEADER_FILE_ONLY "TRUE")
set_target_properties(mm-harness PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(mm-harness PROPERTIES PREFIX "")
set_target_properties(mm-harness PROPERTIES RUNTIME_OUTPUT_NAME "mm-harness")
set_target_properties(mm-harness PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/mm-harness PROPERTIES GENERATED "TRUE")
list(APPEND mm-harness__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET mm-harness APPEND PROPERTY INCLUDE_DIRECTORIES ${mm-harness__include_dirs})
set_target_properties(mm-harness PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(mm-harness PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(mm-harness PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(mm-harness PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(mm-harness PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(mm-harness PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(mm-harness
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:libscal#target
set(TARGET "libscal")
set(TOOLSET "target")
list(APPEND libscal__cxx_srcs
  "../../src/util/allocation.cc"
  "../../src/util/random.cc"
  "../../src/util/threadlocals.cc"
  "../../src/util/workloads.cc")
list(APPEND libscal__other_srcs
  "../../src/util/atomic_value128.h"
  "../../src/util/atomic_value64_base.h"
  "../../src/util/atomic_value64_no_offset.h"
  "../../src/util/atomic_value64_offset.h"
  "../../src/util/atomic_value.h"
  "../../src/util/atomic_value_new.h"
  "../../src/util/allocation.h"
  "../../src/util/barrier.h"
  "../../src/util/bitmap.h"
  "../../src/util/malloc-compat.h"
  "../../src/util/operation_logger.h"
  "../../src/util/platform.h"
  "../../src/util/random.h"
  "../../src/util/threadlocals.h"
  "../../src/util/time.h"
  "../../src/util/workloads.h")
add_library(libscal STATIC ${libscal__cxx_srcs} ${libscal__other_srcs})
set_target_properties(libscal PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_source_files_properties(${libscal__other_srcs} PROPERTIES HEADER_FILE_ONLY "TRUE")
set_target_properties(libscal PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(libscal PROPERTIES PREFIX "lib")
set_target_properties(libscal PROPERTIES ARCHIVE_OUTPUT_NAME "scal")
set_target_properties(libscal PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libscal.a PROPERTIES GENERATED "TRUE")
list(APPEND libscal__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET libscal APPEND PROPERTY INCLUDE_DIRECTORIES ${libscal__include_dirs})
set_target_properties(libscal PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(libscal PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(libscal PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(libscal PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(libscal PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(libscal PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-lcrq#target
set(TARGET "seqalt-lcrq")
set(TOOLSET "target")
set(seqalt-lcrq__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-lcrq__dummy_srcs}")
  file(WRITE "${seqalt-lcrq__dummy_srcs}" "")
endif()
add_executable(seqalt-lcrq ${seqalt-lcrq__dummy_srcs})
set_target_properties(seqalt-lcrq PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-lcrq PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-lcrq PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-lcrq PROPERTIES PREFIX "")
set_target_properties(seqalt-lcrq PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-lcrq")
set_target_properties(seqalt-lcrq PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-lcrq PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-lcrq__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-lcrq APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-lcrq__include_dirs})
set_target_properties(seqalt-lcrq PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-lcrq PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-lcrq PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-lcrq PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-lcrq PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-lcrq PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-lcrq
-Wl,--start-group
  libscal
  seqalt-base
  lcrq
  lcrq-base
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-lcrq#target
set(TARGET "prodcon-lcrq")
set(TOOLSET "target")
set(prodcon-lcrq__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-lcrq__dummy_srcs}")
  file(WRITE "${prodcon-lcrq__dummy_srcs}" "")
endif()
add_executable(prodcon-lcrq ${prodcon-lcrq__dummy_srcs})
set_target_properties(prodcon-lcrq PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-lcrq PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-lcrq PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-lcrq PROPERTIES PREFIX "")
set_target_properties(prodcon-lcrq PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-lcrq")
set_target_properties(prodcon-lcrq PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-lcrq PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-lcrq__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-lcrq APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-lcrq__include_dirs})
set_target_properties(prodcon-lcrq PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-lcrq PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-lcrq PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-lcrq PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-lcrq PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-lcrq PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-lcrq
-Wl,--start-group
  libscal
  prodcon-base
  lcrq
  lcrq-base
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:computational-load#target
set(TARGET "computational-load")
set(TOOLSET "target")
list(APPEND computational-load__cxx_srcs
  "../../src/benchmark/common.cc"
  "../../src/util/allocation.cc"
  "../../src/util/threadlocals.cc"
  "../../src/util/workloads.cc"
  "../../src/benchmark/computational-load/computational-load.cc")
list(APPEND computational-load__other_srcs
  "../../src/benchmark/common.h"
  "../../src/util/allocation.h"
  "../../src/util/threadlocals.h"
  "../../src/util/workloads.h")
add_executable(computational-load ${computational-load__cxx_srcs} ${computational-load__other_srcs})
set_target_properties(computational-load PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_source_files_properties(${computational-load__other_srcs} PROPERTIES HEADER_FILE_ONLY "TRUE")
set_target_properties(computational-load PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(computational-load PROPERTIES PREFIX "")
set_target_properties(computational-load PROPERTIES RUNTIME_OUTPUT_NAME "computational-load")
set_target_properties(computational-load PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/computational-load PROPERTIES GENERATED "TRUE")
list(APPEND computational-load__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET computational-load APPEND PROPERTY INCLUDE_DIRECTORIES ${computational-load__include_dirs})
set_target_properties(computational-load PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(computational-load PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(computational-load PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(computational-load PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(computational-load PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(computational-load PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(computational-load
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:wf-queue#target
set(TARGET "wf-queue")
set(TOOLSET "target")
set(wf-queue__cxx_srcs "../../src/benchmark/std_glue/glue_wf_ppopp12.cc")
add_library(wf-queue STATIC ${wf-queue__cxx_srcs})
set_target_properties(wf-queue PROPERTIES EXCLUDE_FROM_ALL "TRUE")
set_target_properties(wf-queue PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(wf-queue PROPERTIES PREFIX "lib")
set_target_properties(wf-queue PROPERTIES ARCHIVE_OUTPUT_NAME "wf-queue")
set_target_properties(wf-queue PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libwf-queue.a PROPERTIES GENERATED "TRUE")
list(APPEND wf-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET wf-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${wf-queue__include_dirs})
set_target_properties(wf-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(wf-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(wf-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(wf-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(wf-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(wf-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#glue.gyp:us-kfifo#target
set(TARGET "us-kfifo")
set(TOOLSET "target")
set(us-kfifo__cxx_srcs "../../src/benchmark/std_glue/glue_uskfifo.cc")
add_library(us-kfifo STATIC ${us-kfifo__cxx_srcs})
set_target_properties(us-kfifo PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(us-kfifo PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(us-kfifo PROPERTIES PREFIX "lib")
set_target_properties(us-kfifo PROPERTIES ARCHIVE_OUTPUT_NAME "us-kfifo")
set_target_properties(us-kfifo PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libus-kfifo.a PROPERTIES GENERATED "TRUE")
list(APPEND us-kfifo__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET us-kfifo APPEND PROPERTY INCLUDE_DIRECTORIES ${us-kfifo__include_dirs})
set_target_properties(us-kfifo PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(us-kfifo PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(us-kfifo PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(us-kfifo PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-us-kfifo#target
set(TARGET "seqalt-us-kfifo")
set(TOOLSET "target")
set(seqalt-us-kfifo__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-us-kfifo__dummy_srcs}")
  file(WRITE "${seqalt-us-kfifo__dummy_srcs}" "")
endif()
add_executable(seqalt-us-kfifo ${seqalt-us-kfifo__dummy_srcs})
set_target_properties(seqalt-us-kfifo PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-us-kfifo PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-us-kfifo PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-us-kfifo PROPERTIES PREFIX "")
set_target_properties(seqalt-us-kfifo PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-us-kfifo")
set_target_properties(seqalt-us-kfifo PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-us-kfifo PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-us-kfifo__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-us-kfifo APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-us-kfifo__include_dirs})
set_target_properties(seqalt-us-kfifo PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-us-kfifo PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-us-kfifo PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-us-kfifo PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-us-kfifo
-Wl,--start-group
  libscal
  seqalt-base
  us-kfifo
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-us-kfifo#target
set(TARGET "prodcon-us-kfifo")
set(TOOLSET "target")
set(prodcon-us-kfifo__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-us-kfifo__dummy_srcs}")
  file(WRITE "${prodcon-us-kfifo__dummy_srcs}" "")
endif()
add_executable(prodcon-us-kfifo ${prodcon-us-kfifo__dummy_srcs})
set_target_properties(prodcon-us-kfifo PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-us-kfifo PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-us-kfifo PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-us-kfifo PROPERTIES PREFIX "")
set_target_properties(prodcon-us-kfifo PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-us-kfifo")
set_target_properties(prodcon-us-kfifo PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-us-kfifo PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-us-kfifo__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-us-kfifo APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-us-kfifo__include_dirs})
set_target_properties(prodcon-us-kfifo PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-us-kfifo PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-us-kfifo PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-us-kfifo PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-us-kfifo
-Wl,--start-group
  libscal
  prodcon-base
  us-kfifo
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ts-stutter-deque#target
set(TARGET "ts-stutter-deque")
set(TOOLSET "target")
set(ts-stutter-deque__cxx_srcs "../../src/benchmark/std_glue/glue_ts_stutter_deque.cc")
add_library(ts-stutter-deque STATIC ${ts-stutter-deque__cxx_srcs})
set_target_properties(ts-stutter-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ts-stutter-deque PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ts-stutter-deque PROPERTIES PREFIX "lib")
set_target_properties(ts-stutter-deque PROPERTIES ARCHIVE_OUTPUT_NAME "ts-stutter-deque")
set_target_properties(ts-stutter-deque PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libts-stutter-deque.a PROPERTIES GENERATED "TRUE")
list(APPEND ts-stutter-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ts-stutter-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${ts-stutter-deque__include_dirs})
set_target_properties(ts-stutter-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(ts-stutter-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ts-stutter-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ts-stutter-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ts-stutter-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ts-stutter-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ts-stutter-deque#target
set(TARGET "seqalt-ts-stutter-deque")
set(TOOLSET "target")
set(seqalt-ts-stutter-deque__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ts-stutter-deque__dummy_srcs}")
  file(WRITE "${seqalt-ts-stutter-deque__dummy_srcs}" "")
endif()
add_executable(seqalt-ts-stutter-deque ${seqalt-ts-stutter-deque__dummy_srcs})
set_target_properties(seqalt-ts-stutter-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ts-stutter-deque PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ts-stutter-deque PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ts-stutter-deque PROPERTIES PREFIX "")
set_target_properties(seqalt-ts-stutter-deque PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ts-stutter-deque")
set_target_properties(seqalt-ts-stutter-deque PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ts-stutter-deque PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ts-stutter-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ts-stutter-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ts-stutter-deque__include_dirs})
set_target_properties(seqalt-ts-stutter-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ts-stutter-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ts-stutter-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ts-stutter-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ts-stutter-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ts-stutter-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ts-stutter-deque
-Wl,--start-group
  libscal
  seqalt-base
  ts-stutter-deque
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ts-stutter-deque#target
set(TARGET "prodcon-ts-stutter-deque")
set(TOOLSET "target")
set(prodcon-ts-stutter-deque__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ts-stutter-deque__dummy_srcs}")
  file(WRITE "${prodcon-ts-stutter-deque__dummy_srcs}" "")
endif()
add_executable(prodcon-ts-stutter-deque ${prodcon-ts-stutter-deque__dummy_srcs})
set_target_properties(prodcon-ts-stutter-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ts-stutter-deque PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ts-stutter-deque PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ts-stutter-deque PROPERTIES PREFIX "")
set_target_properties(prodcon-ts-stutter-deque PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ts-stutter-deque")
set_target_properties(prodcon-ts-stutter-deque PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ts-stutter-deque PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ts-stutter-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ts-stutter-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ts-stutter-deque__include_dirs})
set_target_properties(prodcon-ts-stutter-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ts-stutter-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ts-stutter-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ts-stutter-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ts-stutter-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ts-stutter-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ts-stutter-deque
-Wl,--start-group
  libscal
  prodcon-base
  ts-stutter-deque
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ts-interval-deque#target
set(TARGET "ts-interval-deque")
set(TOOLSET "target")
set(ts-interval-deque__cxx_srcs "../../src/benchmark/std_glue/glue_ts_interval_deque.cc")
add_library(ts-interval-deque STATIC ${ts-interval-deque__cxx_srcs})
set_target_properties(ts-interval-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ts-interval-deque PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ts-interval-deque PROPERTIES PREFIX "lib")
set_target_properties(ts-interval-deque PROPERTIES ARCHIVE_OUTPUT_NAME "ts-interval-deque")
set_target_properties(ts-interval-deque PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libts-interval-deque.a PROPERTIES GENERATED "TRUE")
list(APPEND ts-interval-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ts-interval-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${ts-interval-deque__include_dirs})
set_target_properties(ts-interval-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(ts-interval-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ts-interval-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ts-interval-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ts-interval-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ts-interval-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ts-interval-deque#target
set(TARGET "seqalt-ts-interval-deque")
set(TOOLSET "target")
set(seqalt-ts-interval-deque__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ts-interval-deque__dummy_srcs}")
  file(WRITE "${seqalt-ts-interval-deque__dummy_srcs}" "")
endif()
add_executable(seqalt-ts-interval-deque ${seqalt-ts-interval-deque__dummy_srcs})
set_target_properties(seqalt-ts-interval-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ts-interval-deque PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ts-interval-deque PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ts-interval-deque PROPERTIES PREFIX "")
set_target_properties(seqalt-ts-interval-deque PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ts-interval-deque")
set_target_properties(seqalt-ts-interval-deque PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ts-interval-deque PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ts-interval-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ts-interval-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ts-interval-deque__include_dirs})
set_target_properties(seqalt-ts-interval-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ts-interval-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ts-interval-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ts-interval-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ts-interval-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ts-interval-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ts-interval-deque
-Wl,--start-group
  libscal
  seqalt-base
  ts-interval-deque
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ts-interval-deque#target
set(TARGET "prodcon-ts-interval-deque")
set(TOOLSET "target")
set(prodcon-ts-interval-deque__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ts-interval-deque__dummy_srcs}")
  file(WRITE "${prodcon-ts-interval-deque__dummy_srcs}" "")
endif()
add_executable(prodcon-ts-interval-deque ${prodcon-ts-interval-deque__dummy_srcs})
set_target_properties(prodcon-ts-interval-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ts-interval-deque PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ts-interval-deque PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ts-interval-deque PROPERTIES PREFIX "")
set_target_properties(prodcon-ts-interval-deque PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ts-interval-deque")
set_target_properties(prodcon-ts-interval-deque PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ts-interval-deque PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ts-interval-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ts-interval-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ts-interval-deque__include_dirs})
set_target_properties(prodcon-ts-interval-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ts-interval-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ts-interval-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ts-interval-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ts-interval-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ts-interval-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ts-interval-deque
-Wl,--start-group
  libscal
  prodcon-base
  ts-interval-deque
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ts-hardware-deque#target
set(TARGET "ts-hardware-deque")
set(TOOLSET "target")
set(ts-hardware-deque__cxx_srcs "../../src/benchmark/std_glue/glue_ts_hardware_deque.cc")
add_library(ts-hardware-deque STATIC ${ts-hardware-deque__cxx_srcs})
set_target_properties(ts-hardware-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ts-hardware-deque PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ts-hardware-deque PROPERTIES PREFIX "lib")
set_target_properties(ts-hardware-deque PROPERTIES ARCHIVE_OUTPUT_NAME "ts-hardware-deque")
set_target_properties(ts-hardware-deque PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libts-hardware-deque.a PROPERTIES GENERATED "TRUE")
list(APPEND ts-hardware-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ts-hardware-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${ts-hardware-deque__include_dirs})
set_target_properties(ts-hardware-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(ts-hardware-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ts-hardware-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ts-hardware-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ts-hardware-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ts-hardware-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ts-hardware-deque#target
set(TARGET "seqalt-ts-hardware-deque")
set(TOOLSET "target")
set(seqalt-ts-hardware-deque__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ts-hardware-deque__dummy_srcs}")
  file(WRITE "${seqalt-ts-hardware-deque__dummy_srcs}" "")
endif()
add_executable(seqalt-ts-hardware-deque ${seqalt-ts-hardware-deque__dummy_srcs})
set_target_properties(seqalt-ts-hardware-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ts-hardware-deque PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ts-hardware-deque PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ts-hardware-deque PROPERTIES PREFIX "")
set_target_properties(seqalt-ts-hardware-deque PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ts-hardware-deque")
set_target_properties(seqalt-ts-hardware-deque PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ts-hardware-deque PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ts-hardware-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ts-hardware-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ts-hardware-deque__include_dirs})
set_target_properties(seqalt-ts-hardware-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ts-hardware-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ts-hardware-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ts-hardware-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ts-hardware-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ts-hardware-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ts-hardware-deque
-Wl,--start-group
  libscal
  seqalt-base
  ts-hardware-deque
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ts-hardware-deque#target
set(TARGET "prodcon-ts-hardware-deque")
set(TOOLSET "target")
set(prodcon-ts-hardware-deque__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ts-hardware-deque__dummy_srcs}")
  file(WRITE "${prodcon-ts-hardware-deque__dummy_srcs}" "")
endif()
add_executable(prodcon-ts-hardware-deque ${prodcon-ts-hardware-deque__dummy_srcs})
set_target_properties(prodcon-ts-hardware-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ts-hardware-deque PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ts-hardware-deque PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ts-hardware-deque PROPERTIES PREFIX "")
set_target_properties(prodcon-ts-hardware-deque PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ts-hardware-deque")
set_target_properties(prodcon-ts-hardware-deque PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ts-hardware-deque PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ts-hardware-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ts-hardware-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ts-hardware-deque__include_dirs})
set_target_properties(prodcon-ts-hardware-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ts-hardware-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ts-hardware-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ts-hardware-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ts-hardware-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ts-hardware-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ts-hardware-deque
-Wl,--start-group
  libscal
  prodcon-base
  ts-hardware-deque
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ts-cas-deque#target
set(TARGET "ts-cas-deque")
set(TOOLSET "target")
set(ts-cas-deque__cxx_srcs "../../src/benchmark/std_glue/glue_ts_cas_deque.cc")
add_library(ts-cas-deque STATIC ${ts-cas-deque__cxx_srcs})
set_target_properties(ts-cas-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ts-cas-deque PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ts-cas-deque PROPERTIES PREFIX "lib")
set_target_properties(ts-cas-deque PROPERTIES ARCHIVE_OUTPUT_NAME "ts-cas-deque")
set_target_properties(ts-cas-deque PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libts-cas-deque.a PROPERTIES GENERATED "TRUE")
list(APPEND ts-cas-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ts-cas-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${ts-cas-deque__include_dirs})
set_target_properties(ts-cas-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(ts-cas-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ts-cas-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ts-cas-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ts-cas-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ts-cas-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ts-cas-deque#target
set(TARGET "seqalt-ts-cas-deque")
set(TOOLSET "target")
set(seqalt-ts-cas-deque__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ts-cas-deque__dummy_srcs}")
  file(WRITE "${seqalt-ts-cas-deque__dummy_srcs}" "")
endif()
add_executable(seqalt-ts-cas-deque ${seqalt-ts-cas-deque__dummy_srcs})
set_target_properties(seqalt-ts-cas-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ts-cas-deque PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ts-cas-deque PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ts-cas-deque PROPERTIES PREFIX "")
set_target_properties(seqalt-ts-cas-deque PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ts-cas-deque")
set_target_properties(seqalt-ts-cas-deque PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ts-cas-deque PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ts-cas-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ts-cas-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ts-cas-deque__include_dirs})
set_target_properties(seqalt-ts-cas-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ts-cas-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ts-cas-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ts-cas-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ts-cas-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ts-cas-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ts-cas-deque
-Wl,--start-group
  libscal
  seqalt-base
  ts-cas-deque
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ts-cas-deque#target
set(TARGET "prodcon-ts-cas-deque")
set(TOOLSET "target")
set(prodcon-ts-cas-deque__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ts-cas-deque__dummy_srcs}")
  file(WRITE "${prodcon-ts-cas-deque__dummy_srcs}" "")
endif()
add_executable(prodcon-ts-cas-deque ${prodcon-ts-cas-deque__dummy_srcs})
set_target_properties(prodcon-ts-cas-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ts-cas-deque PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ts-cas-deque PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ts-cas-deque PROPERTIES PREFIX "")
set_target_properties(prodcon-ts-cas-deque PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ts-cas-deque")
set_target_properties(prodcon-ts-cas-deque PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ts-cas-deque PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ts-cas-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ts-cas-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ts-cas-deque__include_dirs})
set_target_properties(prodcon-ts-cas-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ts-cas-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ts-cas-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ts-cas-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ts-cas-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ts-cas-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ts-cas-deque
-Wl,--start-group
  libscal
  prodcon-base
  ts-cas-deque
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ts-atomic-deque#target
set(TARGET "ts-atomic-deque")
set(TOOLSET "target")
set(ts-atomic-deque__cxx_srcs "../../src/benchmark/std_glue/glue_ts_atomic_deque.cc")
add_library(ts-atomic-deque STATIC ${ts-atomic-deque__cxx_srcs})
set_target_properties(ts-atomic-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ts-atomic-deque PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ts-atomic-deque PROPERTIES PREFIX "lib")
set_target_properties(ts-atomic-deque PROPERTIES ARCHIVE_OUTPUT_NAME "ts-atomic-deque")
set_target_properties(ts-atomic-deque PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libts-atomic-deque.a PROPERTIES GENERATED "TRUE")
list(APPEND ts-atomic-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ts-atomic-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${ts-atomic-deque__include_dirs})
set_target_properties(ts-atomic-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(ts-atomic-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ts-atomic-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ts-atomic-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ts-atomic-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ts-atomic-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ts-atomic-deque#target
set(TARGET "seqalt-ts-atomic-deque")
set(TOOLSET "target")
set(seqalt-ts-atomic-deque__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ts-atomic-deque__dummy_srcs}")
  file(WRITE "${seqalt-ts-atomic-deque__dummy_srcs}" "")
endif()
add_executable(seqalt-ts-atomic-deque ${seqalt-ts-atomic-deque__dummy_srcs})
set_target_properties(seqalt-ts-atomic-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ts-atomic-deque PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ts-atomic-deque PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ts-atomic-deque PROPERTIES PREFIX "")
set_target_properties(seqalt-ts-atomic-deque PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ts-atomic-deque")
set_target_properties(seqalt-ts-atomic-deque PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ts-atomic-deque PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ts-atomic-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ts-atomic-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ts-atomic-deque__include_dirs})
set_target_properties(seqalt-ts-atomic-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ts-atomic-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ts-atomic-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ts-atomic-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ts-atomic-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ts-atomic-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ts-atomic-deque
-Wl,--start-group
  libscal
  seqalt-base
  ts-atomic-deque
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ts-atomic-deque#target
set(TARGET "prodcon-ts-atomic-deque")
set(TOOLSET "target")
set(prodcon-ts-atomic-deque__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ts-atomic-deque__dummy_srcs}")
  file(WRITE "${prodcon-ts-atomic-deque__dummy_srcs}" "")
endif()
add_executable(prodcon-ts-atomic-deque ${prodcon-ts-atomic-deque__dummy_srcs})
set_target_properties(prodcon-ts-atomic-deque PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ts-atomic-deque PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ts-atomic-deque PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ts-atomic-deque PROPERTIES PREFIX "")
set_target_properties(prodcon-ts-atomic-deque PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ts-atomic-deque")
set_target_properties(prodcon-ts-atomic-deque PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ts-atomic-deque PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ts-atomic-deque__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ts-atomic-deque APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ts-atomic-deque__include_dirs})
set_target_properties(prodcon-ts-atomic-deque PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ts-atomic-deque PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ts-atomic-deque PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ts-atomic-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ts-atomic-deque PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ts-atomic-deque PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ts-atomic-deque
-Wl,--start-group
  libscal
  prodcon-base
  ts-atomic-deque
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:treiber#target
set(TARGET "treiber")
set(TOOLSET "target")
set(treiber__cxx_srcs "../../src/benchmark/std_glue/glue_treiber_stack.cc")
add_library(treiber STATIC ${treiber__cxx_srcs})
set_target_properties(treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(treiber PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(treiber PROPERTIES PREFIX "lib")
set_target_properties(treiber PROPERTIES ARCHIVE_OUTPUT_NAME "treiber")
set_target_properties(treiber PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libtreiber.a PROPERTIES GENERATED "TRUE")
list(APPEND treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${treiber__include_dirs})
set_target_properties(treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-treiber#target
set(TARGET "seqalt-treiber")
set(TOOLSET "target")
set(seqalt-treiber__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-treiber__dummy_srcs}")
  file(WRITE "${seqalt-treiber__dummy_srcs}" "")
endif()
add_executable(seqalt-treiber ${seqalt-treiber__dummy_srcs})
set_target_properties(seqalt-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-treiber PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-treiber PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-treiber PROPERTIES PREFIX "")
set_target_properties(seqalt-treiber PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-treiber")
set_target_properties(seqalt-treiber PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-treiber PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-treiber__include_dirs})
set_target_properties(seqalt-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-treiber
-Wl,--start-group
  libscal
  seqalt-base
  treiber
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-treiber#target
set(TARGET "prodcon-treiber")
set(TOOLSET "target")
set(prodcon-treiber__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-treiber__dummy_srcs}")
  file(WRITE "${prodcon-treiber__dummy_srcs}" "")
endif()
add_executable(prodcon-treiber ${prodcon-treiber__dummy_srcs})
set_target_properties(prodcon-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-treiber PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-treiber PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-treiber PROPERTIES PREFIX "")
set_target_properties(prodcon-treiber PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-treiber")
set_target_properties(prodcon-treiber PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-treiber PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-treiber__include_dirs})
set_target_properties(prodcon-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-treiber
-Wl,--start-group
  libscal
  prodcon-base
  treiber
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:sq#target
set(TARGET "sq")
set(TOOLSET "target")
set(sq__cxx_srcs "../../src/benchmark/std_glue/glue_sq_queue.cc")
add_library(sq STATIC ${sq__cxx_srcs})
set_target_properties(sq PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(sq PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(sq PROPERTIES PREFIX "lib")
set_target_properties(sq PROPERTIES ARCHIVE_OUTPUT_NAME "sq")
set_target_properties(sq PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libsq.a PROPERTIES GENERATED "TRUE")
list(APPEND sq__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET sq APPEND PROPERTY INCLUDE_DIRECTORIES ${sq__include_dirs})
set_target_properties(sq PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(sq PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(sq PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(sq PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(sq PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(sq PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-sq#target
set(TARGET "seqalt-sq")
set(TOOLSET "target")
set(seqalt-sq__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-sq__dummy_srcs}")
  file(WRITE "${seqalt-sq__dummy_srcs}" "")
endif()
add_executable(seqalt-sq ${seqalt-sq__dummy_srcs})
set_target_properties(seqalt-sq PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-sq PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-sq PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-sq PROPERTIES PREFIX "")
set_target_properties(seqalt-sq PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-sq")
set_target_properties(seqalt-sq PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-sq PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-sq__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-sq APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-sq__include_dirs})
set_target_properties(seqalt-sq PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-sq PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-sq PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-sq PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-sq PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-sq PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-sq
-Wl,--start-group
  libscal
  seqalt-base
  sq
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-sq#target
set(TARGET "prodcon-sq")
set(TOOLSET "target")
set(prodcon-sq__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-sq__dummy_srcs}")
  file(WRITE "${prodcon-sq__dummy_srcs}" "")
endif()
add_executable(prodcon-sq ${prodcon-sq__dummy_srcs})
set_target_properties(prodcon-sq PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-sq PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-sq PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-sq PROPERTIES PREFIX "")
set_target_properties(prodcon-sq PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-sq")
set_target_properties(prodcon-sq PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-sq PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-sq__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-sq APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-sq__include_dirs})
set_target_properties(prodcon-sq PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-sq PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-sq PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-sq PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-sq PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-sq PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-sq
-Wl,--start-group
  libscal
  prodcon-base
  sq
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:rts-queue#target
set(TARGET "rts-queue")
set(TOOLSET "target")
set(rts-queue__cxx_srcs "../../src/benchmark/std_glue/glue_rts_queue.cc")
add_library(rts-queue STATIC ${rts-queue__cxx_srcs})
set_target_properties(rts-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(rts-queue PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(rts-queue PROPERTIES PREFIX "lib")
set_target_properties(rts-queue PROPERTIES ARCHIVE_OUTPUT_NAME "rts-queue")
set_target_properties(rts-queue PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/librts-queue.a PROPERTIES GENERATED "TRUE")
list(APPEND rts-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET rts-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${rts-queue__include_dirs})
set_target_properties(rts-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(rts-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(rts-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(rts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(rts-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(rts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-rts-queue#target
set(TARGET "seqalt-rts-queue")
set(TOOLSET "target")
set(seqalt-rts-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-rts-queue__dummy_srcs}")
  file(WRITE "${seqalt-rts-queue__dummy_srcs}" "")
endif()
add_executable(seqalt-rts-queue ${seqalt-rts-queue__dummy_srcs})
set_target_properties(seqalt-rts-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-rts-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-rts-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-rts-queue PROPERTIES PREFIX "")
set_target_properties(seqalt-rts-queue PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-rts-queue")
set_target_properties(seqalt-rts-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-rts-queue PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-rts-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-rts-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-rts-queue__include_dirs})
set_target_properties(seqalt-rts-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-rts-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-rts-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-rts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-rts-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-rts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-rts-queue
-Wl,--start-group
  libscal
  seqalt-base
  rts-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-rts-queue#target
set(TARGET "prodcon-rts-queue")
set(TOOLSET "target")
set(prodcon-rts-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-rts-queue__dummy_srcs}")
  file(WRITE "${prodcon-rts-queue__dummy_srcs}" "")
endif()
add_executable(prodcon-rts-queue ${prodcon-rts-queue__dummy_srcs})
set_target_properties(prodcon-rts-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-rts-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-rts-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-rts-queue PROPERTIES PREFIX "")
set_target_properties(prodcon-rts-queue PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-rts-queue")
set_target_properties(prodcon-rts-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-rts-queue PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-rts-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-rts-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-rts-queue__include_dirs})
set_target_properties(prodcon-rts-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-rts-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-rts-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-rts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-rts-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-rts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-rts-queue
-Wl,--start-group
  libscal
  prodcon-base
  rts-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:rd#target
set(TARGET "rd")
set(TOOLSET "target")
set(rd__cxx_srcs "../../src/benchmark/std_glue/glue_rd_queue.cc")
add_library(rd STATIC ${rd__cxx_srcs})
set_target_properties(rd PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(rd PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(rd PROPERTIES PREFIX "lib")
set_target_properties(rd PROPERTIES ARCHIVE_OUTPUT_NAME "rd")
set_target_properties(rd PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/librd.a PROPERTIES GENERATED "TRUE")
list(APPEND rd__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET rd APPEND PROPERTY INCLUDE_DIRECTORIES ${rd__include_dirs})
set_target_properties(rd PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(rd PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(rd PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(rd PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(rd PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(rd PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-rd#target
set(TARGET "seqalt-rd")
set(TOOLSET "target")
set(seqalt-rd__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-rd__dummy_srcs}")
  file(WRITE "${seqalt-rd__dummy_srcs}" "")
endif()
add_executable(seqalt-rd ${seqalt-rd__dummy_srcs})
set_target_properties(seqalt-rd PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-rd PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-rd PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-rd PROPERTIES PREFIX "")
set_target_properties(seqalt-rd PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-rd")
set_target_properties(seqalt-rd PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-rd PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-rd__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-rd APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-rd__include_dirs})
set_target_properties(seqalt-rd PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-rd PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-rd PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-rd PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-rd PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-rd PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-rd
-Wl,--start-group
  libscal
  seqalt-base
  rd
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-rd#target
set(TARGET "prodcon-rd")
set(TOOLSET "target")
set(prodcon-rd__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-rd__dummy_srcs}")
  file(WRITE "${prodcon-rd__dummy_srcs}" "")
endif()
add_executable(prodcon-rd ${prodcon-rd__dummy_srcs})
set_target_properties(prodcon-rd PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-rd PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-rd PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-rd PROPERTIES PREFIX "")
set_target_properties(prodcon-rd PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-rd")
set_target_properties(prodcon-rd PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-rd PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-rd__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-rd APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-rd__include_dirs})
set_target_properties(prodcon-rd PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-rd PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-rd PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-rd PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-rd PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-rd PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-rd
-Wl,--start-group
  libscal
  prodcon-base
  rd
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ms#target
set(TARGET "ms")
set(TOOLSET "target")
set(ms__cxx_srcs "../../src/benchmark/std_glue/glue_ms_queue.cc")
add_library(ms STATIC ${ms__cxx_srcs})
set_target_properties(ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ms PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ms PROPERTIES PREFIX "lib")
set_target_properties(ms PROPERTIES ARCHIVE_OUTPUT_NAME "ms")
set_target_properties(ms PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libms.a PROPERTIES GENERATED "TRUE")
list(APPEND ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ms APPEND PROPERTY INCLUDE_DIRECTORIES ${ms__include_dirs})
set_target_properties(ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ms#target
set(TARGET "seqalt-ms")
set(TOOLSET "target")
set(seqalt-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ms__dummy_srcs}")
  file(WRITE "${seqalt-ms__dummy_srcs}" "")
endif()
add_executable(seqalt-ms ${seqalt-ms__dummy_srcs})
set_target_properties(seqalt-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ms PROPERTIES PREFIX "")
set_target_properties(seqalt-ms PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ms")
set_target_properties(seqalt-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ms PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ms__include_dirs})
set_target_properties(seqalt-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ms
-Wl,--start-group
  libscal
  seqalt-base
  ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ms#target
set(TARGET "prodcon-ms")
set(TOOLSET "target")
set(prodcon-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ms__dummy_srcs}")
  file(WRITE "${prodcon-ms__dummy_srcs}" "")
endif()
add_executable(prodcon-ms ${prodcon-ms__dummy_srcs})
set_target_properties(prodcon-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ms PROPERTIES PREFIX "")
set_target_properties(prodcon-ms PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ms")
set_target_properties(prodcon-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ms PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ms__include_dirs})
set_target_properties(prodcon-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ms
-Wl,--start-group
  libscal
  prodcon-base
  ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:lru-dds-treiber-stack#target
set(TARGET "lru-dds-treiber-stack")
set(TOOLSET "target")
set(lru-dds-treiber-stack__cxx_srcs "../../src/benchmark/std_glue/glue_lru_dds_treiber_stack.cc")
add_library(lru-dds-treiber-stack STATIC ${lru-dds-treiber-stack__cxx_srcs})
set_target_properties(lru-dds-treiber-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(lru-dds-treiber-stack PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(lru-dds-treiber-stack PROPERTIES PREFIX "lib")
set_target_properties(lru-dds-treiber-stack PROPERTIES ARCHIVE_OUTPUT_NAME "lru-dds-treiber-stack")
set_target_properties(lru-dds-treiber-stack PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/liblru-dds-treiber-stack.a PROPERTIES GENERATED "TRUE")
list(APPEND lru-dds-treiber-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET lru-dds-treiber-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${lru-dds-treiber-stack__include_dirs})
set_target_properties(lru-dds-treiber-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(lru-dds-treiber-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(lru-dds-treiber-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(lru-dds-treiber-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(lru-dds-treiber-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(lru-dds-treiber-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-lru-dds-treiber-stack#target
set(TARGET "seqalt-lru-dds-treiber-stack")
set(TOOLSET "target")
set(seqalt-lru-dds-treiber-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-lru-dds-treiber-stack__dummy_srcs}")
  file(WRITE "${seqalt-lru-dds-treiber-stack__dummy_srcs}" "")
endif()
add_executable(seqalt-lru-dds-treiber-stack ${seqalt-lru-dds-treiber-stack__dummy_srcs})
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES PREFIX "")
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-lru-dds-treiber-stack")
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-lru-dds-treiber-stack PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-lru-dds-treiber-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-lru-dds-treiber-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-lru-dds-treiber-stack__include_dirs})
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-lru-dds-treiber-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-lru-dds-treiber-stack
-Wl,--start-group
  libscal
  seqalt-base
  lru-dds-treiber-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-lru-dds-treiber-stack#target
set(TARGET "prodcon-lru-dds-treiber-stack")
set(TOOLSET "target")
set(prodcon-lru-dds-treiber-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-lru-dds-treiber-stack__dummy_srcs}")
  file(WRITE "${prodcon-lru-dds-treiber-stack__dummy_srcs}" "")
endif()
add_executable(prodcon-lru-dds-treiber-stack ${prodcon-lru-dds-treiber-stack__dummy_srcs})
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES PREFIX "")
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-lru-dds-treiber-stack")
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-lru-dds-treiber-stack PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-lru-dds-treiber-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-lru-dds-treiber-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-lru-dds-treiber-stack__include_dirs})
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-lru-dds-treiber-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-lru-dds-treiber-stack
-Wl,--start-group
  libscal
  prodcon-base
  lru-dds-treiber-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:lru-dds-ms#target
set(TARGET "lru-dds-ms")
set(TOOLSET "target")
set(lru-dds-ms__cxx_srcs "../../src/benchmark/std_glue/glue_lru_dds_ms.cc")
add_library(lru-dds-ms STATIC ${lru-dds-ms__cxx_srcs})
set_target_properties(lru-dds-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(lru-dds-ms PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(lru-dds-ms PROPERTIES PREFIX "lib")
set_target_properties(lru-dds-ms PROPERTIES ARCHIVE_OUTPUT_NAME "lru-dds-ms")
set_target_properties(lru-dds-ms PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/liblru-dds-ms.a PROPERTIES GENERATED "TRUE")
list(APPEND lru-dds-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET lru-dds-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${lru-dds-ms__include_dirs})
set_target_properties(lru-dds-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(lru-dds-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(lru-dds-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(lru-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(lru-dds-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(lru-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-lru-dds-ms#target
set(TARGET "seqalt-lru-dds-ms")
set(TOOLSET "target")
set(seqalt-lru-dds-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-lru-dds-ms__dummy_srcs}")
  file(WRITE "${seqalt-lru-dds-ms__dummy_srcs}" "")
endif()
add_executable(seqalt-lru-dds-ms ${seqalt-lru-dds-ms__dummy_srcs})
set_target_properties(seqalt-lru-dds-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-lru-dds-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-lru-dds-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-lru-dds-ms PROPERTIES PREFIX "")
set_target_properties(seqalt-lru-dds-ms PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-lru-dds-ms")
set_target_properties(seqalt-lru-dds-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-lru-dds-ms PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-lru-dds-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-lru-dds-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-lru-dds-ms__include_dirs})
set_target_properties(seqalt-lru-dds-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-lru-dds-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-lru-dds-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-lru-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-lru-dds-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-lru-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-lru-dds-ms
-Wl,--start-group
  libscal
  seqalt-base
  lru-dds-ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-lru-dds-ms#target
set(TARGET "prodcon-lru-dds-ms")
set(TOOLSET "target")
set(prodcon-lru-dds-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-lru-dds-ms__dummy_srcs}")
  file(WRITE "${prodcon-lru-dds-ms__dummy_srcs}" "")
endif()
add_executable(prodcon-lru-dds-ms ${prodcon-lru-dds-ms__dummy_srcs})
set_target_properties(prodcon-lru-dds-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-lru-dds-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-lru-dds-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-lru-dds-ms PROPERTIES PREFIX "")
set_target_properties(prodcon-lru-dds-ms PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-lru-dds-ms")
set_target_properties(prodcon-lru-dds-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-lru-dds-ms PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-lru-dds-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-lru-dds-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-lru-dds-ms__include_dirs})
set_target_properties(prodcon-lru-dds-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-lru-dds-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-lru-dds-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-lru-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-lru-dds-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-lru-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-lru-dds-ms
-Wl,--start-group
  libscal
  prodcon-base
  lru-dds-ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ll-us-kfifo#target
set(TARGET "ll-us-kfifo")
set(TOOLSET "target")
set(ll-us-kfifo__cxx_srcs "../../src/benchmark/std_glue/glue_uskfifo.cc")
add_library(ll-us-kfifo STATIC ${ll-us-kfifo__cxx_srcs})
set_target_properties(ll-us-kfifo PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ll-us-kfifo PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ll-us-kfifo PROPERTIES PREFIX "lib")
set_target_properties(ll-us-kfifo PROPERTIES ARCHIVE_OUTPUT_NAME "ll-us-kfifo")
set_target_properties(ll-us-kfifo PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libll-us-kfifo.a PROPERTIES GENERATED "TRUE")
list(APPEND ll-us-kfifo__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ll-us-kfifo APPEND PROPERTY INCLUDE_DIRECTORIES ${ll-us-kfifo__include_dirs})
set_target_properties(ll-us-kfifo PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(ll-us-kfifo PROPERTIES COMPILE_FLAGS "-DLOCALLY_LINEARIZABLE -Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ll-us-kfifo PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ll-us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ll-us-kfifo PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ll-us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ll-us-kfifo#target
set(TARGET "seqalt-ll-us-kfifo")
set(TOOLSET "target")
set(seqalt-ll-us-kfifo__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ll-us-kfifo__dummy_srcs}")
  file(WRITE "${seqalt-ll-us-kfifo__dummy_srcs}" "")
endif()
add_executable(seqalt-ll-us-kfifo ${seqalt-ll-us-kfifo__dummy_srcs})
set_target_properties(seqalt-ll-us-kfifo PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ll-us-kfifo PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ll-us-kfifo PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ll-us-kfifo PROPERTIES PREFIX "")
set_target_properties(seqalt-ll-us-kfifo PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ll-us-kfifo")
set_target_properties(seqalt-ll-us-kfifo PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ll-us-kfifo PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ll-us-kfifo__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ll-us-kfifo APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ll-us-kfifo__include_dirs})
set_target_properties(seqalt-ll-us-kfifo PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ll-us-kfifo PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ll-us-kfifo PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ll-us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ll-us-kfifo PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ll-us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ll-us-kfifo
-Wl,--start-group
  libscal
  seqalt-base
  ll-us-kfifo
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ll-us-kfifo#target
set(TARGET "prodcon-ll-us-kfifo")
set(TOOLSET "target")
set(prodcon-ll-us-kfifo__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ll-us-kfifo__dummy_srcs}")
  file(WRITE "${prodcon-ll-us-kfifo__dummy_srcs}" "")
endif()
add_executable(prodcon-ll-us-kfifo ${prodcon-ll-us-kfifo__dummy_srcs})
set_target_properties(prodcon-ll-us-kfifo PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ll-us-kfifo PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ll-us-kfifo PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ll-us-kfifo PROPERTIES PREFIX "")
set_target_properties(prodcon-ll-us-kfifo PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ll-us-kfifo")
set_target_properties(prodcon-ll-us-kfifo PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ll-us-kfifo PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ll-us-kfifo__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ll-us-kfifo APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ll-us-kfifo__include_dirs})
set_target_properties(prodcon-ll-us-kfifo PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ll-us-kfifo PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ll-us-kfifo PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ll-us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ll-us-kfifo PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ll-us-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ll-us-kfifo
-Wl,--start-group
  libscal
  prodcon-base
  ll-us-kfifo
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ll-kstack#target
set(TARGET "ll-kstack")
set(TOOLSET "target")
set(ll-kstack__cxx_srcs "../../src/benchmark/std_glue/glue_ll_kstack.cc")
add_library(ll-kstack STATIC ${ll-kstack__cxx_srcs})
set_target_properties(ll-kstack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ll-kstack PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ll-kstack PROPERTIES PREFIX "lib")
set_target_properties(ll-kstack PROPERTIES ARCHIVE_OUTPUT_NAME "ll-kstack")
set_target_properties(ll-kstack PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libll-kstack.a PROPERTIES GENERATED "TRUE")
list(APPEND ll-kstack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ll-kstack APPEND PROPERTY INCLUDE_DIRECTORIES ${ll-kstack__include_dirs})
set_target_properties(ll-kstack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(ll-kstack PROPERTIES COMPILE_FLAGS "-DLOCALLY_LINEARIZABLE -Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ll-kstack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ll-kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ll-kstack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ll-kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ll-kstack#target
set(TARGET "seqalt-ll-kstack")
set(TOOLSET "target")
set(seqalt-ll-kstack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ll-kstack__dummy_srcs}")
  file(WRITE "${seqalt-ll-kstack__dummy_srcs}" "")
endif()
add_executable(seqalt-ll-kstack ${seqalt-ll-kstack__dummy_srcs})
set_target_properties(seqalt-ll-kstack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ll-kstack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ll-kstack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ll-kstack PROPERTIES PREFIX "")
set_target_properties(seqalt-ll-kstack PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ll-kstack")
set_target_properties(seqalt-ll-kstack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ll-kstack PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ll-kstack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ll-kstack APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ll-kstack__include_dirs})
set_target_properties(seqalt-ll-kstack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ll-kstack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ll-kstack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ll-kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ll-kstack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ll-kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ll-kstack
-Wl,--start-group
  libscal
  seqalt-base
  ll-kstack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ll-kstack#target
set(TARGET "prodcon-ll-kstack")
set(TOOLSET "target")
set(prodcon-ll-kstack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ll-kstack__dummy_srcs}")
  file(WRITE "${prodcon-ll-kstack__dummy_srcs}" "")
endif()
add_executable(prodcon-ll-kstack ${prodcon-ll-kstack__dummy_srcs})
set_target_properties(prodcon-ll-kstack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ll-kstack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ll-kstack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ll-kstack PROPERTIES PREFIX "")
set_target_properties(prodcon-ll-kstack PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ll-kstack")
set_target_properties(prodcon-ll-kstack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ll-kstack PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ll-kstack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ll-kstack APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ll-kstack__include_dirs})
set_target_properties(prodcon-ll-kstack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ll-kstack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ll-kstack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ll-kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ll-kstack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ll-kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ll-kstack
-Wl,--start-group
  libscal
  prodcon-base
  ll-kstack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ll-dyn-dds-treiber-nonlinempty#target
set(TARGET "ll-dyn-dds-treiber-nonlinempty")
set(TOOLSET "target")
set(ll-dyn-dds-treiber-nonlinempty__cxx_srcs "../../src/benchmark/std_glue/glue_dyn_dds.cc")
add_library(ll-dyn-dds-treiber-nonlinempty STATIC ${ll-dyn-dds-treiber-nonlinempty__cxx_srcs})
set_target_properties(ll-dyn-dds-treiber-nonlinempty PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ll-dyn-dds-treiber-nonlinempty PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ll-dyn-dds-treiber-nonlinempty PROPERTIES PREFIX "lib")
set_target_properties(ll-dyn-dds-treiber-nonlinempty PROPERTIES ARCHIVE_OUTPUT_NAME "ll-dyn-dds-treiber-nonlinempty")
set_target_properties(ll-dyn-dds-treiber-nonlinempty PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libll-dyn-dds-treiber-nonlinempty.a PROPERTIES GENERATED "TRUE")
list(APPEND ll-dyn-dds-treiber-nonlinempty__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ll-dyn-dds-treiber-nonlinempty APPEND PROPERTY INCLUDE_DIRECTORIES ${ll-dyn-dds-treiber-nonlinempty__include_dirs})
set_target_properties(ll-dyn-dds-treiber-nonlinempty PROPERTIES COMPILE_DEFINITIONS "BACKEND_TREIBER;NON_LINEARIZABLE_EMPTY;__STDC_FORMAT_MACROS=1;")
set_target_properties(ll-dyn-dds-treiber-nonlinempty PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ll-dyn-dds-treiber-nonlinempty PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ll-dyn-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ll-dyn-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ll-dyn-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ll-dyn-dds-treiber-nonlinempty#target
set(TARGET "prodcon-ll-dyn-dds-treiber-nonlinempty")
set(TOOLSET "target")
set(prodcon-ll-dyn-dds-treiber-nonlinempty__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ll-dyn-dds-treiber-nonlinempty__dummy_srcs}")
  file(WRITE "${prodcon-ll-dyn-dds-treiber-nonlinempty__dummy_srcs}" "")
endif()
add_executable(prodcon-ll-dyn-dds-treiber-nonlinempty ${prodcon-ll-dyn-dds-treiber-nonlinempty__dummy_srcs})
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES PREFIX "")
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ll-dyn-dds-treiber-nonlinempty")
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ll-dyn-dds-treiber-nonlinempty__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ll-dyn-dds-treiber-nonlinempty APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ll-dyn-dds-treiber-nonlinempty__include_dirs})
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ll-dyn-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ll-dyn-dds-treiber-nonlinempty
-Wl,--start-group
  libscal
  prodcon-base
  ll-dyn-dds-treiber-nonlinempty
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ll-dyn-dds-treiber#target
set(TARGET "ll-dyn-dds-treiber")
set(TOOLSET "target")
set(ll-dyn-dds-treiber__cxx_srcs "../../src/benchmark/std_glue/glue_ll_dyn_dds_treiber.cc")
add_library(ll-dyn-dds-treiber STATIC ${ll-dyn-dds-treiber__cxx_srcs})
set_target_properties(ll-dyn-dds-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ll-dyn-dds-treiber PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ll-dyn-dds-treiber PROPERTIES PREFIX "lib")
set_target_properties(ll-dyn-dds-treiber PROPERTIES ARCHIVE_OUTPUT_NAME "ll-dyn-dds-treiber")
set_target_properties(ll-dyn-dds-treiber PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libll-dyn-dds-treiber.a PROPERTIES GENERATED "TRUE")
list(APPEND ll-dyn-dds-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ll-dyn-dds-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${ll-dyn-dds-treiber__include_dirs})
set_target_properties(ll-dyn-dds-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(ll-dyn-dds-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ll-dyn-dds-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ll-dyn-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ll-dyn-dds-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ll-dyn-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ll-dyn-dds-treiber#target
set(TARGET "seqalt-ll-dyn-dds-treiber")
set(TOOLSET "target")
set(seqalt-ll-dyn-dds-treiber__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ll-dyn-dds-treiber__dummy_srcs}")
  file(WRITE "${seqalt-ll-dyn-dds-treiber__dummy_srcs}" "")
endif()
add_executable(seqalt-ll-dyn-dds-treiber ${seqalt-ll-dyn-dds-treiber__dummy_srcs})
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES PREFIX "")
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ll-dyn-dds-treiber")
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ll-dyn-dds-treiber PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ll-dyn-dds-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ll-dyn-dds-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ll-dyn-dds-treiber__include_dirs})
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ll-dyn-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ll-dyn-dds-treiber
-Wl,--start-group
  libscal
  seqalt-base
  ll-dyn-dds-treiber
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ll-dyn-dds-treiber#target
set(TARGET "prodcon-ll-dyn-dds-treiber")
set(TOOLSET "target")
set(prodcon-ll-dyn-dds-treiber__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ll-dyn-dds-treiber__dummy_srcs}")
  file(WRITE "${prodcon-ll-dyn-dds-treiber__dummy_srcs}" "")
endif()
add_executable(prodcon-ll-dyn-dds-treiber ${prodcon-ll-dyn-dds-treiber__dummy_srcs})
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES PREFIX "")
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ll-dyn-dds-treiber")
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ll-dyn-dds-treiber PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ll-dyn-dds-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ll-dyn-dds-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ll-dyn-dds-treiber__include_dirs})
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ll-dyn-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ll-dyn-dds-treiber
-Wl,--start-group
  libscal
  prodcon-base
  ll-dyn-dds-treiber
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ll-dyn-dds-ms-nonlinempty#target
set(TARGET "ll-dyn-dds-ms-nonlinempty")
set(TOOLSET "target")
set(ll-dyn-dds-ms-nonlinempty__cxx_srcs "../../src/benchmark/std_glue/glue_dyn_dds.cc")
add_library(ll-dyn-dds-ms-nonlinempty STATIC ${ll-dyn-dds-ms-nonlinempty__cxx_srcs})
set_target_properties(ll-dyn-dds-ms-nonlinempty PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ll-dyn-dds-ms-nonlinempty PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ll-dyn-dds-ms-nonlinempty PROPERTIES PREFIX "lib")
set_target_properties(ll-dyn-dds-ms-nonlinempty PROPERTIES ARCHIVE_OUTPUT_NAME "ll-dyn-dds-ms-nonlinempty")
set_target_properties(ll-dyn-dds-ms-nonlinempty PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libll-dyn-dds-ms-nonlinempty.a PROPERTIES GENERATED "TRUE")
list(APPEND ll-dyn-dds-ms-nonlinempty__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ll-dyn-dds-ms-nonlinempty APPEND PROPERTY INCLUDE_DIRECTORIES ${ll-dyn-dds-ms-nonlinempty__include_dirs})
set_target_properties(ll-dyn-dds-ms-nonlinempty PROPERTIES COMPILE_DEFINITIONS "BACKEND_MS_QUEUE;NON_LINEARIZABLE_EMPTY;__STDC_FORMAT_MACROS=1;")
set_target_properties(ll-dyn-dds-ms-nonlinempty PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ll-dyn-dds-ms-nonlinempty PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ll-dyn-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ll-dyn-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ll-dyn-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ll-dyn-dds-ms-nonlinempty#target
set(TARGET "prodcon-ll-dyn-dds-ms-nonlinempty")
set(TOOLSET "target")
set(prodcon-ll-dyn-dds-ms-nonlinempty__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ll-dyn-dds-ms-nonlinempty__dummy_srcs}")
  file(WRITE "${prodcon-ll-dyn-dds-ms-nonlinempty__dummy_srcs}" "")
endif()
add_executable(prodcon-ll-dyn-dds-ms-nonlinempty ${prodcon-ll-dyn-dds-ms-nonlinempty__dummy_srcs})
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES PREFIX "")
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ll-dyn-dds-ms-nonlinempty")
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ll-dyn-dds-ms-nonlinempty__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ll-dyn-dds-ms-nonlinempty APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ll-dyn-dds-ms-nonlinempty__include_dirs})
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ll-dyn-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ll-dyn-dds-ms-nonlinempty
-Wl,--start-group
  libscal
  prodcon-base
  ll-dyn-dds-ms-nonlinempty
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ll-dyn-dds-ms#target
set(TARGET "ll-dyn-dds-ms")
set(TOOLSET "target")
set(ll-dyn-dds-ms__cxx_srcs "../../src/benchmark/std_glue/glue_ll_dyn_dds_ms.cc")
add_library(ll-dyn-dds-ms STATIC ${ll-dyn-dds-ms__cxx_srcs})
set_target_properties(ll-dyn-dds-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ll-dyn-dds-ms PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ll-dyn-dds-ms PROPERTIES PREFIX "lib")
set_target_properties(ll-dyn-dds-ms PROPERTIES ARCHIVE_OUTPUT_NAME "ll-dyn-dds-ms")
set_target_properties(ll-dyn-dds-ms PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libll-dyn-dds-ms.a PROPERTIES GENERATED "TRUE")
list(APPEND ll-dyn-dds-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ll-dyn-dds-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${ll-dyn-dds-ms__include_dirs})
set_target_properties(ll-dyn-dds-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(ll-dyn-dds-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ll-dyn-dds-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ll-dyn-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ll-dyn-dds-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ll-dyn-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ll-dyn-dds-ms#target
set(TARGET "seqalt-ll-dyn-dds-ms")
set(TOOLSET "target")
set(seqalt-ll-dyn-dds-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ll-dyn-dds-ms__dummy_srcs}")
  file(WRITE "${seqalt-ll-dyn-dds-ms__dummy_srcs}" "")
endif()
add_executable(seqalt-ll-dyn-dds-ms ${seqalt-ll-dyn-dds-ms__dummy_srcs})
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES PREFIX "")
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ll-dyn-dds-ms")
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ll-dyn-dds-ms PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ll-dyn-dds-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ll-dyn-dds-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ll-dyn-dds-ms__include_dirs})
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ll-dyn-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ll-dyn-dds-ms
-Wl,--start-group
  libscal
  seqalt-base
  ll-dyn-dds-ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ll-dyn-dds-ms#target
set(TARGET "prodcon-ll-dyn-dds-ms")
set(TOOLSET "target")
set(prodcon-ll-dyn-dds-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ll-dyn-dds-ms__dummy_srcs}")
  file(WRITE "${prodcon-ll-dyn-dds-ms__dummy_srcs}" "")
endif()
add_executable(prodcon-ll-dyn-dds-ms ${prodcon-ll-dyn-dds-ms__dummy_srcs})
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES PREFIX "")
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ll-dyn-dds-ms")
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ll-dyn-dds-ms PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ll-dyn-dds-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ll-dyn-dds-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ll-dyn-dds-ms__include_dirs})
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ll-dyn-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ll-dyn-dds-ms
-Wl,--start-group
  libscal
  prodcon-base
  ll-dyn-dds-ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ll-dds-treiber-nonlinempty#target
set(TARGET "ll-dds-treiber-nonlinempty")
set(TOOLSET "target")
set(ll-dds-treiber-nonlinempty__cxx_srcs "../../src/benchmark/std_glue/glue_dds.cc")
add_library(ll-dds-treiber-nonlinempty STATIC ${ll-dds-treiber-nonlinempty__cxx_srcs})
set_target_properties(ll-dds-treiber-nonlinempty PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ll-dds-treiber-nonlinempty PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ll-dds-treiber-nonlinempty PROPERTIES PREFIX "lib")
set_target_properties(ll-dds-treiber-nonlinempty PROPERTIES ARCHIVE_OUTPUT_NAME "ll-dds-treiber-nonlinempty")
set_target_properties(ll-dds-treiber-nonlinempty PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libll-dds-treiber-nonlinempty.a PROPERTIES GENERATED "TRUE")
list(APPEND ll-dds-treiber-nonlinempty__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ll-dds-treiber-nonlinempty APPEND PROPERTY INCLUDE_DIRECTORIES ${ll-dds-treiber-nonlinempty__include_dirs})
set_target_properties(ll-dds-treiber-nonlinempty PROPERTIES COMPILE_DEFINITIONS "BACKEND_TREIBER;BALANCER_LL;NON_LINEARIZABLE_EMPTY;__STDC_FORMAT_MACROS=1;")
set_target_properties(ll-dds-treiber-nonlinempty PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ll-dds-treiber-nonlinempty PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ll-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ll-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ll-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ll-dds-treiber-nonlinempty#target
set(TARGET "prodcon-ll-dds-treiber-nonlinempty")
set(TOOLSET "target")
set(prodcon-ll-dds-treiber-nonlinempty__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ll-dds-treiber-nonlinempty__dummy_srcs}")
  file(WRITE "${prodcon-ll-dds-treiber-nonlinempty__dummy_srcs}" "")
endif()
add_executable(prodcon-ll-dds-treiber-nonlinempty ${prodcon-ll-dds-treiber-nonlinempty__dummy_srcs})
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES PREFIX "")
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ll-dds-treiber-nonlinempty")
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ll-dds-treiber-nonlinempty PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ll-dds-treiber-nonlinempty__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ll-dds-treiber-nonlinempty APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ll-dds-treiber-nonlinempty__include_dirs})
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ll-dds-treiber-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ll-dds-treiber-nonlinempty
-Wl,--start-group
  libscal
  prodcon-base
  ll-dds-treiber-nonlinempty
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ll-dds-treiber#target
set(TARGET "ll-dds-treiber")
set(TOOLSET "target")
set(ll-dds-treiber__cxx_srcs "../../src/benchmark/std_glue/glue_ll_dds_treiber.cc")
add_library(ll-dds-treiber STATIC ${ll-dds-treiber__cxx_srcs})
set_target_properties(ll-dds-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ll-dds-treiber PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ll-dds-treiber PROPERTIES PREFIX "lib")
set_target_properties(ll-dds-treiber PROPERTIES ARCHIVE_OUTPUT_NAME "ll-dds-treiber")
set_target_properties(ll-dds-treiber PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libll-dds-treiber.a PROPERTIES GENERATED "TRUE")
list(APPEND ll-dds-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ll-dds-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${ll-dds-treiber__include_dirs})
set_target_properties(ll-dds-treiber PROPERTIES COMPILE_DEFINITIONS "GET_TRY_LOCAL_FIRST;__STDC_FORMAT_MACROS=1;")
set_target_properties(ll-dds-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ll-dds-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ll-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ll-dds-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ll-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ll-dds-treiber#target
set(TARGET "seqalt-ll-dds-treiber")
set(TOOLSET "target")
set(seqalt-ll-dds-treiber__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ll-dds-treiber__dummy_srcs}")
  file(WRITE "${seqalt-ll-dds-treiber__dummy_srcs}" "")
endif()
add_executable(seqalt-ll-dds-treiber ${seqalt-ll-dds-treiber__dummy_srcs})
set_target_properties(seqalt-ll-dds-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ll-dds-treiber PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ll-dds-treiber PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ll-dds-treiber PROPERTIES PREFIX "")
set_target_properties(seqalt-ll-dds-treiber PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ll-dds-treiber")
set_target_properties(seqalt-ll-dds-treiber PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ll-dds-treiber PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ll-dds-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ll-dds-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ll-dds-treiber__include_dirs})
set_target_properties(seqalt-ll-dds-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ll-dds-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ll-dds-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ll-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ll-dds-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ll-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ll-dds-treiber
-Wl,--start-group
  libscal
  seqalt-base
  ll-dds-treiber
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ll-dds-treiber#target
set(TARGET "prodcon-ll-dds-treiber")
set(TOOLSET "target")
set(prodcon-ll-dds-treiber__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ll-dds-treiber__dummy_srcs}")
  file(WRITE "${prodcon-ll-dds-treiber__dummy_srcs}" "")
endif()
add_executable(prodcon-ll-dds-treiber ${prodcon-ll-dds-treiber__dummy_srcs})
set_target_properties(prodcon-ll-dds-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ll-dds-treiber PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ll-dds-treiber PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ll-dds-treiber PROPERTIES PREFIX "")
set_target_properties(prodcon-ll-dds-treiber PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ll-dds-treiber")
set_target_properties(prodcon-ll-dds-treiber PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ll-dds-treiber PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ll-dds-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ll-dds-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ll-dds-treiber__include_dirs})
set_target_properties(prodcon-ll-dds-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ll-dds-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ll-dds-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ll-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ll-dds-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ll-dds-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ll-dds-treiber
-Wl,--start-group
  libscal
  prodcon-base
  ll-dds-treiber
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ll-dds-ms-nonlinempty#target
set(TARGET "ll-dds-ms-nonlinempty")
set(TOOLSET "target")
set(ll-dds-ms-nonlinempty__cxx_srcs "../../src/benchmark/std_glue/glue_dds.cc")
add_library(ll-dds-ms-nonlinempty STATIC ${ll-dds-ms-nonlinempty__cxx_srcs})
set_target_properties(ll-dds-ms-nonlinempty PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ll-dds-ms-nonlinempty PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ll-dds-ms-nonlinempty PROPERTIES PREFIX "lib")
set_target_properties(ll-dds-ms-nonlinempty PROPERTIES ARCHIVE_OUTPUT_NAME "ll-dds-ms-nonlinempty")
set_target_properties(ll-dds-ms-nonlinempty PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libll-dds-ms-nonlinempty.a PROPERTIES GENERATED "TRUE")
list(APPEND ll-dds-ms-nonlinempty__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ll-dds-ms-nonlinempty APPEND PROPERTY INCLUDE_DIRECTORIES ${ll-dds-ms-nonlinempty__include_dirs})
set_target_properties(ll-dds-ms-nonlinempty PROPERTIES COMPILE_DEFINITIONS "BACKEND_MS_QUEUE;BALANCER_LL;NON_LINEARIZABLE_EMPTY;__STDC_FORMAT_MACROS=1;")
set_target_properties(ll-dds-ms-nonlinempty PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ll-dds-ms-nonlinempty PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ll-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ll-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ll-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ll-dds-ms-nonlinempty#target
set(TARGET "prodcon-ll-dds-ms-nonlinempty")
set(TOOLSET "target")
set(prodcon-ll-dds-ms-nonlinempty__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ll-dds-ms-nonlinempty__dummy_srcs}")
  file(WRITE "${prodcon-ll-dds-ms-nonlinempty__dummy_srcs}" "")
endif()
add_executable(prodcon-ll-dds-ms-nonlinempty ${prodcon-ll-dds-ms-nonlinempty__dummy_srcs})
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES PREFIX "")
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ll-dds-ms-nonlinempty")
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ll-dds-ms-nonlinempty PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ll-dds-ms-nonlinempty__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ll-dds-ms-nonlinempty APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ll-dds-ms-nonlinempty__include_dirs})
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ll-dds-ms-nonlinempty PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ll-dds-ms-nonlinempty
-Wl,--start-group
  libscal
  prodcon-base
  ll-dds-ms-nonlinempty
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:ll-dds-ms#target
set(TARGET "ll-dds-ms")
set(TOOLSET "target")
set(ll-dds-ms__cxx_srcs "../../src/benchmark/std_glue/glue_ll_dds_ms.cc")
add_library(ll-dds-ms STATIC ${ll-dds-ms__cxx_srcs})
set_target_properties(ll-dds-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(ll-dds-ms PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(ll-dds-ms PROPERTIES PREFIX "lib")
set_target_properties(ll-dds-ms PROPERTIES ARCHIVE_OUTPUT_NAME "ll-dds-ms")
set_target_properties(ll-dds-ms PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libll-dds-ms.a PROPERTIES GENERATED "TRUE")
list(APPEND ll-dds-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET ll-dds-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${ll-dds-ms__include_dirs})
set_target_properties(ll-dds-ms PROPERTIES COMPILE_DEFINITIONS "GET_TRY_LOCAL_FIRST;__STDC_FORMAT_MACROS=1;")
set_target_properties(ll-dds-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(ll-dds-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(ll-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(ll-dds-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(ll-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-ll-dds-ms#target
set(TARGET "seqalt-ll-dds-ms")
set(TOOLSET "target")
set(seqalt-ll-dds-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-ll-dds-ms__dummy_srcs}")
  file(WRITE "${seqalt-ll-dds-ms__dummy_srcs}" "")
endif()
add_executable(seqalt-ll-dds-ms ${seqalt-ll-dds-ms__dummy_srcs})
set_target_properties(seqalt-ll-dds-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-ll-dds-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-ll-dds-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-ll-dds-ms PROPERTIES PREFIX "")
set_target_properties(seqalt-ll-dds-ms PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-ll-dds-ms")
set_target_properties(seqalt-ll-dds-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-ll-dds-ms PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-ll-dds-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-ll-dds-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-ll-dds-ms__include_dirs})
set_target_properties(seqalt-ll-dds-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-ll-dds-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-ll-dds-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-ll-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-ll-dds-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-ll-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-ll-dds-ms
-Wl,--start-group
  libscal
  seqalt-base
  ll-dds-ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-ll-dds-ms#target
set(TARGET "prodcon-ll-dds-ms")
set(TOOLSET "target")
set(prodcon-ll-dds-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-ll-dds-ms__dummy_srcs}")
  file(WRITE "${prodcon-ll-dds-ms__dummy_srcs}" "")
endif()
add_executable(prodcon-ll-dds-ms ${prodcon-ll-dds-ms__dummy_srcs})
set_target_properties(prodcon-ll-dds-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-ll-dds-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-ll-dds-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-ll-dds-ms PROPERTIES PREFIX "")
set_target_properties(prodcon-ll-dds-ms PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-ll-dds-ms")
set_target_properties(prodcon-ll-dds-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-ll-dds-ms PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-ll-dds-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-ll-dds-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-ll-dds-ms__include_dirs})
set_target_properties(prodcon-ll-dds-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-ll-dds-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-ll-dds-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-ll-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-ll-dds-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-ll-dds-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-ll-dds-ms
-Wl,--start-group
  libscal
  prodcon-base
  ll-dds-ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:lb-stack#target
set(TARGET "lb-stack")
set(TOOLSET "target")
set(lb-stack__cxx_srcs "../../src/benchmark/std_glue/glue_lb_stack.cc")
add_library(lb-stack STATIC ${lb-stack__cxx_srcs})
set_target_properties(lb-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(lb-stack PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(lb-stack PROPERTIES PREFIX "lib")
set_target_properties(lb-stack PROPERTIES ARCHIVE_OUTPUT_NAME "lb-stack")
set_target_properties(lb-stack PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/liblb-stack.a PROPERTIES GENERATED "TRUE")
list(APPEND lb-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET lb-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${lb-stack__include_dirs})
set_target_properties(lb-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(lb-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(lb-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(lb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(lb-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(lb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-lb-stack#target
set(TARGET "seqalt-lb-stack")
set(TOOLSET "target")
set(seqalt-lb-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-lb-stack__dummy_srcs}")
  file(WRITE "${seqalt-lb-stack__dummy_srcs}" "")
endif()
add_executable(seqalt-lb-stack ${seqalt-lb-stack__dummy_srcs})
set_target_properties(seqalt-lb-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-lb-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-lb-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-lb-stack PROPERTIES PREFIX "")
set_target_properties(seqalt-lb-stack PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-lb-stack")
set_target_properties(seqalt-lb-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-lb-stack PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-lb-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-lb-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-lb-stack__include_dirs})
set_target_properties(seqalt-lb-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-lb-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-lb-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-lb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-lb-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-lb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-lb-stack
-Wl,--start-group
  libscal
  seqalt-base
  lb-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-lb-stack#target
set(TARGET "prodcon-lb-stack")
set(TOOLSET "target")
set(prodcon-lb-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-lb-stack__dummy_srcs}")
  file(WRITE "${prodcon-lb-stack__dummy_srcs}" "")
endif()
add_executable(prodcon-lb-stack ${prodcon-lb-stack__dummy_srcs})
set_target_properties(prodcon-lb-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-lb-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-lb-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-lb-stack PROPERTIES PREFIX "")
set_target_properties(prodcon-lb-stack PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-lb-stack")
set_target_properties(prodcon-lb-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-lb-stack PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-lb-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-lb-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-lb-stack__include_dirs})
set_target_properties(prodcon-lb-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-lb-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-lb-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-lb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-lb-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-lb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-lb-stack
-Wl,--start-group
  libscal
  prodcon-base
  lb-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:lb-queue#target
set(TARGET "lb-queue")
set(TOOLSET "target")
set(lb-queue__cxx_srcs "../../src/benchmark/std_glue/glue_lb_queue.cc")
add_library(lb-queue STATIC ${lb-queue__cxx_srcs})
set_target_properties(lb-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(lb-queue PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(lb-queue PROPERTIES PREFIX "lib")
set_target_properties(lb-queue PROPERTIES ARCHIVE_OUTPUT_NAME "lb-queue")
set_target_properties(lb-queue PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/liblb-queue.a PROPERTIES GENERATED "TRUE")
list(APPEND lb-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET lb-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${lb-queue__include_dirs})
set_target_properties(lb-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(lb-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(lb-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(lb-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(lb-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(lb-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-lb-queue#target
set(TARGET "seqalt-lb-queue")
set(TOOLSET "target")
set(seqalt-lb-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-lb-queue__dummy_srcs}")
  file(WRITE "${seqalt-lb-queue__dummy_srcs}" "")
endif()
add_executable(seqalt-lb-queue ${seqalt-lb-queue__dummy_srcs})
set_target_properties(seqalt-lb-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-lb-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-lb-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-lb-queue PROPERTIES PREFIX "")
set_target_properties(seqalt-lb-queue PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-lb-queue")
set_target_properties(seqalt-lb-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-lb-queue PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-lb-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-lb-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-lb-queue__include_dirs})
set_target_properties(seqalt-lb-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-lb-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-lb-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-lb-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-lb-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-lb-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-lb-queue
-Wl,--start-group
  libscal
  seqalt-base
  lb-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-lb-queue#target
set(TARGET "prodcon-lb-queue")
set(TOOLSET "target")
set(prodcon-lb-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-lb-queue__dummy_srcs}")
  file(WRITE "${prodcon-lb-queue__dummy_srcs}" "")
endif()
add_executable(prodcon-lb-queue ${prodcon-lb-queue__dummy_srcs})
set_target_properties(prodcon-lb-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-lb-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-lb-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-lb-queue PROPERTIES PREFIX "")
set_target_properties(prodcon-lb-queue PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-lb-queue")
set_target_properties(prodcon-lb-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-lb-queue PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-lb-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-lb-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-lb-queue__include_dirs})
set_target_properties(prodcon-lb-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-lb-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-lb-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-lb-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-lb-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-lb-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-lb-queue
-Wl,--start-group
  libscal
  prodcon-base
  lb-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:kstack#target
set(TARGET "kstack")
set(TOOLSET "target")
set(kstack__cxx_srcs "../../src/benchmark/std_glue/glue_kstack.cc")
add_library(kstack STATIC ${kstack__cxx_srcs})
set_target_properties(kstack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(kstack PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(kstack PROPERTIES PREFIX "lib")
set_target_properties(kstack PROPERTIES ARCHIVE_OUTPUT_NAME "kstack")
set_target_properties(kstack PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libkstack.a PROPERTIES GENERATED "TRUE")
list(APPEND kstack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET kstack APPEND PROPERTY INCLUDE_DIRECTORIES ${kstack__include_dirs})
set_target_properties(kstack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(kstack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(kstack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(kstack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-kstack#target
set(TARGET "seqalt-kstack")
set(TOOLSET "target")
set(seqalt-kstack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-kstack__dummy_srcs}")
  file(WRITE "${seqalt-kstack__dummy_srcs}" "")
endif()
add_executable(seqalt-kstack ${seqalt-kstack__dummy_srcs})
set_target_properties(seqalt-kstack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-kstack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-kstack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-kstack PROPERTIES PREFIX "")
set_target_properties(seqalt-kstack PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-kstack")
set_target_properties(seqalt-kstack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-kstack PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-kstack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-kstack APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-kstack__include_dirs})
set_target_properties(seqalt-kstack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-kstack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-kstack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-kstack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-kstack
-Wl,--start-group
  libscal
  seqalt-base
  kstack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-kstack#target
set(TARGET "prodcon-kstack")
set(TOOLSET "target")
set(prodcon-kstack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-kstack__dummy_srcs}")
  file(WRITE "${prodcon-kstack__dummy_srcs}" "")
endif()
add_executable(prodcon-kstack ${prodcon-kstack__dummy_srcs})
set_target_properties(prodcon-kstack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-kstack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-kstack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-kstack PROPERTIES PREFIX "")
set_target_properties(prodcon-kstack PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-kstack")
set_target_properties(prodcon-kstack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-kstack PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-kstack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-kstack APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-kstack__include_dirs})
set_target_properties(prodcon-kstack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-kstack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-kstack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-kstack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-kstack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-kstack
-Wl,--start-group
  libscal
  prodcon-base
  kstack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:hc-ts-stutter-stack#target
set(TARGET "hc-ts-stutter-stack")
set(TOOLSET "target")
set(hc-ts-stutter-stack__cxx_srcs "../../src/benchmark/std_glue/glue_hardcoded_ts_stutter_stack.cc")
add_library(hc-ts-stutter-stack STATIC ${hc-ts-stutter-stack__cxx_srcs})
set_target_properties(hc-ts-stutter-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(hc-ts-stutter-stack PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(hc-ts-stutter-stack PROPERTIES PREFIX "lib")
set_target_properties(hc-ts-stutter-stack PROPERTIES ARCHIVE_OUTPUT_NAME "hc-ts-stutter-stack")
set_target_properties(hc-ts-stutter-stack PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libhc-ts-stutter-stack.a PROPERTIES GENERATED "TRUE")
list(APPEND hc-ts-stutter-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET hc-ts-stutter-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${hc-ts-stutter-stack__include_dirs})
set_target_properties(hc-ts-stutter-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(hc-ts-stutter-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(hc-ts-stutter-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(hc-ts-stutter-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(hc-ts-stutter-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(hc-ts-stutter-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-hc-ts-stutter-stack#target
set(TARGET "seqalt-hc-ts-stutter-stack")
set(TOOLSET "target")
set(seqalt-hc-ts-stutter-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-hc-ts-stutter-stack__dummy_srcs}")
  file(WRITE "${seqalt-hc-ts-stutter-stack__dummy_srcs}" "")
endif()
add_executable(seqalt-hc-ts-stutter-stack ${seqalt-hc-ts-stutter-stack__dummy_srcs})
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES PREFIX "")
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-hc-ts-stutter-stack")
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-hc-ts-stutter-stack PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-hc-ts-stutter-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-hc-ts-stutter-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-hc-ts-stutter-stack__include_dirs})
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-hc-ts-stutter-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-hc-ts-stutter-stack
-Wl,--start-group
  libscal
  seqalt-base
  hc-ts-stutter-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-hc-ts-stutter-stack#target
set(TARGET "prodcon-hc-ts-stutter-stack")
set(TOOLSET "target")
set(prodcon-hc-ts-stutter-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-hc-ts-stutter-stack__dummy_srcs}")
  file(WRITE "${prodcon-hc-ts-stutter-stack__dummy_srcs}" "")
endif()
add_executable(prodcon-hc-ts-stutter-stack ${prodcon-hc-ts-stutter-stack__dummy_srcs})
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES PREFIX "")
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-hc-ts-stutter-stack")
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-hc-ts-stutter-stack PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-hc-ts-stutter-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-hc-ts-stutter-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-hc-ts-stutter-stack__include_dirs})
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-hc-ts-stutter-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-hc-ts-stutter-stack
-Wl,--start-group
  libscal
  prodcon-base
  hc-ts-stutter-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:hc-ts-stutter-queue#target
set(TARGET "hc-ts-stutter-queue")
set(TOOLSET "target")
set(hc-ts-stutter-queue__cxx_srcs "../../src/benchmark/std_glue/glue_hardcoded_ts_stutter_queue.cc")
add_library(hc-ts-stutter-queue STATIC ${hc-ts-stutter-queue__cxx_srcs})
set_target_properties(hc-ts-stutter-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(hc-ts-stutter-queue PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(hc-ts-stutter-queue PROPERTIES PREFIX "lib")
set_target_properties(hc-ts-stutter-queue PROPERTIES ARCHIVE_OUTPUT_NAME "hc-ts-stutter-queue")
set_target_properties(hc-ts-stutter-queue PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libhc-ts-stutter-queue.a PROPERTIES GENERATED "TRUE")
list(APPEND hc-ts-stutter-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET hc-ts-stutter-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${hc-ts-stutter-queue__include_dirs})
set_target_properties(hc-ts-stutter-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(hc-ts-stutter-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(hc-ts-stutter-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(hc-ts-stutter-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(hc-ts-stutter-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(hc-ts-stutter-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-hc-ts-stutter-queue#target
set(TARGET "seqalt-hc-ts-stutter-queue")
set(TOOLSET "target")
set(seqalt-hc-ts-stutter-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-hc-ts-stutter-queue__dummy_srcs}")
  file(WRITE "${seqalt-hc-ts-stutter-queue__dummy_srcs}" "")
endif()
add_executable(seqalt-hc-ts-stutter-queue ${seqalt-hc-ts-stutter-queue__dummy_srcs})
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES PREFIX "")
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-hc-ts-stutter-queue")
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-hc-ts-stutter-queue PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-hc-ts-stutter-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-hc-ts-stutter-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-hc-ts-stutter-queue__include_dirs})
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-hc-ts-stutter-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-hc-ts-stutter-queue
-Wl,--start-group
  libscal
  seqalt-base
  hc-ts-stutter-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-hc-ts-stutter-queue#target
set(TARGET "prodcon-hc-ts-stutter-queue")
set(TOOLSET "target")
set(prodcon-hc-ts-stutter-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-hc-ts-stutter-queue__dummy_srcs}")
  file(WRITE "${prodcon-hc-ts-stutter-queue__dummy_srcs}" "")
endif()
add_executable(prodcon-hc-ts-stutter-queue ${prodcon-hc-ts-stutter-queue__dummy_srcs})
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES PREFIX "")
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-hc-ts-stutter-queue")
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-hc-ts-stutter-queue PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-hc-ts-stutter-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-hc-ts-stutter-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-hc-ts-stutter-queue__include_dirs})
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-hc-ts-stutter-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-hc-ts-stutter-queue
-Wl,--start-group
  libscal
  prodcon-base
  hc-ts-stutter-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:hc-ts-interval-stack#target
set(TARGET "hc-ts-interval-stack")
set(TOOLSET "target")
set(hc-ts-interval-stack__cxx_srcs "../../src/benchmark/std_glue/glue_hardcoded_ts_interval_stack.cc")
add_library(hc-ts-interval-stack STATIC ${hc-ts-interval-stack__cxx_srcs})
set_target_properties(hc-ts-interval-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(hc-ts-interval-stack PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(hc-ts-interval-stack PROPERTIES PREFIX "lib")
set_target_properties(hc-ts-interval-stack PROPERTIES ARCHIVE_OUTPUT_NAME "hc-ts-interval-stack")
set_target_properties(hc-ts-interval-stack PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libhc-ts-interval-stack.a PROPERTIES GENERATED "TRUE")
list(APPEND hc-ts-interval-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET hc-ts-interval-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${hc-ts-interval-stack__include_dirs})
set_target_properties(hc-ts-interval-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(hc-ts-interval-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(hc-ts-interval-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(hc-ts-interval-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(hc-ts-interval-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(hc-ts-interval-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-hc-ts-interval-stack#target
set(TARGET "seqalt-hc-ts-interval-stack")
set(TOOLSET "target")
set(seqalt-hc-ts-interval-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-hc-ts-interval-stack__dummy_srcs}")
  file(WRITE "${seqalt-hc-ts-interval-stack__dummy_srcs}" "")
endif()
add_executable(seqalt-hc-ts-interval-stack ${seqalt-hc-ts-interval-stack__dummy_srcs})
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES PREFIX "")
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-hc-ts-interval-stack")
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-hc-ts-interval-stack PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-hc-ts-interval-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-hc-ts-interval-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-hc-ts-interval-stack__include_dirs})
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-hc-ts-interval-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-hc-ts-interval-stack
-Wl,--start-group
  libscal
  seqalt-base
  hc-ts-interval-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-hc-ts-interval-stack#target
set(TARGET "prodcon-hc-ts-interval-stack")
set(TOOLSET "target")
set(prodcon-hc-ts-interval-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-hc-ts-interval-stack__dummy_srcs}")
  file(WRITE "${prodcon-hc-ts-interval-stack__dummy_srcs}" "")
endif()
add_executable(prodcon-hc-ts-interval-stack ${prodcon-hc-ts-interval-stack__dummy_srcs})
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES PREFIX "")
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-hc-ts-interval-stack")
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-hc-ts-interval-stack PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-hc-ts-interval-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-hc-ts-interval-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-hc-ts-interval-stack__include_dirs})
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-hc-ts-interval-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-hc-ts-interval-stack
-Wl,--start-group
  libscal
  prodcon-base
  hc-ts-interval-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:hc-ts-interval-queue#target
set(TARGET "hc-ts-interval-queue")
set(TOOLSET "target")
set(hc-ts-interval-queue__cxx_srcs "../../src/benchmark/std_glue/glue_hardcoded_ts_interval_queue.cc")
add_library(hc-ts-interval-queue STATIC ${hc-ts-interval-queue__cxx_srcs})
set_target_properties(hc-ts-interval-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(hc-ts-interval-queue PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(hc-ts-interval-queue PROPERTIES PREFIX "lib")
set_target_properties(hc-ts-interval-queue PROPERTIES ARCHIVE_OUTPUT_NAME "hc-ts-interval-queue")
set_target_properties(hc-ts-interval-queue PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libhc-ts-interval-queue.a PROPERTIES GENERATED "TRUE")
list(APPEND hc-ts-interval-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET hc-ts-interval-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${hc-ts-interval-queue__include_dirs})
set_target_properties(hc-ts-interval-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(hc-ts-interval-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(hc-ts-interval-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(hc-ts-interval-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(hc-ts-interval-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(hc-ts-interval-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-hc-ts-interval-queue#target
set(TARGET "seqalt-hc-ts-interval-queue")
set(TOOLSET "target")
set(seqalt-hc-ts-interval-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-hc-ts-interval-queue__dummy_srcs}")
  file(WRITE "${seqalt-hc-ts-interval-queue__dummy_srcs}" "")
endif()
add_executable(seqalt-hc-ts-interval-queue ${seqalt-hc-ts-interval-queue__dummy_srcs})
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES PREFIX "")
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-hc-ts-interval-queue")
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-hc-ts-interval-queue PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-hc-ts-interval-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-hc-ts-interval-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-hc-ts-interval-queue__include_dirs})
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-hc-ts-interval-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-hc-ts-interval-queue
-Wl,--start-group
  libscal
  seqalt-base
  hc-ts-interval-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-hc-ts-interval-queue#target
set(TARGET "prodcon-hc-ts-interval-queue")
set(TOOLSET "target")
set(prodcon-hc-ts-interval-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-hc-ts-interval-queue__dummy_srcs}")
  file(WRITE "${prodcon-hc-ts-interval-queue__dummy_srcs}" "")
endif()
add_executable(prodcon-hc-ts-interval-queue ${prodcon-hc-ts-interval-queue__dummy_srcs})
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES PREFIX "")
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-hc-ts-interval-queue")
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-hc-ts-interval-queue PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-hc-ts-interval-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-hc-ts-interval-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-hc-ts-interval-queue__include_dirs})
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-hc-ts-interval-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-hc-ts-interval-queue
-Wl,--start-group
  libscal
  prodcon-base
  hc-ts-interval-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:hc-ts-hardware-stack#target
set(TARGET "hc-ts-hardware-stack")
set(TOOLSET "target")
set(hc-ts-hardware-stack__cxx_srcs "../../src/benchmark/std_glue/glue_hardcoded_ts_hardware_stack.cc")
add_library(hc-ts-hardware-stack STATIC ${hc-ts-hardware-stack__cxx_srcs})
set_target_properties(hc-ts-hardware-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(hc-ts-hardware-stack PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(hc-ts-hardware-stack PROPERTIES PREFIX "lib")
set_target_properties(hc-ts-hardware-stack PROPERTIES ARCHIVE_OUTPUT_NAME "hc-ts-hardware-stack")
set_target_properties(hc-ts-hardware-stack PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libhc-ts-hardware-stack.a PROPERTIES GENERATED "TRUE")
list(APPEND hc-ts-hardware-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET hc-ts-hardware-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${hc-ts-hardware-stack__include_dirs})
set_target_properties(hc-ts-hardware-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(hc-ts-hardware-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(hc-ts-hardware-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(hc-ts-hardware-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(hc-ts-hardware-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(hc-ts-hardware-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-hc-ts-hardware-stack#target
set(TARGET "seqalt-hc-ts-hardware-stack")
set(TOOLSET "target")
set(seqalt-hc-ts-hardware-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-hc-ts-hardware-stack__dummy_srcs}")
  file(WRITE "${seqalt-hc-ts-hardware-stack__dummy_srcs}" "")
endif()
add_executable(seqalt-hc-ts-hardware-stack ${seqalt-hc-ts-hardware-stack__dummy_srcs})
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES PREFIX "")
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-hc-ts-hardware-stack")
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-hc-ts-hardware-stack PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-hc-ts-hardware-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-hc-ts-hardware-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-hc-ts-hardware-stack__include_dirs})
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-hc-ts-hardware-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-hc-ts-hardware-stack
-Wl,--start-group
  libscal
  seqalt-base
  hc-ts-hardware-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-hc-ts-hardware-stack#target
set(TARGET "prodcon-hc-ts-hardware-stack")
set(TOOLSET "target")
set(prodcon-hc-ts-hardware-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-hc-ts-hardware-stack__dummy_srcs}")
  file(WRITE "${prodcon-hc-ts-hardware-stack__dummy_srcs}" "")
endif()
add_executable(prodcon-hc-ts-hardware-stack ${prodcon-hc-ts-hardware-stack__dummy_srcs})
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES PREFIX "")
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-hc-ts-hardware-stack")
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-hc-ts-hardware-stack PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-hc-ts-hardware-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-hc-ts-hardware-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-hc-ts-hardware-stack__include_dirs})
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-hc-ts-hardware-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-hc-ts-hardware-stack
-Wl,--start-group
  libscal
  prodcon-base
  hc-ts-hardware-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:hc-ts-hardware-queue#target
set(TARGET "hc-ts-hardware-queue")
set(TOOLSET "target")
set(hc-ts-hardware-queue__cxx_srcs "../../src/benchmark/std_glue/glue_hardcoded_ts_hardware_queue.cc")
add_library(hc-ts-hardware-queue STATIC ${hc-ts-hardware-queue__cxx_srcs})
set_target_properties(hc-ts-hardware-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(hc-ts-hardware-queue PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(hc-ts-hardware-queue PROPERTIES PREFIX "lib")
set_target_properties(hc-ts-hardware-queue PROPERTIES ARCHIVE_OUTPUT_NAME "hc-ts-hardware-queue")
set_target_properties(hc-ts-hardware-queue PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libhc-ts-hardware-queue.a PROPERTIES GENERATED "TRUE")
list(APPEND hc-ts-hardware-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET hc-ts-hardware-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${hc-ts-hardware-queue__include_dirs})
set_target_properties(hc-ts-hardware-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(hc-ts-hardware-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(hc-ts-hardware-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(hc-ts-hardware-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(hc-ts-hardware-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(hc-ts-hardware-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-hc-ts-hardware-queue#target
set(TARGET "seqalt-hc-ts-hardware-queue")
set(TOOLSET "target")
set(seqalt-hc-ts-hardware-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-hc-ts-hardware-queue__dummy_srcs}")
  file(WRITE "${seqalt-hc-ts-hardware-queue__dummy_srcs}" "")
endif()
add_executable(seqalt-hc-ts-hardware-queue ${seqalt-hc-ts-hardware-queue__dummy_srcs})
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES PREFIX "")
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-hc-ts-hardware-queue")
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-hc-ts-hardware-queue PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-hc-ts-hardware-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-hc-ts-hardware-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-hc-ts-hardware-queue__include_dirs})
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-hc-ts-hardware-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-hc-ts-hardware-queue
-Wl,--start-group
  libscal
  seqalt-base
  hc-ts-hardware-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-hc-ts-hardware-queue#target
set(TARGET "prodcon-hc-ts-hardware-queue")
set(TOOLSET "target")
set(prodcon-hc-ts-hardware-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-hc-ts-hardware-queue__dummy_srcs}")
  file(WRITE "${prodcon-hc-ts-hardware-queue__dummy_srcs}" "")
endif()
add_executable(prodcon-hc-ts-hardware-queue ${prodcon-hc-ts-hardware-queue__dummy_srcs})
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES PREFIX "")
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-hc-ts-hardware-queue")
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-hc-ts-hardware-queue PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-hc-ts-hardware-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-hc-ts-hardware-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-hc-ts-hardware-queue__include_dirs})
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-hc-ts-hardware-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-hc-ts-hardware-queue
-Wl,--start-group
  libscal
  prodcon-base
  hc-ts-hardware-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:hc-ts-cas-stack#target
set(TARGET "hc-ts-cas-stack")
set(TOOLSET "target")
set(hc-ts-cas-stack__cxx_srcs "../../src/benchmark/std_glue/glue_hardcoded_ts_cas_stack.cc")
add_library(hc-ts-cas-stack STATIC ${hc-ts-cas-stack__cxx_srcs})
set_target_properties(hc-ts-cas-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(hc-ts-cas-stack PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(hc-ts-cas-stack PROPERTIES PREFIX "lib")
set_target_properties(hc-ts-cas-stack PROPERTIES ARCHIVE_OUTPUT_NAME "hc-ts-cas-stack")
set_target_properties(hc-ts-cas-stack PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libhc-ts-cas-stack.a PROPERTIES GENERATED "TRUE")
list(APPEND hc-ts-cas-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET hc-ts-cas-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${hc-ts-cas-stack__include_dirs})
set_target_properties(hc-ts-cas-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(hc-ts-cas-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(hc-ts-cas-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(hc-ts-cas-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(hc-ts-cas-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(hc-ts-cas-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-hc-ts-cas-stack#target
set(TARGET "seqalt-hc-ts-cas-stack")
set(TOOLSET "target")
set(seqalt-hc-ts-cas-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-hc-ts-cas-stack__dummy_srcs}")
  file(WRITE "${seqalt-hc-ts-cas-stack__dummy_srcs}" "")
endif()
add_executable(seqalt-hc-ts-cas-stack ${seqalt-hc-ts-cas-stack__dummy_srcs})
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES PREFIX "")
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-hc-ts-cas-stack")
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-hc-ts-cas-stack PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-hc-ts-cas-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-hc-ts-cas-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-hc-ts-cas-stack__include_dirs})
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-hc-ts-cas-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-hc-ts-cas-stack
-Wl,--start-group
  libscal
  seqalt-base
  hc-ts-cas-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-hc-ts-cas-stack#target
set(TARGET "prodcon-hc-ts-cas-stack")
set(TOOLSET "target")
set(prodcon-hc-ts-cas-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-hc-ts-cas-stack__dummy_srcs}")
  file(WRITE "${prodcon-hc-ts-cas-stack__dummy_srcs}" "")
endif()
add_executable(prodcon-hc-ts-cas-stack ${prodcon-hc-ts-cas-stack__dummy_srcs})
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES PREFIX "")
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-hc-ts-cas-stack")
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-hc-ts-cas-stack PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-hc-ts-cas-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-hc-ts-cas-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-hc-ts-cas-stack__include_dirs})
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-hc-ts-cas-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-hc-ts-cas-stack
-Wl,--start-group
  libscal
  prodcon-base
  hc-ts-cas-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:hc-ts-cas-queue#target
set(TARGET "hc-ts-cas-queue")
set(TOOLSET "target")
set(hc-ts-cas-queue__cxx_srcs "../../src/benchmark/std_glue/glue_hardcoded_ts_cas_queue.cc")
add_library(hc-ts-cas-queue STATIC ${hc-ts-cas-queue__cxx_srcs})
set_target_properties(hc-ts-cas-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(hc-ts-cas-queue PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(hc-ts-cas-queue PROPERTIES PREFIX "lib")
set_target_properties(hc-ts-cas-queue PROPERTIES ARCHIVE_OUTPUT_NAME "hc-ts-cas-queue")
set_target_properties(hc-ts-cas-queue PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libhc-ts-cas-queue.a PROPERTIES GENERATED "TRUE")
list(APPEND hc-ts-cas-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET hc-ts-cas-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${hc-ts-cas-queue__include_dirs})
set_target_properties(hc-ts-cas-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(hc-ts-cas-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(hc-ts-cas-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(hc-ts-cas-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(hc-ts-cas-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(hc-ts-cas-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-hc-ts-cas-queue#target
set(TARGET "seqalt-hc-ts-cas-queue")
set(TOOLSET "target")
set(seqalt-hc-ts-cas-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-hc-ts-cas-queue__dummy_srcs}")
  file(WRITE "${seqalt-hc-ts-cas-queue__dummy_srcs}" "")
endif()
add_executable(seqalt-hc-ts-cas-queue ${seqalt-hc-ts-cas-queue__dummy_srcs})
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES PREFIX "")
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-hc-ts-cas-queue")
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-hc-ts-cas-queue PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-hc-ts-cas-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-hc-ts-cas-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-hc-ts-cas-queue__include_dirs})
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-hc-ts-cas-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-hc-ts-cas-queue
-Wl,--start-group
  libscal
  seqalt-base
  hc-ts-cas-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-hc-ts-cas-queue#target
set(TARGET "prodcon-hc-ts-cas-queue")
set(TOOLSET "target")
set(prodcon-hc-ts-cas-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-hc-ts-cas-queue__dummy_srcs}")
  file(WRITE "${prodcon-hc-ts-cas-queue__dummy_srcs}" "")
endif()
add_executable(prodcon-hc-ts-cas-queue ${prodcon-hc-ts-cas-queue__dummy_srcs})
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES PREFIX "")
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-hc-ts-cas-queue")
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-hc-ts-cas-queue PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-hc-ts-cas-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-hc-ts-cas-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-hc-ts-cas-queue__include_dirs})
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-hc-ts-cas-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-hc-ts-cas-queue
-Wl,--start-group
  libscal
  prodcon-base
  hc-ts-cas-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:hc-ts-atomic-stack#target
set(TARGET "hc-ts-atomic-stack")
set(TOOLSET "target")
set(hc-ts-atomic-stack__cxx_srcs "../../src/benchmark/std_glue/glue_hardcoded_ts_atomic_stack.cc")
add_library(hc-ts-atomic-stack STATIC ${hc-ts-atomic-stack__cxx_srcs})
set_target_properties(hc-ts-atomic-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(hc-ts-atomic-stack PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(hc-ts-atomic-stack PROPERTIES PREFIX "lib")
set_target_properties(hc-ts-atomic-stack PROPERTIES ARCHIVE_OUTPUT_NAME "hc-ts-atomic-stack")
set_target_properties(hc-ts-atomic-stack PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libhc-ts-atomic-stack.a PROPERTIES GENERATED "TRUE")
list(APPEND hc-ts-atomic-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET hc-ts-atomic-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${hc-ts-atomic-stack__include_dirs})
set_target_properties(hc-ts-atomic-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(hc-ts-atomic-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(hc-ts-atomic-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(hc-ts-atomic-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(hc-ts-atomic-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(hc-ts-atomic-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-hc-ts-atomic-stack#target
set(TARGET "seqalt-hc-ts-atomic-stack")
set(TOOLSET "target")
set(seqalt-hc-ts-atomic-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-hc-ts-atomic-stack__dummy_srcs}")
  file(WRITE "${seqalt-hc-ts-atomic-stack__dummy_srcs}" "")
endif()
add_executable(seqalt-hc-ts-atomic-stack ${seqalt-hc-ts-atomic-stack__dummy_srcs})
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES PREFIX "")
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-hc-ts-atomic-stack")
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-hc-ts-atomic-stack PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-hc-ts-atomic-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-hc-ts-atomic-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-hc-ts-atomic-stack__include_dirs})
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-hc-ts-atomic-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-hc-ts-atomic-stack
-Wl,--start-group
  libscal
  seqalt-base
  hc-ts-atomic-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-hc-ts-atomic-stack#target
set(TARGET "prodcon-hc-ts-atomic-stack")
set(TOOLSET "target")
set(prodcon-hc-ts-atomic-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-hc-ts-atomic-stack__dummy_srcs}")
  file(WRITE "${prodcon-hc-ts-atomic-stack__dummy_srcs}" "")
endif()
add_executable(prodcon-hc-ts-atomic-stack ${prodcon-hc-ts-atomic-stack__dummy_srcs})
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES PREFIX "")
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-hc-ts-atomic-stack")
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-hc-ts-atomic-stack PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-hc-ts-atomic-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-hc-ts-atomic-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-hc-ts-atomic-stack__include_dirs})
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-hc-ts-atomic-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-hc-ts-atomic-stack
-Wl,--start-group
  libscal
  prodcon-base
  hc-ts-atomic-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:hc-ts-atomic-queue#target
set(TARGET "hc-ts-atomic-queue")
set(TOOLSET "target")
set(hc-ts-atomic-queue__cxx_srcs "../../src/benchmark/std_glue/glue_hardcoded_ts_atomic_queue.cc")
add_library(hc-ts-atomic-queue STATIC ${hc-ts-atomic-queue__cxx_srcs})
set_target_properties(hc-ts-atomic-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(hc-ts-atomic-queue PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(hc-ts-atomic-queue PROPERTIES PREFIX "lib")
set_target_properties(hc-ts-atomic-queue PROPERTIES ARCHIVE_OUTPUT_NAME "hc-ts-atomic-queue")
set_target_properties(hc-ts-atomic-queue PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libhc-ts-atomic-queue.a PROPERTIES GENERATED "TRUE")
list(APPEND hc-ts-atomic-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET hc-ts-atomic-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${hc-ts-atomic-queue__include_dirs})
set_target_properties(hc-ts-atomic-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(hc-ts-atomic-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(hc-ts-atomic-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(hc-ts-atomic-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(hc-ts-atomic-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(hc-ts-atomic-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-hc-ts-atomic-queue#target
set(TARGET "seqalt-hc-ts-atomic-queue")
set(TOOLSET "target")
set(seqalt-hc-ts-atomic-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-hc-ts-atomic-queue__dummy_srcs}")
  file(WRITE "${seqalt-hc-ts-atomic-queue__dummy_srcs}" "")
endif()
add_executable(seqalt-hc-ts-atomic-queue ${seqalt-hc-ts-atomic-queue__dummy_srcs})
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES PREFIX "")
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-hc-ts-atomic-queue")
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-hc-ts-atomic-queue PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-hc-ts-atomic-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-hc-ts-atomic-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-hc-ts-atomic-queue__include_dirs})
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-hc-ts-atomic-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-hc-ts-atomic-queue
-Wl,--start-group
  libscal
  seqalt-base
  hc-ts-atomic-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-hc-ts-atomic-queue#target
set(TARGET "prodcon-hc-ts-atomic-queue")
set(TOOLSET "target")
set(prodcon-hc-ts-atomic-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-hc-ts-atomic-queue__dummy_srcs}")
  file(WRITE "${prodcon-hc-ts-atomic-queue__dummy_srcs}" "")
endif()
add_executable(prodcon-hc-ts-atomic-queue ${prodcon-hc-ts-atomic-queue__dummy_srcs})
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES PREFIX "")
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-hc-ts-atomic-queue")
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-hc-ts-atomic-queue PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-hc-ts-atomic-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-hc-ts-atomic-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-hc-ts-atomic-queue__include_dirs})
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-hc-ts-atomic-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-hc-ts-atomic-queue
-Wl,--start-group
  libscal
  prodcon-base
  hc-ts-atomic-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:fc#target
set(TARGET "fc")
set(TOOLSET "target")
set(fc__cxx_srcs "../../src/benchmark/std_glue/glue_fc_queue.cc")
add_library(fc STATIC ${fc__cxx_srcs})
set_target_properties(fc PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(fc PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(fc PROPERTIES PREFIX "lib")
set_target_properties(fc PROPERTIES ARCHIVE_OUTPUT_NAME "fc")
set_target_properties(fc PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libfc.a PROPERTIES GENERATED "TRUE")
list(APPEND fc__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET fc APPEND PROPERTY INCLUDE_DIRECTORIES ${fc__include_dirs})
set_target_properties(fc PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(fc PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(fc PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(fc PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(fc PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(fc PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-fc#target
set(TARGET "seqalt-fc")
set(TOOLSET "target")
set(seqalt-fc__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-fc__dummy_srcs}")
  file(WRITE "${seqalt-fc__dummy_srcs}" "")
endif()
add_executable(seqalt-fc ${seqalt-fc__dummy_srcs})
set_target_properties(seqalt-fc PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-fc PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-fc PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-fc PROPERTIES PREFIX "")
set_target_properties(seqalt-fc PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-fc")
set_target_properties(seqalt-fc PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-fc PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-fc__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-fc APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-fc__include_dirs})
set_target_properties(seqalt-fc PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-fc PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-fc PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-fc PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-fc PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-fc PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-fc
-Wl,--start-group
  libscal
  seqalt-base
  fc
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-fc#target
set(TARGET "prodcon-fc")
set(TOOLSET "target")
set(prodcon-fc__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-fc__dummy_srcs}")
  file(WRITE "${prodcon-fc__dummy_srcs}" "")
endif()
add_executable(prodcon-fc ${prodcon-fc__dummy_srcs})
set_target_properties(prodcon-fc PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-fc PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-fc PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-fc PROPERTIES PREFIX "")
set_target_properties(prodcon-fc PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-fc")
set_target_properties(prodcon-fc PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-fc PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-fc__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-fc APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-fc__include_dirs})
set_target_properties(prodcon-fc PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-fc PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-fc PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-fc PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-fc PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-fc PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-fc
-Wl,--start-group
  libscal
  prodcon-base
  fc
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:eb-stack#target
set(TARGET "eb-stack")
set(TOOLSET "target")
set(eb-stack__cxx_srcs "../../src/benchmark/std_glue/glue_eb_stack.cc")
add_library(eb-stack STATIC ${eb-stack__cxx_srcs})
set_target_properties(eb-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(eb-stack PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(eb-stack PROPERTIES PREFIX "lib")
set_target_properties(eb-stack PROPERTIES ARCHIVE_OUTPUT_NAME "eb-stack")
set_target_properties(eb-stack PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libeb-stack.a PROPERTIES GENERATED "TRUE")
list(APPEND eb-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET eb-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${eb-stack__include_dirs})
set_target_properties(eb-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(eb-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(eb-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(eb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(eb-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(eb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-eb-stack#target
set(TARGET "seqalt-eb-stack")
set(TOOLSET "target")
set(seqalt-eb-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-eb-stack__dummy_srcs}")
  file(WRITE "${seqalt-eb-stack__dummy_srcs}" "")
endif()
add_executable(seqalt-eb-stack ${seqalt-eb-stack__dummy_srcs})
set_target_properties(seqalt-eb-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-eb-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-eb-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-eb-stack PROPERTIES PREFIX "")
set_target_properties(seqalt-eb-stack PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-eb-stack")
set_target_properties(seqalt-eb-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-eb-stack PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-eb-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-eb-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-eb-stack__include_dirs})
set_target_properties(seqalt-eb-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-eb-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-eb-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-eb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-eb-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-eb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-eb-stack
-Wl,--start-group
  libscal
  seqalt-base
  eb-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-eb-stack#target
set(TARGET "prodcon-eb-stack")
set(TOOLSET "target")
set(prodcon-eb-stack__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-eb-stack__dummy_srcs}")
  file(WRITE "${prodcon-eb-stack__dummy_srcs}" "")
endif()
add_executable(prodcon-eb-stack ${prodcon-eb-stack__dummy_srcs})
set_target_properties(prodcon-eb-stack PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-eb-stack PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-eb-stack PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-eb-stack PROPERTIES PREFIX "")
set_target_properties(prodcon-eb-stack PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-eb-stack")
set_target_properties(prodcon-eb-stack PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-eb-stack PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-eb-stack__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-eb-stack APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-eb-stack__include_dirs})
set_target_properties(prodcon-eb-stack PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-eb-stack PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-eb-stack PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-eb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-eb-stack PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-eb-stack PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-eb-stack
-Wl,--start-group
  libscal
  prodcon-base
  eb-stack
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:dds-partrr-treiber#target
set(TARGET "dds-partrr-treiber")
set(TOOLSET "target")
set(dds-partrr-treiber__cxx_srcs "../../src/benchmark/std_glue/glue_dds_partrr_treiber.cc")
add_library(dds-partrr-treiber STATIC ${dds-partrr-treiber__cxx_srcs})
set_target_properties(dds-partrr-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(dds-partrr-treiber PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(dds-partrr-treiber PROPERTIES PREFIX "lib")
set_target_properties(dds-partrr-treiber PROPERTIES ARCHIVE_OUTPUT_NAME "dds-partrr-treiber")
set_target_properties(dds-partrr-treiber PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libdds-partrr-treiber.a PROPERTIES GENERATED "TRUE")
list(APPEND dds-partrr-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET dds-partrr-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${dds-partrr-treiber__include_dirs})
set_target_properties(dds-partrr-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(dds-partrr-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(dds-partrr-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(dds-partrr-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(dds-partrr-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(dds-partrr-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-dds-partrr-treiber#target
set(TARGET "seqalt-dds-partrr-treiber")
set(TOOLSET "target")
set(seqalt-dds-partrr-treiber__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-dds-partrr-treiber__dummy_srcs}")
  file(WRITE "${seqalt-dds-partrr-treiber__dummy_srcs}" "")
endif()
add_executable(seqalt-dds-partrr-treiber ${seqalt-dds-partrr-treiber__dummy_srcs})
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES PREFIX "")
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-dds-partrr-treiber")
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-dds-partrr-treiber PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-dds-partrr-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-dds-partrr-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-dds-partrr-treiber__include_dirs})
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-dds-partrr-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-dds-partrr-treiber
-Wl,--start-group
  libscal
  seqalt-base
  dds-partrr-treiber
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-dds-partrr-treiber#target
set(TARGET "prodcon-dds-partrr-treiber")
set(TOOLSET "target")
set(prodcon-dds-partrr-treiber__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-dds-partrr-treiber__dummy_srcs}")
  file(WRITE "${prodcon-dds-partrr-treiber__dummy_srcs}" "")
endif()
add_executable(prodcon-dds-partrr-treiber ${prodcon-dds-partrr-treiber__dummy_srcs})
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES PREFIX "")
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-dds-partrr-treiber")
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-dds-partrr-treiber PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-dds-partrr-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-dds-partrr-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-dds-partrr-treiber__include_dirs})
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-dds-partrr-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-dds-partrr-treiber
-Wl,--start-group
  libscal
  prodcon-base
  dds-partrr-treiber
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:dds-partrr-ms#target
set(TARGET "dds-partrr-ms")
set(TOOLSET "target")
set(dds-partrr-ms__cxx_srcs "../../src/benchmark/std_glue/glue_dds_partrr_ms.cc")
add_library(dds-partrr-ms STATIC ${dds-partrr-ms__cxx_srcs})
set_target_properties(dds-partrr-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(dds-partrr-ms PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(dds-partrr-ms PROPERTIES PREFIX "lib")
set_target_properties(dds-partrr-ms PROPERTIES ARCHIVE_OUTPUT_NAME "dds-partrr-ms")
set_target_properties(dds-partrr-ms PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libdds-partrr-ms.a PROPERTIES GENERATED "TRUE")
list(APPEND dds-partrr-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET dds-partrr-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${dds-partrr-ms__include_dirs})
set_target_properties(dds-partrr-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(dds-partrr-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(dds-partrr-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(dds-partrr-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(dds-partrr-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(dds-partrr-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-dds-partrr-ms#target
set(TARGET "seqalt-dds-partrr-ms")
set(TOOLSET "target")
set(seqalt-dds-partrr-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-dds-partrr-ms__dummy_srcs}")
  file(WRITE "${seqalt-dds-partrr-ms__dummy_srcs}" "")
endif()
add_executable(seqalt-dds-partrr-ms ${seqalt-dds-partrr-ms__dummy_srcs})
set_target_properties(seqalt-dds-partrr-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-dds-partrr-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-dds-partrr-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-dds-partrr-ms PROPERTIES PREFIX "")
set_target_properties(seqalt-dds-partrr-ms PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-dds-partrr-ms")
set_target_properties(seqalt-dds-partrr-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-dds-partrr-ms PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-dds-partrr-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-dds-partrr-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-dds-partrr-ms__include_dirs})
set_target_properties(seqalt-dds-partrr-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-dds-partrr-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-dds-partrr-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-dds-partrr-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-dds-partrr-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-dds-partrr-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-dds-partrr-ms
-Wl,--start-group
  libscal
  seqalt-base
  dds-partrr-ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-dds-partrr-ms#target
set(TARGET "prodcon-dds-partrr-ms")
set(TOOLSET "target")
set(prodcon-dds-partrr-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-dds-partrr-ms__dummy_srcs}")
  file(WRITE "${prodcon-dds-partrr-ms__dummy_srcs}" "")
endif()
add_executable(prodcon-dds-partrr-ms ${prodcon-dds-partrr-ms__dummy_srcs})
set_target_properties(prodcon-dds-partrr-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-dds-partrr-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-dds-partrr-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-dds-partrr-ms PROPERTIES PREFIX "")
set_target_properties(prodcon-dds-partrr-ms PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-dds-partrr-ms")
set_target_properties(prodcon-dds-partrr-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-dds-partrr-ms PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-dds-partrr-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-dds-partrr-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-dds-partrr-ms__include_dirs})
set_target_properties(prodcon-dds-partrr-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-dds-partrr-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-dds-partrr-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-dds-partrr-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-dds-partrr-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-dds-partrr-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-dds-partrr-ms
-Wl,--start-group
  libscal
  prodcon-base
  dds-partrr-ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:dds-1random-treiber#target
set(TARGET "dds-1random-treiber")
set(TOOLSET "target")
set(dds-1random-treiber__cxx_srcs "../../src/benchmark/std_glue/glue_dds_1random_treiber.cc")
add_library(dds-1random-treiber STATIC ${dds-1random-treiber__cxx_srcs})
set_target_properties(dds-1random-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(dds-1random-treiber PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(dds-1random-treiber PROPERTIES PREFIX "lib")
set_target_properties(dds-1random-treiber PROPERTIES ARCHIVE_OUTPUT_NAME "dds-1random-treiber")
set_target_properties(dds-1random-treiber PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libdds-1random-treiber.a PROPERTIES GENERATED "TRUE")
list(APPEND dds-1random-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET dds-1random-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${dds-1random-treiber__include_dirs})
set_target_properties(dds-1random-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(dds-1random-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(dds-1random-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(dds-1random-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(dds-1random-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(dds-1random-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-dds-1random-treiber#target
set(TARGET "seqalt-dds-1random-treiber")
set(TOOLSET "target")
set(seqalt-dds-1random-treiber__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-dds-1random-treiber__dummy_srcs}")
  file(WRITE "${seqalt-dds-1random-treiber__dummy_srcs}" "")
endif()
add_executable(seqalt-dds-1random-treiber ${seqalt-dds-1random-treiber__dummy_srcs})
set_target_properties(seqalt-dds-1random-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-dds-1random-treiber PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-dds-1random-treiber PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-dds-1random-treiber PROPERTIES PREFIX "")
set_target_properties(seqalt-dds-1random-treiber PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-dds-1random-treiber")
set_target_properties(seqalt-dds-1random-treiber PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-dds-1random-treiber PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-dds-1random-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-dds-1random-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-dds-1random-treiber__include_dirs})
set_target_properties(seqalt-dds-1random-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-dds-1random-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-dds-1random-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-dds-1random-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-dds-1random-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-dds-1random-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-dds-1random-treiber
-Wl,--start-group
  libscal
  seqalt-base
  dds-1random-treiber
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-dds-1random-treiber#target
set(TARGET "prodcon-dds-1random-treiber")
set(TOOLSET "target")
set(prodcon-dds-1random-treiber__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-dds-1random-treiber__dummy_srcs}")
  file(WRITE "${prodcon-dds-1random-treiber__dummy_srcs}" "")
endif()
add_executable(prodcon-dds-1random-treiber ${prodcon-dds-1random-treiber__dummy_srcs})
set_target_properties(prodcon-dds-1random-treiber PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-dds-1random-treiber PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-dds-1random-treiber PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-dds-1random-treiber PROPERTIES PREFIX "")
set_target_properties(prodcon-dds-1random-treiber PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-dds-1random-treiber")
set_target_properties(prodcon-dds-1random-treiber PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-dds-1random-treiber PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-dds-1random-treiber__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-dds-1random-treiber APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-dds-1random-treiber__include_dirs})
set_target_properties(prodcon-dds-1random-treiber PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-dds-1random-treiber PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-dds-1random-treiber PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-dds-1random-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-dds-1random-treiber PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-dds-1random-treiber PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-dds-1random-treiber
-Wl,--start-group
  libscal
  prodcon-base
  dds-1random-treiber
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:dds-1random-ms#target
set(TARGET "dds-1random-ms")
set(TOOLSET "target")
set(dds-1random-ms__cxx_srcs "../../src/benchmark/std_glue/glue_dds_1random_ms.cc")
add_library(dds-1random-ms STATIC ${dds-1random-ms__cxx_srcs})
set_target_properties(dds-1random-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(dds-1random-ms PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(dds-1random-ms PROPERTIES PREFIX "lib")
set_target_properties(dds-1random-ms PROPERTIES ARCHIVE_OUTPUT_NAME "dds-1random-ms")
set_target_properties(dds-1random-ms PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libdds-1random-ms.a PROPERTIES GENERATED "TRUE")
list(APPEND dds-1random-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET dds-1random-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${dds-1random-ms__include_dirs})
set_target_properties(dds-1random-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(dds-1random-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(dds-1random-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(dds-1random-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(dds-1random-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(dds-1random-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-dds-1random-ms#target
set(TARGET "seqalt-dds-1random-ms")
set(TOOLSET "target")
set(seqalt-dds-1random-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-dds-1random-ms__dummy_srcs}")
  file(WRITE "${seqalt-dds-1random-ms__dummy_srcs}" "")
endif()
add_executable(seqalt-dds-1random-ms ${seqalt-dds-1random-ms__dummy_srcs})
set_target_properties(seqalt-dds-1random-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-dds-1random-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-dds-1random-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-dds-1random-ms PROPERTIES PREFIX "")
set_target_properties(seqalt-dds-1random-ms PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-dds-1random-ms")
set_target_properties(seqalt-dds-1random-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-dds-1random-ms PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-dds-1random-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-dds-1random-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-dds-1random-ms__include_dirs})
set_target_properties(seqalt-dds-1random-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-dds-1random-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-dds-1random-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-dds-1random-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-dds-1random-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-dds-1random-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-dds-1random-ms
-Wl,--start-group
  libscal
  seqalt-base
  dds-1random-ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-dds-1random-ms#target
set(TARGET "prodcon-dds-1random-ms")
set(TOOLSET "target")
set(prodcon-dds-1random-ms__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-dds-1random-ms__dummy_srcs}")
  file(WRITE "${prodcon-dds-1random-ms__dummy_srcs}" "")
endif()
add_executable(prodcon-dds-1random-ms ${prodcon-dds-1random-ms__dummy_srcs})
set_target_properties(prodcon-dds-1random-ms PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-dds-1random-ms PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-dds-1random-ms PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-dds-1random-ms PROPERTIES PREFIX "")
set_target_properties(prodcon-dds-1random-ms PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-dds-1random-ms")
set_target_properties(prodcon-dds-1random-ms PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-dds-1random-ms PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-dds-1random-ms__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-dds-1random-ms APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-dds-1random-ms__include_dirs})
set_target_properties(prodcon-dds-1random-ms PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-dds-1random-ms PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-dds-1random-ms PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-dds-1random-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-dds-1random-ms PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-dds-1random-ms PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-dds-1random-ms
-Wl,--start-group
  libscal
  prodcon-base
  dds-1random-ms
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:cts-queue#target
set(TARGET "cts-queue")
set(TOOLSET "target")
set(cts-queue__cxx_srcs "../../src/benchmark/std_glue/glue_cts_queue.cc")
add_library(cts-queue STATIC ${cts-queue__cxx_srcs})
set_target_properties(cts-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(cts-queue PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(cts-queue PROPERTIES PREFIX "lib")
set_target_properties(cts-queue PROPERTIES ARCHIVE_OUTPUT_NAME "cts-queue")
set_target_properties(cts-queue PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libcts-queue.a PROPERTIES GENERATED "TRUE")
list(APPEND cts-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET cts-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${cts-queue__include_dirs})
set_target_properties(cts-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(cts-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(cts-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(cts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(cts-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(cts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-cts-queue#target
set(TARGET "seqalt-cts-queue")
set(TOOLSET "target")
set(seqalt-cts-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-cts-queue__dummy_srcs}")
  file(WRITE "${seqalt-cts-queue__dummy_srcs}" "")
endif()
add_executable(seqalt-cts-queue ${seqalt-cts-queue__dummy_srcs})
set_target_properties(seqalt-cts-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-cts-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-cts-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-cts-queue PROPERTIES PREFIX "")
set_target_properties(seqalt-cts-queue PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-cts-queue")
set_target_properties(seqalt-cts-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-cts-queue PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-cts-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-cts-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-cts-queue__include_dirs})
set_target_properties(seqalt-cts-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-cts-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-cts-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-cts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-cts-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-cts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-cts-queue
-Wl,--start-group
  libscal
  seqalt-base
  cts-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-cts-queue#target
set(TARGET "prodcon-cts-queue")
set(TOOLSET "target")
set(prodcon-cts-queue__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-cts-queue__dummy_srcs}")
  file(WRITE "${prodcon-cts-queue__dummy_srcs}" "")
endif()
add_executable(prodcon-cts-queue ${prodcon-cts-queue__dummy_srcs})
set_target_properties(prodcon-cts-queue PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-cts-queue PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-cts-queue PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-cts-queue PROPERTIES PREFIX "")
set_target_properties(prodcon-cts-queue PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-cts-queue")
set_target_properties(prodcon-cts-queue PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-cts-queue PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-cts-queue__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-cts-queue APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-cts-queue__include_dirs})
set_target_properties(prodcon-cts-queue PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-cts-queue PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-cts-queue PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-cts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-cts-queue PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-cts-queue PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-cts-queue
-Wl,--start-group
  libscal
  prodcon-base
  cts-queue
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#glue.gyp:bs-kfifo#target
set(TARGET "bs-kfifo")
set(TOOLSET "target")
set(bs-kfifo__cxx_srcs "../../src/benchmark/std_glue/glue_bskfifo.cc")
add_library(bs-kfifo STATIC ${bs-kfifo__cxx_srcs})
set_target_properties(bs-kfifo PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(bs-kfifo PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "${obj}.${TOOLSET}/")
set_target_properties(bs-kfifo PROPERTIES PREFIX "lib")
set_target_properties(bs-kfifo PROPERTIES ARCHIVE_OUTPUT_NAME "bs-kfifo")
set_target_properties(bs-kfifo PROPERTIES SUFFIX ".a")
set_source_files_properties(${obj}.${TOOLSET}/libbs-kfifo.a PROPERTIES GENERATED "TRUE")
list(APPEND bs-kfifo__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET bs-kfifo APPEND PROPERTY INCLUDE_DIRECTORIES ${bs-kfifo__include_dirs})
set_target_properties(bs-kfifo PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(bs-kfifo PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 -std=c++11 -fno-rtti ")
set_target_properties(bs-kfifo PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(bs-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(bs-kfifo PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(bs-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
unset(TOOLSET)
unset(TARGET)

#scal.gyp:seqalt-bs-kfifo#target
set(TARGET "seqalt-bs-kfifo")
set(TOOLSET "target")
set(seqalt-bs-kfifo__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${seqalt-bs-kfifo__dummy_srcs}")
  file(WRITE "${seqalt-bs-kfifo__dummy_srcs}" "")
endif()
add_executable(seqalt-bs-kfifo ${seqalt-bs-kfifo__dummy_srcs})
set_target_properties(seqalt-bs-kfifo PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(seqalt-bs-kfifo PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(seqalt-bs-kfifo PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(seqalt-bs-kfifo PROPERTIES PREFIX "")
set_target_properties(seqalt-bs-kfifo PROPERTIES RUNTIME_OUTPUT_NAME "seqalt-bs-kfifo")
set_target_properties(seqalt-bs-kfifo PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/seqalt-bs-kfifo PROPERTIES GENERATED "TRUE")
list(APPEND seqalt-bs-kfifo__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET seqalt-bs-kfifo APPEND PROPERTY INCLUDE_DIRECTORIES ${seqalt-bs-kfifo__include_dirs})
set_target_properties(seqalt-bs-kfifo PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(seqalt-bs-kfifo PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(seqalt-bs-kfifo PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(seqalt-bs-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(seqalt-bs-kfifo PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(seqalt-bs-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(seqalt-bs-kfifo
-Wl,--start-group
  libscal
  prodcon-base
  bs-kfifo
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)

#scal.gyp:prodcon-bs-kfifo#target
set(TARGET "prodcon-bs-kfifo")
set(TOOLSET "target")
set(prodcon-bs-kfifo__dummy_srcs "${obj}.${TOOLSET}/${TARGET}/genc/dummy.c")
if(NOT EXISTS "${prodcon-bs-kfifo__dummy_srcs}")
  file(WRITE "${prodcon-bs-kfifo__dummy_srcs}" "")
endif()
add_executable(prodcon-bs-kfifo ${prodcon-bs-kfifo__dummy_srcs})
set_target_properties(prodcon-bs-kfifo PROPERTIES EXCLUDE_FROM_ALL "FALSE")
set_target_properties(prodcon-bs-kfifo PROPERTIES LINKER_LANGUAGE "C")
set_target_properties(prodcon-bs-kfifo PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${builddir}")
set_target_properties(prodcon-bs-kfifo PROPERTIES PREFIX "")
set_target_properties(prodcon-bs-kfifo PROPERTIES RUNTIME_OUTPUT_NAME "prodcon-bs-kfifo")
set_target_properties(prodcon-bs-kfifo PROPERTIES SUFFIX "")
set_source_files_properties(${builddir}/prodcon-bs-kfifo PROPERTIES GENERATED "TRUE")
list(APPEND prodcon-bs-kfifo__include_dirs
  "${CMAKE_CURRENT_LIST_DIR}/../.."
  "${CMAKE_CURRENT_LIST_DIR}/../../src"
  "/usr/include"
  "/usr/local/include")
set_property(TARGET prodcon-bs-kfifo APPEND PROPERTY INCLUDE_DIRECTORIES ${prodcon-bs-kfifo__include_dirs})
set_target_properties(prodcon-bs-kfifo PROPERTIES COMPILE_DEFINITIONS "__STDC_FORMAT_MACROS=1;")
set_target_properties(prodcon-bs-kfifo PROPERTIES COMPILE_FLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -O3 ")
set_target_properties(prodcon-bs-kfifo PROPERTIES LINK_FLAGS "-Wl,--as-needed ")
set_target_properties(prodcon-bs-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_CFLAGS "-Wall -Werror -ftls-model=initial-exec -m64 -mcx16 -mtune=native -ffast-math -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free -fno-omit-frame-pointer -fno-exceptions -fPIC -g -O3 ")
set_target_properties(prodcon-bs-kfifo PROPERTIES XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
set_target_properties(prodcon-bs-kfifo PROPERTIES XCODE_ATTRIBUTE_OTHER_LDFLAGS "-Wl,--as-needed ")
target_link_libraries(prodcon-bs-kfifo
-Wl,--start-group
  libscal
  prodcon-base
  bs-kfifo
-Wl,--end-group
  "-lpthread"
  "-lgflags"
)
unset(TOOLSET)
unset(TARGET)
