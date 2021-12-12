import matplotlib.pyplot as plt
import pandas            as pd

import openpyxl
import lxml

def first_task():
    df = pd.read_csv("transactions.csv")
    m = df[df['STATUS'] == 'OK']
    print(m.groupby(by = ['STATUS'])['SUM'].sum())
    print(*m.sort_values(by='SUM', ascending=False).iloc[0:3,3])

def second_task():
    flights = pd.read_csv("flights.csv", index_col=[0])

    plt.subplot(1, 3, 1)
    flights.groupby(by = ['CARGO'])['PRICE'].sum().plot(kind='bar', rot=0)
    plt.title("Цена, жалко, что белый будет не видно :)")
    plt.subplot(1, 3, 2)
    flights.groupby(by = ['CARGO'])['WEIGHT'].sum().plot(kind='bar', color='g', rot=0)
    plt.title("Вес.")
    plt.subplot(1, 3, 3)
    flights['CARGO'].value_counts().plot(kind= 'bar', color='r', rot=0)
    plt.title('Kолличество перелетов')
    plt.show()

def third_task():
    students_info = pd.read_excel('students_info.xlsx')
    resultes = pd.read_html('results_ejudge.html') 
    resultes = resultes[0]
    m = students_info.merge(resultes, left_on= 'login', right_on= 'User', how= 'outer')
    m.dropna(subset = ['login'], inplace= True)
    plt.subplot(1,2,1)
    m.groupby(by = 'group_faculty')['Score'].mean().plot.bar(rot= 0, color= 'red' )
    plt.subplot(1,2,2)
    m.groupby(by = 'group_out')['Score'].mean().plot.bar(rot= 0)
    f = m.copy()
    z = m.copy()
    z.dropna(subset= ['G'], inplace= True)
    f.dropna(subset= ['H'], inplace= True)
    cool_guys = pd.concat((z,f), axis = 0)
    print(cool_guys['group_faculty'].value_counts(), '\n',cool_guys['group_out'].value_counts())
    plt.show()

if __name__ == "__main__":

    print("##################################################")
    print("------------------------Firts---------------------")
    first_task()

    print("##################################################")
    print("----------------------Second----------------------")
    second_task()

    print("##################################################")
    print("-----------------------Third----------------------")
    third_task()
