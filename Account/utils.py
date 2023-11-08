import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
import pandas as pd
from Product.models import *

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def count_plot():
    df = pd.read_csv("static/flipkart3.csv") 
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.xticks(rotation=90)
    sns.countplot(data=df,x="brand",palette="Pastel1")
    plt.xlabel("Brand")
    plt.plot()
    plt.tight_layout()
    graph = get_graph()
    return graph

def brand_rating():
    df = pd.read_csv("static/flipkart3.csv")
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.xticks(rotation=60)
    sns.barplot(data=df,x="brand",y="Ratings",palette="Pastel1")
    plt.xlabel("Brand")
    plt.plot()
    plt.tight_layout()
    graph = get_graph()
    return graph

def brand_discount():
    df = pd.read_csv("static/flipkart3.csv")
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.xticks(rotation=60)
    sns.stripplot(data=df,x="brand",y="Discount",palette="Pastel1")
    plt.xlabel("Brand")
    plt.plot()
    plt.tight_layout()
    graph = get_graph()
    return graph

def predicted_price_chart(x,y):
    y = int(y.replace(',',''))
    data = {'X':[x,y],'Y':["Predicted Discounted Price","Discounted Price"]}
    df = pd.DataFrame(data)
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.xticks(rotation=60)
    sns.scatterplot(data=df,x="X",y='Y',hue=y,palette="Pastel1",markers='o')
    plt.xlabel("Category")
    plt.ylabel("Prices")
    plt.plot()
    plt.tight_layout()
    graph = get_graph() 
    return graph

def price_comparision():
    df = pd.read_csv("static/comparision.csv")
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    # plt.xticks(rotation=15)
    sns.barplot(data=df,x="name",y="price",palette="Pastel1",hue="website")
    plt.xlabel("Product_Name")
    plt.ylabel("Original_Price")
    plt.plot()
    plt.tight_layout()
    graph = get_graph()
    return graph