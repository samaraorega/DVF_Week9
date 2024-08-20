#Concatenation is adding contents of a second collection to the end of the first collection
#Syntax:
'to_concat = [df1, df2, df3]'
'big_df = pd.concat(to_concat)'

#There are four types of joins:
#Inner, Left, Right and Outer
#.join() method does the joining
"joined_df = df1.join(df2, how='inner')"
#You must pass the right table