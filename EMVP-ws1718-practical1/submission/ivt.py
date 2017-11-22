#! python
import sys
import csv
import numpy
import matplotlib.pyplot as plt


# ------- Exercise 2.2

def remove_invalid(data):
    # Remove invalid data points

    erased = []

    for x in range(2, len(data)):

        if (data[x][5] != '0') and (data[x][10] != '0'):
            erased.append(data[x])

    return erased


def plot_points(image_name, data):
    image = plt.imread(image_name)
    implot = plt.imshow(image)

    for x in range(2, len(data)):
        # left eye
        plt.scatter([data[x][1]], [data[x][2]], s=1, c='b')

        # right eye
        plt.scatter([data[x][6]], [data[x][7]], s=1, c='r')

    plt.savefig('eyes-overlay.jpg')
    plt.show()


# ------- Exercise 3 I-VT

def ivt(data, velocity_threshold):
    fixation_threshold = 100  # TODO benutzen?
    saccade_threshold = 300  # TODO benutzen?

    fixations = []

    for point in range(0, len(data) - 1):

        # Calculate the point-to-point velocities for each point in the protocol
        velocity = float(data[point + 1][0]) - float(data[point][0])

        # Label each point below velocity threshold as a fixation point, otherwise saccade
        if velocity < velocity_threshold:
            data[point].append('1')  # 1 is fixation, 0 is saccade
        else:
            data[point].append('0')

    # Collapse consecutive fixation points into fixation groups, removing saccade points
    for point in range(0, len(data) - 1):
        if (data[point][11] != '0'):
            fixations.append(data[point])

    # map each fixation group to a fixation at the centroid of its points

    # TODO

    # Return fixations
    return fixations


def main():
    # ------- Exercise 2.1

    # Read data
    datalist = []

    # Read data and save to list
    with open('data.csv', 'rt', encoding='utf-8') as csvfile:
        data = csv.reader(csvfile, delimiter='\t', quotechar='|')
        datalist = list(data)

    # ------- Exercise 2.2

    # Remove invalid data points
    erased = remove_invalid(datalist)
    # TODO: Sind das wirklich alle die Invalid sind?

    # Show data points on image
    image_name = 'stimuli.jpg'
    plot_points(image_name, datalist)

    # Exercise 3 - IVT
    velocity_threshold = 8250  # TODO Macht das Sinn? Irgendwie kommen da nur so große abstände raus
    fixations_ivt = ivt(erased, velocity_threshold)


if __name__ == "__main__": main()
