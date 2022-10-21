import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main(data):

    # bottles sold by zip code
    bottles_sold = data.groupby(by=['zip_code', ]).agg({'bottles_sold': 'sum'})
    plt.scatter(bottles_sold.index, bottles_sold, c=np.random.rand(len(bottles_sold.index), 3))
    plt.title('Bottles sold')
    plt.xlabel('Zip code')
    plt.ylabel('Bottles sold')
    plt.show()

    # table zip code, item description and bottles sold
    bottles_sold_item = data.groupby(by=['zip_code', 'item_description']).agg({'bottles_sold': 'sum'})
    print(bottles_sold_item.head())

    # percentage sale per store
    total_sales = sum(data['sale_dollars'])
    sales = data.groupby(by=['store_name']).agg({'sale_dollars': 'sum'})
    sorted_sales = sales.apply(lambda x: x.sort_values(ascending=True))
    per_sorted_sales = sorted_sales.apply(lambda x: (x / total_sales) * 100).round(2).tail(15)
    fig, ax = plt.subplots(figsize=(8,6))
    p = ax.barh(per_sorted_sales.index, per_sorted_sales.values.flatten(),height=0.7)
    ax.set_title('%Sales by store')
    ax.set_xlabel('%Sales', fontsize=12)
    ax.set_ylabel('Store name', fontsize=1)
    ax.bar_label(p, fmt='%.2f')
    ax.set_xlim(right=15)
    plt.xlim([0, 20])
    plt.show()

if __name__ == '__main__':

    df = pd.read_csv('C:\\Users\\Themis\\Desktop\\tutworkearly\\dataset\\sample.csv')
    print(df.info())
    print(df.shape)

    main(df)
