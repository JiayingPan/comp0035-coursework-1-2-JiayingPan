import pandas as pd

if __name__ == '__main__':

    # Add a line of code to print the dataframe contents
    df1 = pd.read_csv('London_PM2.5.csv')
    pd.set_option('display.max_rows', df1.shape[0] + 1)
    pd.set_option('display.max_columns', df1.shape[1] + 1)

    # 1. Print the number of rows and columns in the DataFrame
    print(df1.shape)

    # 2. Print the column labels and data types. Note any columns that you don't think are needed.
    print(df1.info(verbose=True))

    # 3. Drop the list of named columns `['locationId', 'city', 'local', 'unit', 'latitude', 'longitude']
    df1.drop(['locationId', 'city', 'country', 'local',  'unit', 'latitude', 'longitude'], axis=1, inplace=True)
    print(df1.info())

    # 4. Find and count the number of missing values, create a dataframe with the rows that contain missing values
    print(df1.isna().sum().sum())
    df1_isna = df1[df1.isna().any(axis=1)]
    print(df1_isna)

    # 5. Drop rows where there is a na in the value
    #df1.dropna(axis=0, inplace=True, subset=['value'])
    #df1_isna = df1[df1.isna().any(axis=1)]
    #print(df1_isna)

    # 6. Find the unique values for the Type column
    print(df1['parameter'].unique())

    # 7. Remove the extra spaces. replace the df[parameter"] series with the result of the str.strip() function
    #df1['parameter'] = df1['parameter'].str.strip()
    #print(df1['parameter'].unique())

    # 8. Clean the data for the second data set in a same way
    df2 = pd.read_csv('London_PM10.csv')
    pd.set_option('display.max_rows', df1.shape[0] + 1)
    pd.set_option('display.max_columns', df1.shape[1] + 1)
    print(df2.shape)
    print(df2.info(verbose=True))
    df2.drop(['locationId', 'location', 'country', 'city', 'local', 'latitude', 'longitude'], axis=1, inplace=True)
    print(df2.info())
    print(df2.isna().sum().sum())
    df2_isna = df2[df2.isna().any(axis=1)]
    print(df2_isna)
    #df2.dropna(axis=0, inplace=True, subset=['value'])
    #df2_isna = df2[df1.isna().any(axis=1)]
    #print(df2_isna)
    print(df2['parameter'].unique())
    #df2['parameter'] = df2['parameter'].str.strip()
    #print(df2['parameter'].unique())

    # 9. Merge the columns where df1['utc'] matches df2['utc']
    df_merged = pd.merge(df1, df2, on='utc', how='outer')
    print(df_merged.info())

    # 10. Rename the columns of 'value_x' and 'value_y' to distinguish PM2.5 and PM10
    df_merged.rename(columns={'value_x':'PM2.5', 'value_y':'PM10'}, inplace=True)

    # 11. Drop the columns of 'parameter_x' and 'parameter_y' with duplicate information
    df_merged.drop(['parameter_x', 'parameter_y'], axis=1, inplace=True)

    # 12. Add a column to calculate the sum of PM2.5 and PM10
    df_merged.loc[:, 'Total'] = df_merged.sum(numeric_only=True, axis=1)
    print(df_merged.info())

    # 13. Change the order of the 'Total' and 'unit' columns
    df_merged = df_merged.iloc[:,[0,1,2,3,5,4]]

    # 13. Export the prepared dataframe to a new csv file
    df_merged.to_csv('prepared_dataset.csv', index=False, header=True)

