Scal
====

The Scal framework provides implementantions and benchmarks for concurrent
objects.  The benchmarks show the trade-off between concurrent data structure
semantics and scalablity.

Homepage: http://scal.cs.uni-salzburg.at

Dependencies
------------

* pkg-config
* gflags
* g++ with support for template aliasing (>= 4.7)

Building
--------

This is as easy as

    ./configure
    make

See `./configure --help` for optional features, for instance compiling with
debugging symbols.

The format for the resulting binaries is `<benchmark>-<datastructure>`. Each
binary supports the `--help` paramter to show a list of supported configuration
flags.

Examples
--------

### Producer/consumer

The most common paramters are:
* consumers: Number of consuming threads
* producers: Number of producing threads
* c: The computational workload to do between two data structure operations
* operations: The number of put/enqueue operations the should be performed by a producer

The following runs the Michael-Scott queue in a producer/consumer benchmark:

    ./prodcon-ms -producers=15 -consumers=15 -operations=100000 -c=250

And the same for the bounded-size k-FIFO queue:

    ./prodcon-bskfifo -producers=15 -consumers=15 -operations=100000 -c=250

Try `./prodcon-bskfifo --help` to see the full list of available paramters.

License
-------

Copyright (c) 2012, the Scal project authors.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the 
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the 
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY 
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND 
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
