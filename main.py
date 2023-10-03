import pandas as pd
import ast
import json
from pandas import  json_normalize
from fastapi import FastAPI
app = FastAPI()
# http://127.0.0.1:8000


@app.get('/')
def index():
    return {'mensaje': 'Hola, Pythonianos'}


@app.get('/libros/{id}')
def mostrar_libro(id:int):
    return {'data': id}

@app.get('/head')
def mostrar_cabecera():
    reviews = []
    with open ('australian_user_reviews.json', 'r', encoding='utf-8') as f:
        for line in f.readlines():
                reviews.append(ast.literal_eval(line))


    df_reviews = pd.DataFrame(reviews)
    return df_reviews.head(6)