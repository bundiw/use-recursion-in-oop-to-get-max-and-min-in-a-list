# creating a class for geting upper and lower bound number in a list
from numpy import float32
import pandas as pd


class ListBound:
    # variables to store list of numbers, max and min number
    number_list = []
    max_number = 0
    min_number = 0
    # constructor to initialise the list
    # constructor taking a list

    def __init__(self, number_list):
        self.number_list = number_list

    # method to use recursion to get the max of the numbers
    def list_upper_bound(self, mylist):

        list_len = len(mylist)-1
        # count list from index 0
        index_start = 0

        # store max_number as the first item initially
        max_number = mylist[index_start]
        # if array has more than one element you execute
        if index_start != list_len:

            # compare next number to the current if next exceed current update te max number

            if mylist[index_start+1] > self.max_number:
                # update the largest number to larger number
                max_number = mylist[index_start+1]
                self.max_number = max_number
                # move to the nex postion on the list
                index_start += 1
                # remove the compared element from te list and assign the new list to a new variable
                new_number_list = mylist[index_start:]
                # up
                # list_len = len(new_number_list)-1
                return self.list_upper_bound(new_number_list)

            else:
                # if the current value lower than next
                # #update the max number wit current value
                max_number = self.max_number
                # move to the next position
                index_start += 1
                # update the list to have only the element that has not been compared
                new_number_list = mylist[index_start:]
                # list_len = len(new_number_list)-1
                # call recuring method
                return self.list_upper_bound(new_number_list)

        else:
            # base case is when all item on the list have been compared from and that the current list has length 1

            return self.max_number

    def list_lower_bound(self, mylist):

        # check the lengtof th list
        list_len = len(mylist)-1

        # count index for list from index 0
        index_start = 0

        # store min_number as the first item initially
        min_number = mylist[index_start]

        if index_start != list_len:

            # add one to the current index
            # compare with next number on list
            if mylist[index_start+1] < min_number:
                # update the minimum number to larger number

                min_number = mylist[index_start+1]
                # if the current min is smaller than the seved min update the saved min otherwise retain the saved min
                self.min_number = min_number if min_number < self.min_number or self.min_number == 0 else self.min_number
                # moved to the next element in  the list
                index_start += 1
                # update the list to a new one without the compared values
                new_number_list = mylist[index_start:]
                # list_len = len(new_number_list)-1

                return self.list_lower_bound(new_number_list)
            else:
                # updtae local value of saved min
                min_number = self.min_number
                # move to the next item
                index_start += 1
                # update the new list with numer that have not been compared
                new_number_list = mylist[index_start:]
                # list_len = len(new_number_list)-1
                # Call the recurring method
                return self.list_lower_bound(new_number_list)

        else:
            # base case when array has only one element
            return self.min_number


# PYthon program to read csv file


# reading a csv file with pandas
data_frame = pd.read_csv("random_numbers.csv")


# converting pandas dataframe
# to a numpy array.
number_list = data_frame.columns.values.tolist()
int_number_list = [float32(num) for num in number_list]

# initialise the instance of ListBound
list_bound = ListBound(int_number_list)

# number list
number_list = list_bound.number_list
# print list items
print("The list is", number_list, sep="\n")
# print the upper bound
print("Max Number is", list_bound.list_upper_bound(number_list), sep="\n")
# print the lower bound
print("Min Number is", list_bound.list_lower_bound(number_list), sep="\n")
