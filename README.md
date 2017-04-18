### Elastic_to_Pandas

A Python class for reading content of an ES index into a Pandas DataFrame

#### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

##### Prerequisites

For running the code you need an up-and-running Elasticsearch index along with a Python interpreter installed on your OS.
To install the requirements please use the `requirements.txt`, 	On Debian/Ubuntu you could run the following in terminal in order to installed the dependencies:
```Bash
sudo pip3 install -U -r requirements.txt # change pip3 to pip for Python2 installation
```

### API and use-cases

Use class `ElasticCom` and `search_and_export_to_df` method in the following example:

```Python
from elastic_to_pandas import ElasticCom

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
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the `CHANGELOG.md`.

