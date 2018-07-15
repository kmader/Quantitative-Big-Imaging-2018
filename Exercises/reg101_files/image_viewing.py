"""
this file contains the ugly code hacked together my overworked PhD students 
to hide boring visualisation boilerplate code from users and keep the course interesting
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def horizontal_pane(I_list, cmap=None):

    Z, axarr = plt.subplots(1, len(I_list))
    i = 0

    if isinstance(I_list, dict):
        for name, value in I_list.items():
            axarr[i].set_title(name)
            if isinstance(value, dict):
                I = value.get('image', None)
                cmap = value.get('cmap', None)
                if cmap:
                    axarr[i].imshow(I, plt.get_cmap(cmap))
                else:
                    axarr[i].imshow(I, plt.get_cmap('gray'))
            else:
                axarr[i].imshow(value, plt.get_cmap(cmap))
            i += 1
    else:
        for I in I_list:
            if cmap is None:
                cmap = 'gray'
            axarr[i].imshow(I, plt.get_cmap(cmap))
            i += 1

    plt.show()


def overlay_RGB(I_list):

    Z, axarr = plt.subplots(1, len(I_list)-1)
    for i in range(len(I_list)-1):
        overlay = numpy.zeros((I_list[i].shape) + (3,), dtype=float)
        overlay[:, :, 0] = I_list[i].astype(float)
        overlay[:, :, 1] = I_list[i+1].astype(float)
        overlay[:, :, 2] = I_list[i].astype(
            float)*0.5 + I_list[i+1].astype(float)*0.5
        if (len(I_list)-1) == 1:
            axarr.imshow(overlay/numpy.max(overlay))
        else:
            axarr[i].imshow(overlay/numpy.max(overlay))
    plt.show()


def overlay_RGB_cost(I_list, cost_history, cost_function, cfuncs, x, y, history=None):

    fig = plt.figure()
    for i in range(len(I_list)-1):
        overlay = numpy.zeros((I_list[i].shape) + (3,), dtype=float)
        overlay[:, :, 0] = I_list[i].astype(float)
        overlay[:, :, 1] = I_list[i+1].astype(float)
        overlay[:, :, 2] = I_list[i].astype(
            float)*0.5 + I_list[i+1].astype(float)*0.5
        ax = fig.add_subplot(1, len(I_list), i+1)
        ax.imshow(overlay/numpy.max(overlay))
        ax = fig.add_subplot(1, len(I_list), len(I_list), projection='3d')
        cf = 0
        cost_fun = {}
        cost_fun[cost_function] = cfuncs[cost_function]

        if isinstance(cost_fun, dict):

            for name, f in cost_fun.items():
                cf = f(I_list[0], I_list[1])
                cost_history[name].append(
                    (x, y, cf, numpy.prod(I_list[0].shape)))
                ch = numpy.array(cost_history[name])
                colour = ch[:, 2] - numpy.min(ch[:, 2])
                colour /= numpy.max(colour)
                if history is None:
                    for i in range(len(ch)-1):
                        ax.plot(ch[i:i+2, 0], ch[i:i+2, 1], ch[i:i+2, 2],
                                color=plt.cm.jet(0.5*(colour[i]+colour[i+1])))
                else:
                    for i in range(max(len(ch)-history, 0), len(ch)-1):
                        ax.plot(ch[i:i+2, 0], ch[i:i+2, 1], ch[i:i+2, 2],
                                color=plt.cm.jet(0.5*(colour[i]+colour[i+1])))
                ax.scatter(ch[-1, 0], ch[-1, 1], ch[-1, 2], s=100)
                l = [x for x in cost_fun]
                # ax.legend(l)
        else:

            cf = cost_fun(I_list[0], I_list[1])
            cost_history.append(
                (x, y, cost_fun(I_list[0], I_list[1]), numpy.prod(I_list[0].shape)))
            ch = numpy.array(cost_history)
            colour = ch[:, 2] - numpy.min(ch[:, 2])
            colour /= numpy.max(colour)
            for i in range(len(ch)-1):
                ax.plot(ch[i:i+2, 0], ch[i:i+2, 1], ch[i:i+2, 2],
                        color=plt.cm.jet(0.5*(colour[i]+colour[i+1])))
            ax.scatter(ch[-1, 0], ch[-1, 1], ch[-1, 2], s=100)
        ax.set_xlabel('X displacement (voxels)')
        ax.set_ylabel('Y displacement (voxels)')
        ax.set_zlabel('Cost (-)')
        t1 = cost_function+"\nCurrent Cost: " + "{0:.3f}".format(cf)
        if len(cost_history) > 2:
            t1 += "\n Gradient: " + \
                "{0:.3f}".format((cf-cost_history[cost_function][-2][2]))
        ax.set_title(t1)

    plt.show()


def normalise_to(I, percentage):
    I_new = (I/numpy.percentile(I, percentage))
    I_new[I_new > 1] = 1.0
    return I_new
