#! python
import sys
import csv
import numpy
import matplotlib.pyplot as plt
import math


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


# Plot detected fixations
def plot_fixations(image_name, data):
    image = plt.imread(image_name)
    implot = plt.imshow(image)

    for x in range(0, len(data)):
        # eye data
        plt.scatter([data[x][0]], [data[x][1]], s=20, c='r')

    plt.savefig('ivt.jpg')
    plt.show()


# ------- Exercise 3 I-VT

def ivt(data, velocity_threshold):
    print("IVT")
    fixations = []

    for point in range(0, len(data) - 1):

        # Calculate the point-to-point velocities for each point in the protocol
        time = float(data[point + 1][0]) - float(data[point][0])
        distance_x_l = float(data[point + 1][1]) - float(data[point][1])
        distance_y_l = float(data[point + 1][2]) - float(data[point][2])
        distance_l = math.sqrt(math.pow(distance_x_l, 2) + math.pow(distance_y_l, 2))

        velocity = distance_l / time

        # Label each point below velocity threshold as a fixation point, otherwise saccade
        if velocity < velocity_threshold:
            data[point].append('1')  # 1 is fixation, 0 is saccade
        else:
            data[point].append('0')

    data[len(data) - 1].append('0')  # last point is saccade, algorithm can use more points

    # Collapse consecutive fixation points into fixation groups, removing saccade points
    idx = 0  # group index
    for point in range(0, len(data) - 1):

        if data[point][3] == '0':

            if data[point + 1][3] == '1':
                idx = idx + 1

            continue

        data[point].append(idx)
        fixations.append(data[point])

    fixation_centroids = []

    # map each fixation group to a fixation at the centroid of its points
    for i in range(0, idx):  # for each group
        counter = 0
        avg_x = 0
        avg_y = 0

        # calculate centroid
        for point in range(0, len(fixations)):
            if fixations[point][4] == i:
                counter = counter + 1
                avg_x = avg_x + float(fixations[point][1])
                avg_y = avg_y + float(fixations[point][2])

        avg_x = avg_x / counter
        avg_y = avg_y / counter
        data = [avg_x, avg_y]

        fixation_centroids.append(data)

    # Return fixations
    print("IVT finished: " + str(idx) + " Groups detected")
    return fixation_centroids


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

    # Show data points on image
    image_name = 'stimuli.jpg'
    # plot_points(image_name, erased)

    # Exercise 3 - IVT
    velocity_threshold = 0.04  # threshold in microseconds

    left_eye = []
    for row in range(len(erased)):
        data_left = [erased[row][0], erased[row][1], erased[row][2]]
        left_eye.append(data_left)

    fixations_left = ivt(left_eye, velocity_threshold)

    plot_fixations(image_name, fixations_left)
    print("Groups left eye: " + str(len(fixations_left)))


if __name__ == "__main__":
    main()
