# Tip Calculation
A simple program that calculates the total amount of tips each employee receives.

### How it Works

First it gets a gets of employees from the user. Then the user enters the number of hours each employee worked followed by the total number of tips.

Then the program sums the hours of each employee and then does the calculation of total_tips/total_hours. This gives a dollar per hour decimal which is then multiplied by the hours each employee worked to give each employees tip earnings for the week.

From here the decimal is dropped and the weeks tip earnings of each employee is summed ( 1. Because the decimal is dropped for the summing the money will be less the the total money earned that week; 2. Note, the decimal we "dropped" data is still saved, this is important for later). Then this sum is subtracted by the total tip money to get the money that is left to be distributed. The computer then sorts the list of employees based on the decimal following their tip earnings for the week.

Example:

Before sorting
 - Dan : $31.75
 - Tom : $20.95
 - Sarah : $30.33
 - Kim : $25.50
 
 After sorting
  - Tom : $20.95
  - Dan : $31.75
  - Kim : $25.50
  - Sarah : $30.33
  
Final the decimal is actually dropped and then the left over dollars are distributed. (Change is not given that is why the decimal isn't used in the distribution of the tips.)

The last figures that are displayed are the dollar amounts each employee will receive for the week.