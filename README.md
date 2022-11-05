### Ascon-p
In this repository are various secure masking designs for the Ascon-p permutation block. most designs were implemented in assembly, the rest were implemented in C.
all implementation were designed to work with a randomness cache buffer, to increase performance (or, to eliminate waiting time from pseudo random generator)
## Building & Runnung
setup.sh - perform required installations on the machine.
make (Makefile) - to build for x86 / x64 / armv7 / aarch64 processors, and run.
running arm requires emulations...

## Scripts
inside scripts, there are:
benchmark.py - benchmark cycles per bit, randomness usage, for both our generic masking and usuba.
codesize.py - calculate the codesize for every implemntation.
datapath.py - simulate the time required for each technology to copy a large buffer.
## License
This repository is licensed under AGPL-3.0 License
## Reference
Dor Salomon, Itamar Levi, "On the Performance Gap of an Generic C Optimized Assembler and Wide Vector Extensions for Masked Software with an Ascon-p test-case", Nov. 2021. [update this]
## About us
The implementations were designed by Dor Salomon as part of a research activity with the Secured Electronic Systems (Selecsys) LAB at Bar-Ilan University, under the supervision of Dr. Itamar Levi.

