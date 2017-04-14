### Elastic_to_Pandas

A class for reading content of an ES index into a Pandas DataFrame (written  in  Python 3)

#### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

##### Prerequisites

For running the code you need an up-and-running Elasticsearch index along with a Python 3 interpreter installed on your OS.

To install the requirements please use the `requirements.txt`, 	On Debian/Ubuntu you could run the following in Terminal: 
```
sudo pip3 install -r requirements.txt
```

### API and usage

Use class `ElasticCom` and `search_and_export_to_df` method in the following example:

```
from src.elastic_to_pandas import ElasticCom
import pandas as pd

if __name__ == "__main__":

  data = ElasticCom(index='index-name', host="localhost",
	port=9200, username="elastic",
	password="changeme",
	authentication=True,
	doc_type='doc', size=10, from_=0)
	.search_and_export_to_df()
```
For more info use `help(ElasticCom)`

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the `CHANGELOG.MD`.

