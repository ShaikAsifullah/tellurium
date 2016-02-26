"""
    tellurium 1.3.1

    auto-generated code (2016-02-26T09:03:10)
        sedmlDoc: L1V1          workingDir: /home/mkoenig/git/tellurium/tellurium/tests/testdata/sedml/sed-ml
        inputType: SEDML_FILE

"""
from __future__ import print_function, division
import tellurium as te
import numpy as np
import matplotlib.pyplot as plt
import libsedml
import os.path

workingDir = '/home/mkoenig/git/tellurium/tellurium/tests/testdata/sedml/sed-ml'

# --------------------------------------------------------
# Models
# --------------------------------------------------------
#  - Application0 (Application0)

# Model <Application0>
Application0 = te.loadSBMLModel(os.path.join(workingDir, '../models/asedml3repeat.xml'))

# --------------------------------------------------------
# Tasks
# --------------------------------------------------------
#  - task_0_0 (task_0_0)
#  - repeatedTask_0_0 (repeatedTask_0_0)

# Task <task_0_0>
Application0.setIntegrator('cvode')
Application0.timeCourseSelections = []
task_0_0 = Application0.simulate(start=0.0, end=30.0, steps=1000)

# Task <repeatedTask_0_0>
__range = [10.0, 20.0, 30.0]
repeatedTask_0_0 = [None] * len(__range)
for k, value in enumerate(__range):
    Application0.reset()
    Application0['init([s1])'] = value
    Application0.setIntegrator('cvode')
    Application0.timeCourseSelections = []
    repeatedTask_0_0[k] = Application0.simulate(start=0.0, end=30.0, steps=1000)


# --------------------------------------------------------
# DataGenerators
# --------------------------------------------------------
#  - time_repeatedTask_0_0 (time_repeatedTask_0_0)
#  - dataGen_repeatedTask_0_0_s0 (dataGen_repeatedTask_0_0_s0)
#  - dataGen_repeatedTask_0_0_s1 (dataGen_repeatedTask_0_0_s1)

# DataGenerator <time_repeatedTask_0_0>
# DataGenerator <dataGen_repeatedTask_0_0_s0>
# DataGenerator <dataGen_repeatedTask_0_0_s1>

# --------------------------------------------------------
# Outputs
# --------------------------------------------------------
#  - plot2d_Simulation0 (Application0plots)

# Output <plot2d_Simulation0>