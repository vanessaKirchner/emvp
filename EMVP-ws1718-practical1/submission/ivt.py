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
    print("IVT")
    fixations = []

    for point in range(0, len(data) - 1):

        # Calculate the point-to-point velocities for each point in the protocol
        velocity = float(data[point + 1][0]) - float(data[point][0])
        #TODO velocity richtig? Eventuell Gradzahl?


        # Label each point below velocity threshold as a fixation point, otherwise saccade
        if velocity < velocity_threshold:
            data[point].append('1')  # 1 is fixation, 0 is saccade
        else:
            data[point].append('0')

    data[len(data)-1].append('0') #last point is saccade, algorithm can use more points

    # Collapse consecutive fixation points into fixation groups, removing saccade points
    idx = 0 # group index
    for point in range(0, len(data) - 1):

        if (data[point][11] == '0'):

            if(data[point+1][11] == '1'):
                idx = idx + 1

            continue

        data[point].append(idx)
        fixations.append(data[point])


    # map each fixation group to a fixation at the centroid of its points
    for i in range(0, idx): # for each group
        counter = 0
        avg_lefteye_x = 0
        avg_righteye_x = 0
        avg_lefteye_y = 0
        avg_righteye_y = 0

        # calculate centroid
        for point in range(0,len(fixations)):
            if (fixations[point][12] == i):
                counter = counter + 1
                avg_lefteye_x = avg_lefteye_x + float(fixations[point][1])
                avg_lefteye_y = avg_lefteye_y + float(fixations[point][2])
                avg_righteye_x = avg_righteye_x + float(fixations[point][6])
                avg_righteye_y = avg_righteye_y + float(fixations[point][7])


        avg_lefteye_x = avg_lefteye_x / counter
        avg_lefteye_y = avg_lefteye_y / counter
        avg_righteye_x = avg_righteye_x / counter
        avg_righteye_y = avg_righteye_y / counter

        print("Group " + str(i) +  " Left: " + str(avg_lefteye_x) + " " + str(avg_lefteye_y) + " Right: " + str(avg_righteye_x) + " " + str(avg_righteye_y))



    # TODO welcher Punkt ist Fixation?

    # Return fixations
    print("IVT finished: " + str(idx) + " Groups detected")
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
    #plot_points(image_name, erased)

    # Exercise 3 - IVT
    velocity_threshold = 200000  # threshold in microseconds
    fixations_ivt = ivt(erased, velocity_threshold)

    print(fixations_ivt[0:10])


if __name__ == "__main__": main()
