from src.elastic_to_pandas import ElasticCom
import pandas as pd

if __name__ == "__main__":

    offset = 0
    size = 10
    rounds = 1
    
    for i in range(rounds):
         data = ElasticCom(index='index-name', host="localhost",
                      port=9200, username="elastic", password="changeme",
                      authentication=True,
                      doc_type='doc', size=10, from_=0).search_and_export_to_df()

         
