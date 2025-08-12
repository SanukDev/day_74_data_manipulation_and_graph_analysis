import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', header=0, names=['DATE','TAG','POSTS'])

print(df.head())
print(df.shape)

# Challenge: Calculate the total number of post per language. Which Programming language has had the highest
# total number of posts of all time?
print(df.groupby('TAG').sum())


# Challenge: Convert the type data in ['DATE'] to date time type
df['DATE'] = pd.to_datetime(df['DATE'])
print(df.head)

# Pivoting the data
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS' )

# Challenge: What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column names
# and print out the first 5 rows of the dataframe.
print(reshaped_df.head())
print(reshaped_df.shape)


# we want to substitute the number 0 for each NaN value in the DataFrame
reshaped_df = reshaped_df.fillna(0)
#

#--------- CREATING A GRAPH
# plt.plot(reshaped_df.index, reshaped_df['python'], reshaped_df['java'])

for column in reshaped_df.columns:
    print(column)
    plt.plot(reshaped_df.index, reshaped_df[column], label= reshaped_df[column].name)
    plt.ylabel('Some number')

plt.legend()
plt.show()