import matplotlib.pyplot as plt
import pandas as pd


def set_pandas_display_options(df):
    """ Sets the pandas display options based on the shape of the dataframe

    :param DataFrame df: the data
    """
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)


if __name__ == '__main__':
    df = pd.read_csv('Data/Prepared_dataset.csv', parse_dates=['utc'], dtype={'utc': str})
    set_pandas_display_options(df)

    # 1. Print the stats generated by describe
    print(df.describe())

    # 2. Generate a box plot to show the outliers (in a same box with same scale)
    bp = df.plot.box(title="Outliers")

    # 3. Generate box plots to show the outliers (in separate boxes with different scale)
    bp_sub = df.plot.box(subplots=True, title="Outliers")

    # 4. Create three line plots of PM monthly values versus dates
    df.plot.line(x='utc', y= ['PM10','PM2.5','Total'], ylabel="µg/m³", title="PM Monthly Variation")
    df.plot.line(x='utc', y= 'PM2.5', ylabel="µg/m³", title="PM2.5 Monthly Variation")
    df.plot.line(x='utc', y= 'PM10', ylabel="µg/m³", title="PM10 Monthly Variation")

    # 5. Create a line plot of PM2.5/PM10 ratio
    df['PM2.5:PM10'] = df['PM2.5'] / df['PM10']
    df.plot.line(x='utc', y='PM2.5:PM10', label="PM2.5/PM10 Ratio", title="PM Monthly Ratio Trend")

    # 6. Define the % equation
    df['PM2.5%'] = df['PM2.5'] / df['Total']
    df['PM10%'] = df['PM10'] / df['Total']

    # 7. Create line plots of the PM values in a certain day, and make the x-axis labels fully visible
    print(df[0:24])
    df.iloc[0:24].plot(x='utc',y=['PM2.5', 'PM10', 'Total'], ylabel="µg/m³", title="PM Daily Variation")
    plt.gcf().subplots_adjust(bottom=0.15)
    df.iloc[0:24].plot(x='utc',y='PM2.5', ylabel="µg/m³", title="PM2.5 Daily Variation")
    plt.gcf().subplots_adjust(bottom=0.15)
    df.iloc[0:24].plot(x='utc',y='PM10', ylabel="µg/m³", title="PM10 Daily Variation")
    plt.gcf().subplots_adjust(bottom=0.15)

    # 8. Create the stacked bar plot of the daily % for PM2.5 and PM10
    df.iloc[0:24].plot.bar(x='utc',y=['PM2.5%', 'PM10%'], stacked=True, title="PM daily Proportions")
    plt.gcf().subplots_adjust(bottom=0.5)

    # 9. Show all the plotting results
    plt.show()



