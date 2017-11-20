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
        plt.scatter([data[x][1]], [data[x][2]], c='b')

        # right eye
        plt.scatter([data[x][6]], [data[x][7]], c='r')

    plt.savefig('eyes-overlay.png')
    plt.show()


# ------- Exercise 3 I-DT

def idt(data, dispersion_threshold, duration_threshold):
    dispersion_threshold = 100
    duration_threshold = 100  # TODO: welcher Wert

    fixations = []

    # initialize window over first points to cover the duration threshold
    # TODO

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
    plot_points(image_name, datalist)

    # Exercise 3 - IDT
    dispersion_threshold = 100
    duration_threshold = 100  # TODO: welcher Wert

    fixations_idt = idt(erased, dispersion_threshold, duration_threshold)


if __name__ == "__main__": main()
