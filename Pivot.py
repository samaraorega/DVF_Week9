#Wide Format: Each column of data represents a variable & each row represents one observation
#The index is usually an integer, with 0 being the topmost row

#Long format: Each index is a point in time for each observation

#Creating a pivot table:
"some_dataframe.pivot(index='State', columns='Gender', values='Deaths_mean')"
#.unstack() moves the index to the right as a variable column while .stack() does the opposite