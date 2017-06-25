Publication:
Our work on join sampling has been published at SSDBM 17! and can be found at https://arxiv.org/abs/1601.05118

Code: 
author = "Niranjan Kamat (kamatn@cse.osu.edu)"
copyright = "Copyright (C) 2014 The Ohio State University"
license = "BSD 3-Clause"
version = 0.1

This is a python implementation of StratJoin_Overall from the paper "Stratified Sampling from Both Sides of the Join". 

final_algo in src/join.py is the implementation of StratJoin_Overall including sampling and join with its unit test being test_final_algo test/test_join.py.

sample method in src/sample.py contains the sampling step.

Other methods / modules are straight-forward can be read through these two methods when needed.
