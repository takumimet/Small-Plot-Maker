from abc import ABCMeta
import matplotlib.pyplot as plt 


class _baseGraph(metaclass=ABCMeta):

    def __init__(self, root_tk, x, y):
        self._x = x
        self._y = y
        self._plotStyle = 'seaborn'
        self.__plot = plt.plot(x, y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        # TODO if isinstance(x,)
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y
    
    @property
    def _plot_style(self):
        return self._plotStyle

    @_plot_style.setter
    def _plot_style(self, new_color):
        if isinstance(new_color, str):
            self._plotStyle = new_color

    def _show_plot(self):
        plt.plot(self._x, self._y)
        plt.show()


if __name__ == '__main__':

    x = list(range(-10,11))
    y = [n**2 for n in x]
    test_plot = _baseGraph(x, y)
    test_plot._show_plot()
