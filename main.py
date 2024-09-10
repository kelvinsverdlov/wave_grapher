import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
import numpy

pyplot.rcParams["figure.autolayout"] = True


# A general multipurpose wave generative class.
class WaveClass:

    def __init__(self, wave_type, wave_amplitude=1, wave_frequency=1):
        
        """
        :param wave_type: The type of the wave, Sine, Cosine, Tangent...
        :param wave_amplitude: The wave's maximum amplitude, defaulted to 1.
        :param wave_frequency: The wave's frequency, defaulted to 1.

        :type wave_type: str
        :type wave_amplitude: float or int
        :type wave_frequency: float or int
        """

        self.wave_type = wave_type
        self.wave_amplitude = wave_amplitude
        self.wave_frequency = wave_frequency

    @staticmethod
    def __safety_check_wave(wave_type, wave_amplitude, wave_frequency, error_code):

        allowed_types = (float, int)

        if wave_type == error_code:
            raise Exception("Wave type couldn't be found! Make sure it is in the python math library.")

        if not type(wave_amplitude) in allowed_types:
            raise Exception("Wave amplitude isn't a real number.")

        if not type(wave_frequency) in allowed_types:
            raise Exception("Wave frequency is not allowed!")


    def wave_function(self, variable):
        error_code = "Does not exist"
        wave_type = getattr(numpy, f"{self.wave_type}", error_code)
        self.__safety_check_wave(wave_type, self.wave_amplitude, self.wave_frequency, error_code)

        wave_function = self.wave_amplitude*wave_type(180 * 2 * self.wave_frequency * variable)

        return wave_function

    @staticmethod
    def set_value(graph_values, x_values, y_values, frame):
        graph_values.set_data(x_values[:frame], y_values[:frame])


    def graph_wave(self, lower_bound, max_bound, zoom_multiplicative=1):

        """
        Parameters are described in pi radians
        :param lower_bound: integer for lower_bound
        :param max_bound: integer for higher_bound
        :param zoom_multiplicative: multiply zoom
        :return:
        """

        x_values = numpy.arange(lower_bound * 180, max_bound * 180 + 1, 1)  # graph over 4pi
        y_values = self.wave_function(x_values)

        figure, axes = pyplot.subplots(1, 1)
        axes.set_xlim((lower_bound * 180, max_bound * 180))
        axes.set_ylim((-self.wave_amplitude * 1/zoom_multiplicative, self.wave_amplitude * 1/zoom_multiplicative))

        graph_values, = axes.plot([], [])
        animated_graph = animation.FuncAnimation(figure, lambda i: self.set_value(graph_values, x_values, y_values, i), frames=len(x_values), interval=1)
        pyplot.show()


wave_object = WaveClass("sin", 1, 0.0001)
wave_object.graph_wave(0, 4)
