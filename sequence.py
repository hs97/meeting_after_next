import pandas as pd
import datetime

def month_diff(next, this):
    """
    This function returns the difference in number of months 
    between two dates
    """
    return (next.year - this.year) * 12 + next.month - this.month

def find_seq(filename, n):
    """
    This function finds the possible sequences for setting expectations 
    with the next n-th meeting.
    """
    dates = pd.read_csv(filename)
    # Formatting dates
    dates["date"] = dates["date"].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
    # Indexing dates by how many months they are away from the first month
    dates["month_ind"] = dates['date'].apply(lambda x: month_diff(x, dates['date'][0])).astype(int)
    # Find the difference in months between this meeting and the next n-th meeting
    dates["diff"] = dates["month_ind"].shift(-n) - dates["month_ind"]
    # Creating an array representing all months from start to end
    # True if there's a meeting in that month, False otherwise. 
    all = [True if any(dates["month_ind"] == x) else False for x in range(dates["month_ind"].iloc[-1]+1)] 
    # Finding the max difference between the meeting month and the month of the
    # n-th next meeting. Using the max difference to partition the set of all
    # possible months
    max_diff = dates["diff"].max().astype(int) + 1
    sequences = [tuple(all[x:x+max_diff]) for x in range(len(all) - max_diff)]
    # Finding the set of these sequences
    return set(sequences)

if __name__ == "__main__":
    # Print all possible sequences
    for a in find_seq("dates.csv", 2):
        print a

