import sqlite3
from config import es
# Подключение к базе данных
conn = sqlite3.connect('documents.db')
cursor = conn.cursor()


# Создание индекса Elasticsearch
index_name = 'documents'
es.indices.create(index=index_name, ignore=400)


# Функция для добавления документа в базу данных и индексирования его в Elasticsearch
def add_document(doc_id, text):
    # Добавление документа в базу данных
    cursor.execute("INSERT INTO documents (id, text) VALUES (?, ?)", (doc_id, text))
    conn.commit()

    # Индексирование документа в Elasticsearch
    es.index(index=index_name, id=doc_id, body={'text': text})


# Функция для выполнения поискового запроса
def search(query):
    # Выполнение поискового запроса в Elasticsearch
    result = es.search(index=index_name, body={'query': {'match': {'text': query}}})

    # Возвращение результатов поиска
    return result['hits']['hits']




results = search('example')
for hit in results:
    print(hit['_source']['text'])
