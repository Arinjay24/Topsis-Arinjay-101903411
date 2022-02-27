# TOPSIS Package in Python
Submitted by: Arinjay Shukla

Roll no: 101903411

# Concept of TOPSIS
TOPSIS is an acronym that stands for Technique of Order Preference Similarity to the Ideal Solution and is a pretty straightforward MCDA method. As the name implies, the method is based on finding an ideal and an anti-ideal solution and comparing the distance of each one of the alternatives to those.

# How to use
The package TOPSIS-Arinjay-101903411 can be run though the command line as follows:

>> pip install TOPSIS-Arinjay-101903411
>> python
>>> from topsis_cal.topsiscode import topsis
>>> topsis("data.csv","1,1,1,2","+,+,-,+")


The rankings are displayed in the form of a table using a package 'tabulate', with the 1st rank offering us the best decision, and last rank offering the worst decision making, according to TOPSIS method.
