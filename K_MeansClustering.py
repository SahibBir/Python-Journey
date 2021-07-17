"""
Submitted By: Sahib Bir Singh Bhatia
Student ID:201547831
COMP 517 - Assignment 2 - 2020-21 - JAN21 - CA Assignment 2 - CLUSTERING ALGORITHM
"""


def distCalc(c, points):
    # Function to calculate the distance between centroid c and data-points. Points is a list of data-points.
    distance_from_c = {}  # Initialising a dictionary
    for i in range(len(points)):
        dist_c = ((points[i][0] - c[0]) ** 2) + ((points[i][1] - c[1]) ** 2)
        distance_from_c["{0} point".format(i + 1)] = round((dist_c ** 0.5), 3)  # Adding distance of points to dict
    return distance_from_c


def cluster(dict1, dict2):
    # Function to sort data-points into clusters depending upon their distance from centroids C1 and C2
    cl_c1 = []  # Initialising a list for centroid c1
    cl_c2 = []  # Initialising a list for centroid c2
    for k in range(len(dict1)):
        if dict1['{0} point'.format(k + 1)] < dict2['{0} point'.format(k + 1)]:
            cl_c1.append(data_points[k])  # Adding data-point into C1 if its closer to C1
        else:
            cl_c2.append(data_points[k])  # Adding data-point into C2 if its closer to C2
    return cl_c1, cl_c2


def clusterMean(cl):
    # Function to calculate the new centroid for further iterations
    mean_list_x = []  # Initialising a list for x co-ordinates of cluster list
    mean_list_y = []  # Initialising a list for y co-ordinates of cluster list

    for m in range(len(cl)):
        mean_list_x.append(cl[m][0])
        mean_list_y.append(cl[m][1])

    avg_x = sum(mean_list_x) / len(mean_list_x)
    avg_y = sum(mean_list_y) / len(mean_list_y)
    centroid = (avg_x, avg_y)
    return centroid


def checkCentroid(li):
    # Function to check whether the centroid remains same after further iterations
    if li[0] == li[1]:
        return True
    else:
        return False


data_points = [(0, 0), (1, 0), (1, 1), (0, 1), (-1, 0)]  # Input data-points
c1 = (1, 0)  # Centroid C1
c2 = (1, 1)  # Centroid C2
li_c1 = []   # Initialising a list for values of centroid c1
li_c2 = []   # Initialising a list for values of centroid c2
x = 0

print("Data points:", data_points)
print("Centroid c1: {0}\nCentroid c2: {1}\n{2}".format(c1, c2, "*" * 150))

while x < 2:
    dist_li_c1 = distCalc(c1, data_points)  # Function called to calculate distance of all points from c1
    dist_li_c2 = distCalc(c2, data_points)  # Function called to calculate distance of all points from c2
    print("Distance from centroid {0}: ".format(c1), dist_li_c1)
    print("Distance from centroid {0}: ".format(c2), dist_li_c2)
    cl_li_c1, cl_li_c2 = cluster(dist_li_c1, dist_li_c2)  # Function called to sort data-points into clusters
    print("First Cluster with centroid {0}: ".format(c1), cl_li_c1)
    print("Second Cluster with centroid {0}: ".format(c2), cl_li_c2)
    c1 = clusterMean(cl_li_c1)  # Re-Initialising Centroid c1 with new value
    c2 = clusterMean(cl_li_c2)  # Re-Initialising Centroid c2 with new value
    print("Centroid of First cluster after {0} Iteration: ".format(x + 1), c1)
    print("Centroid of Second cluster after {0} Iteration: ".format(x + 1), c2)
    print("*" * 150)
    li_c1.append(c1)  # Adding values of c1 into list
    li_c2.append(c2)  # Adding values of c2 into list
    x = x + 1

print("Centroid of First Cluster remain same: ", checkCentroid(li_c1))  # Checking whether centroid values remain same
print("Centroid of Second Cluster remain same: ", checkCentroid(li_c2))  # Checking whether centroid values remain same
