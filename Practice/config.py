from elasticsearch import Elasticsearch

import csv

es = Elasticsearch(hosts=["http://127.0.0.1:9200"])

print(f"Connected to ElasticSearch cluster `{es.info().body['serchText']}`")  # cluster_name

# чтение файла
with open("./posts.csv", "r") as f:
    reader = csv.reader(f)

    for i, line in enumerate(reader):
        document = {
            "text": line[0],

        }
        es.index(index="index", document=document)