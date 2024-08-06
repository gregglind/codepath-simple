
.PHONY:*

data: 
	wget https://drivendata-public-assets.s3.amazonaws.com/data-engineer-takehome/data.zip && \
	mv data.zip data/raw && \
	cd data/raw && \
	unzip data.zip

db:
	python pipeline/models.py

from-csv: db

from-db: db

from-api: db

app:  db

dash: ;
