"""
IPython parameter slider.

see example notebook: `tellurium/examples/notebooks/parameter_slider.ipynb`
"""
from __future__ import print_function, division
import sys
import ipywidgets
import warnings
import tellurium as te
from roadrunner import SelectionRecord


def simulateAndPlot(r, *args, **kwargs):
    """ Simulate with r.simulate with given arguments and plot with tellurium.

    :returns: simulation result
    :rtype: NamedArray
    """
    result = r.simulate(*args, **kwargs)
    te.plotWithLegend(r, result)
    return result


class ParameterSlider(object):
    """ Interactive ipython notebook slider. """

    def __init__(self, r,
                 paramIds=None,
                 minFactor=0,
                 maxFactor=2,
                 sliderStepFactor=10,
                 selection=None,
                 simulateAndPlot=simulateAndPlot):
        """ Create interactive sliders to change model parameters.
        ::

            %matplotlib inline
            import tellurium as te
            from tellurium.widgets import ParameterSlider

            model = '''
                  model pathway()
                    S1 -> S2; k1*S1 - k2*S2 # Reversible term added here

                    # Initialize values
                    S1 = 5; S2 = 0;
                    k1 = 0.1;  k2 = 0.05;

                  end
            '''
            r = te.loadAntimonyModel(model)
            ParameterSlider(r, paramIds=['k1'])

        :param r: roadrunner model
        :type r: roadrunner.RoadRunner
        :param paramIds: list of parameter ids to create sliders, by default creates slider for every parameter
        :type paramIds: list[str]
        :param minFactor: scale factor multiplied with parameter value, to determine minimum value of slider
        :type minFactor: float
        :param maxFactor: scale factor multiplied with parameter value, to determine maximum value of slider
        :type maxFactor: float
        :param sliderStepFactor: scale factor divided with parameter value, to determine step size of slider
        :type sliderStepFactor: float
        :param selection: roadrunner selection, if None r.selections is used
        :type selection: list[str]
        :param simulateAndPlot: simulateAndPlot function with signature f(r, *args, **kwargs)
        :type simulateAndPlot: function
        """

        if paramIds is None:
            paramIds = r.model.getGlobalParameterIds()
        if selection is not None:
            r.selections = selection

        kwargs = {}

        def runSimulation(start=0, stop=100, steps=100, **kwargs):
            """ Function run in interact. """
            # full model reset
            r.reset(SelectionRecord.ALL)
            # set parameters, key:value pairs
            for k, v in kwargs.items():
                try:
                    key = k.encode('ascii', 'ignore')
                    r[key] = v
                except RuntimeError:
                    # error in setting model variable, variable probably not in model
                    e = sys.exc_info()
                    warnings.warn(e)
            # simulate
            try:
                results = simulateAndPlot(r, start, stop, steps=steps)
            except:
                # error in simulation
                e = sys.exc_info()
                warnings.warn(e)

        # create FloatSlider for all parameters
        for pid in paramIds:
            val = r[pid]
            try:
                r[pid] = val
                kwargs[pid] = ipywidgets.FloatSlider(
                    min=minFactor*val,
                    max=maxFactor*val,
                    step=val/sliderStepFactor,
                    value=val)
            except:
                e = sys.exc_info()
                warnings.warn(e)

        # create the widget
        ipywidgets.interact(runSimulation,
                            start=ipywidgets.FloatText(min=0, value=0),
                            stop=ipywidgets.FloatText(min=0, value=100),
                            steps=ipywidgets.IntText(min=0, value=100),
                            **kwargs)