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


# ------- Exercise 3 I-DT

def idt(data, dispersion_threshold, duration_threshold):
    dispersion_threshold = 100
    duration_threshold = 6666061580  # TODO: welcher Wert

    fixations = []

    # TODO: while there are still points

    # initialize window over first points to cover the duration threshold
    duration = 0
    idx = 0;
    window = []
    while (duration < duration_threshold):
        window.append(data[idx])
        duration = duration + int(window[idx][0])

        # if dispersion of window points <= threshold
        dispersion = 0 #TODO calculate Dispersion. Noch falsch
        if (dispersion <= dispersion_threshold):

            # add additional points to the window until dispersion > threshold
            window.append(data[idx])
            idx = idx + 1
            # TODO: Update dispersion: Formel vom Blatt: Was ist x und y?

        # Note a fixation at the centroid of the window points

        # remove window points from points

            # del data[idx] Remove point
            # idx = idx + 1

        # Else: remove first point from points
    # TODO

    print(window)

    # return fixations
    print("I-DT finished")
    return fixations


def main():
    # Test Python version
    # sys.stdout.write("hello from Python %s\n" % (sys.version,))

    ############ Exercise 2.1

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

    # Exercise 3 - IDT
    dispersion_threshold = 100
    duration_threshold = 100  # TODO: welcher Wert

    fixations_idt = idt(erased, dispersion_threshold, duration_threshold)


if __name__ == "__main__": main()
