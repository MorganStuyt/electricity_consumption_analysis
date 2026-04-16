import matplotlib.pyplot as plt
import pandas as pd

# pip install matplotlib pandas


def load_data(newdata, existingfile):
    # import from csv or another data source and print the head
    
    #skip loading the header row HDR, as it only contains data relating to the creation of the file
    df = pd.read_csv(newdata, skiprows=1)
    
    #creating a new dataframe with only the required columns, then adding column labels
    new_df = df.iloc[:, [9,10,12]].copy()
    new_df.columns = ['Start Date', 'End Date', 'Consumption']
    new_df['Start Date'] = pd.to_datetime(new_df['Start Date'])
    #print(new_df.head())

    return new_df

def plot_data(data):
    df = data.dropna()

    fig, ax = plt.subplots()

    ax.plot(df['Start Date'], df['Consumption'], marker='o')

    plt.xlabel('Date')
    plt.ylabel('Consumption [kWh]')
    plt.show()

newdata = r'C:\git\electricity_consumption_analysis\data\CTCT_E_CUST_ICPCONS_202604_20260416_0235950955LCB3520260416125901.CSV'
data = load_data(newdata, existingfile = 1)
plot_data(data)