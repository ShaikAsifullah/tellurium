{% import 'macros_helpers.py' as helpers %}
"""
    tellurium {{ version }}

    auto-generated code ({{ timestamp }})
        sedmlDoc: L{{ doc.getLevel() }}V{{ doc.getVersion() }} {% if doc.isSetId() %}id={{ doc.getId() }} {% endif %} {% if doc.isSetName() %}name={{ doc.getName() }}{% endif %}
        workingDir: {{ factory.workingDir }}
        inputType: {{ factory.inputType }}

"""
from __future__ import print_function, division
import tellurium as te
import numpy as np
import matplotlib.pyplot as plt
import libsedml
import os.path

workingDir = '{{ factory.workingDir }}'

{{ helpers.heading(doc.getListOfModels(), 'Model') }}
{% for m in doc.getListOfModels() %}
# Model <{{ m.getId() }}>
{% for change in model_changes.get(m.getId()) %}
#   Change: {{ change }}
{% endfor %}
{% if m|SEDML_isSBMLModel %}
{{ m.getId() }} = te.loadSBMLModel(os.path.join(workingDir, '{{ model_sources.get(m.getId()) }}'))
{% endif %}
{% if m|SEDML_isCellMLModel %}
{{ m.getId() }} = te.loadCellMLModel(os.path.join(workingDir, '{{ model_sources.get(m.getId()) }}'))
{% endif %}
{% for change in model_changes.get(m.getId()) %}
{{ modelChangeToPython(m, change) }}
{% endfor %}
{% endfor %}

{{ helpers.heading(doc.getListOfTasks(), 'Task') }}
{% for task in doc.getListOfTasks() %}
# Task <{{ task.getId() }}>
{{ taskToPython(factory.doc, task) }}

{% endfor %}

{{ helpers.heading(doc.getListOfDataGenerators(), 'DataGenerator') }}
{% for dg in doc.getListOfDataGenerators() %}
# DataGenerator <{{ dg.getId() }}>
{% endfor %}

{{ helpers.heading(doc.getListOfOutputs(), 'Output') }}
{% for out in doc.getListOfOutputs() %}
# Output <{{ out.getId() }}>
{% endfor %}