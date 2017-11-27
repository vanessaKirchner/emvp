#! python
import csv
import matplotlib.pyplot as plt


# ------- Exercise 2.2

# Remove invalid data points
def remove_invalid(data):

    erased = []

    for x in range(2, len(data)):
        if (data[x][5] != '0') and (data[x][10] != '0'):
            erased.append(data[x])

    return erased


# Plot points on image
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


def plot_idt_fixations(image_name, data):
    image = plt.imread(image_name)
    implot = plt.imshow(image)

    for x in range(0, len(data)):
        # left eye
        plt.scatter([data[x][0]], [data[x][1]], s=20, c='g')

    plt.savefig('idt-overlay.jpg')
    plt.show()
# ------- Exercise 3 I-DT


def idt(data, dispersion_threshold, duration_threshold):
    fixations = []
    counter = 0
    # while there are still some points
    while data:
        idx = 0
        window = []
        duration = 0
        # initialize window over first points to cover the duration threshold
        while duration < duration_threshold:
            window.append(data[idx])
            if idx == 0:
                duration = 0
            else:
                duration = duration + (int(window[idx][0]) - int(window[idx - 1][0]))
            idx = idx + 1
            counter = counter + 1

        # calculate dispersion
        left_x = []
        left_y = []
        for point in range(0, len(window)):
            left_x.append(float(window[point][1]))
            left_y.append(float(window[point][2]))

        max_x_l = max(left_x)
        max_y_l = max(left_y)
        min_x_l = min(left_x)
        min_y_l = min(left_y)
        dispersion = (max_x_l - min_x_l) + (max_y_l - min_y_l)

        # if dispersion of window points <= threshold
        if dispersion <= dispersion_threshold:
            # add additional points to the window until dispersion > threshold
            while dispersion <= dispersion_threshold:
                window.append(data[idx])
                idx = idx + 1
                counter = counter + 1

                # calculate new dispersion
                left_x = []
                left_y = []
                for point in range(0, len(window)):
                    left_x.append(float(window[point][1]))
                    left_y.append(float(window[point][2]))

                max_x_l = max(left_x)
                max_y_l = max(left_y)
                min_x_l = min(left_x)
                min_y_l = min(left_y)
                dispersion = (max_x_l - min_x_l) + (max_y_l - min_y_l)

            # note a fixation at the centoid of the window points
            avg_x_l = 0
            avg_y_l = 0
            for point in range(0, len(window)):
                avg_x_l = avg_x_l + left_x[point]
                avg_y_l = avg_y_l + left_y[point]

            avg_x_l = avg_x_l / len(window)
            avg_y_l = avg_y_l / len(window)
            centroid = [avg_x_l, avg_y_l]
            fixations.append(centroid)
            # remove winow points from data points
            data_temp = []
            for row in range(counter, len(data)):
                data_temp.append(data[row])
            data = data_temp
        else:
            # remove first point from data points
            data_temp = []
            for row in range(1, len(data)):
                data_temp.append(data[row])
            data = data_temp

    # return fixations
    print("I-DT finished")
    print("Amount of fixations found: " + str(len(fixations)))
    return fixations


def main():
    # Test Python version
    # sys.stdout.write("hello from Python %s\n" % (sys.version,))

    # ---------- Exercise 2.1

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

    # Exercise 3 - IDT
    dispersion_threshold = 500
    duration_threshold = 150000

    fixations_idt = idt(erased, dispersion_threshold, duration_threshold)
    plot_idt_fixations(image_name, fixations_idt)


if __name__ == "__main__":
    main()
