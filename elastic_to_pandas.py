__doc__ = """A module containing the routines needed for reading the contents of an Elasticsearch (ES) into a Pandas DataFrame."""

from elasticsearch import Elasticsearch
import pandas as pd

def get_search_hits(es_response, _id=True, data_key=None):
    response_hits = es_response['hits']['hits']
    if len(response_hits) > 0:
        if data_key is None:
            for hit in response_hits:
                if '_source' in hit.keys():
                    data_key = '_source'
                    break
                elif 'fields' in hit.keys():
                    data_key = 'fields'
                    break
            if data_key is None:
                raise ValueError("Neither _source nor fields were in response hits")

        if _id is False:
            return [x.get(data_key, None) for x in response_hits]
        else:
            return [x.get(data_key, None) for x in response_hits]
    else:
        return []

class ElasticCom(object):
    
    def __init__(self, index, doc_type, max_result_window=200000, host='localhost',
                 port=9200, from_=0, size=10000, username="elastic", password="changeme",
                 authentication=True, **kwargs):
        """
        a class for fetching the contenst of an ES index and storing them into a Pandas DataFrame
        :param index: name of the index in ES
        :param doc_type: document type
        :param max_result_window: maximum result window to be retrieved (needed only in case of ES version > 2),
               notice: you might have to change maximum heap size in elasticsaerch.yml ot override the constraints
               of maximum results of ES
        :param hosts: IP address of ES
        :param from_: index pagination start point
        :param size:index pagination offset
        :param kwargs: --
        """
        
        self.index = index
        self.doc_type = doc_type
        self.from_ = from_
        self.size = size
        self.username = username
        self.password = password
        self.authentication = authentication
        self.max_result_window = max_result_window
        self.host = host
        self.port = port

        if authentication:
            self.es= Elasticsearch([{'host': self.host, 'port': self.port}], http_auth=(self.username, self.password))
        else:
            self.es = Elasticsearch([{'host': self.host, 'port': self.port}])

        try:
            self.es.indices.put_settings(index=self.index,
                                         body={"index": {"max_result_window": self.max_result_window}})
        except Exception as exc:
            print("Hey: " + exc.__str__())

    def search_and_export_to_dict(self, *args, **kwargs):
        """
        :param args: index parameters in a list
        :param kwargs: --
        :return: index contents as a Python 3 dictionary
        """
        
        _id = kwargs.pop('_id', True)
        data_key = kwargs.pop('data_key', kwargs.get('fields')) or '_source'
        kwargs = dict({'index': self.index, 'doc_type': self.doc_type}, **kwargs)
        if kwargs.get('size', None) is None:
            kwargs["request_timeout"] = 120
            t = self.es.search(*args, **kwargs)
            kwargs["size"] = self.size
            kwargs["from_"] = self.from_

        return get_search_hits(self.es.search(*args, **kwargs), _id=_id, data_key=data_key)

    def search_and_export_to_df(self, *args, **kwargs):
        """
        :param args: index parameters in a list
        :param kwargs: --
        :return: index contents as a Pandas DataFrame
        """
        
        return pd.DataFrame(self.search_and_export_to_dict(*args, **kwargs))


if __name__ == "__main__":

    offset = 0
    size = 10
    rounds = 1
    
    for i in range(rounds):
         data = ElasticCom(index='index-name', host="localhost",
                      port=9200, username="elastic", password="changeme",
                      authentication=True, doc_type='doc', size=10,
                           from_=0).search_and_export_to_df()
