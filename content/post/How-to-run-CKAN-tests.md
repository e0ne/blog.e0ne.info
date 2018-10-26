---
title: "How to run CKAN tests"
date: 2018-01-04T16:49:00+03:00
draft: False
category: [Python]
tags: [opensource,ckan]
archives: [2018]
aliases:
    - post/How-to-run-CKAN-tests.aspx
---


CKAN is an open-source DMS (data management system) for powering data hubs and data portals. CKAN makes it easy to publish, share and use data. It powers datahub.io, catalog.data.gov and europeandataportal.eu/data/en/dataset among many other sites. [http://ckan.org/](http://ckan.org/)

Open source world is interesting and challenging. Sometimes it’s easy and cheap. Sometimes it’s hard to contribute and costs a lot. Looking into the CKAN I was surprised that it’s used by government portals. That’s why I tried to use it a bit. Here is my short manual that extends an [official one](http://docs.ckan.org/en/latest/contributing/test.html) how to run functional and unit tests.

Unfortunately, I don’t have enough time to make a pull request (maybe you can do it instead of me:) ), so I just make a blog now.

The main issues with tests run are:

 

- Documentation doesn’t cover all steps
- CKAN uses outdated versions of [Solr](http://lucene.apache.org/solr/) and [Node.JS](https://nodejs.org/en/)
- Some bugs in tests which will be described later

 

All these things were found (or even reverse-engineered) in sources and CKAN’s CI results. You can found all needed data in the manual, GitHub ([https://github.com/ckan/ckan/blob/master/circle.yml](https://github.com/ckan/ckan/blob/master/circle.yml) and [https://github.com/ckan/ckan/blob/master/.circleci-matrix.yml](https://github.com/ckan/ckan/blob/master/.circleci-matrix.yml))  and CI report for any pull request ([https://github.com/ckan/ckan/pulls](https://github.com/ckan/ckan/pulls)). I use the same versions as CI does.

 

I use Ubuntu 16.04 LTS distro in my environment. I strongly recommend to do it inside some virtual machine or containers. So it won’t break anything on your desktop or laptop.

### 1. Getting sources

Let’s go! First of all, you need to clone sources:

**git clone https://github.com/ckan/ckan.git**

 

### 2. Node.JS installation

For UI integration test you need to install [Node.JS v. 0.10.33](https://nodejs.org/en/blog/release/v0.10.33/). It won’t work on the latest version for sure. 

**curl -O https://nodejs.org/dist/v0.10.33/node-v0.10.33.tar.g**

**tar pxzf  node-v0.10.33.tar.gz**

**cd node-v0.10.33**

**./configure && make**

**sudo make install**

 

You can install required npm packages now to run tests in the future:

**npm install -g mocha-phantomjs@3.5.0 phantomjs@~1.9.1**

 

### 3. PostgreSQL installation

I used that version of PostgreSQL which is available on my Linux distro:

**apt install postgresql**

**apt install postgresql-server-dev-9.5**

### 4. Redis

It should be simple, just run:

**apt install redis-server**

 

### 5. Python dependencies.

I use virtualenv wherever it’s possible:

**cd ~/ckan**

**virtualenv .venv && . .venv/bin/activate**

Once virtualenv is ready and activated, it’s time to install python packages:

**pip install -r requirement-setuptools.txt**

**pip install -r requirements.txt**

**pip install -r dev-requirements.txt**

**python setup.py develop **

 

### 6. Database configuration

Configure some environment variables to get everything working. I used the same values as we’ve got in the Circle CI configuration:

**export CKAN_POSTGRES_DB=ckan_test**

**export CKAN_POSTGRES_USER=ckan_default**

**export CKAN_POSTGRES_PWD=pass**

**export CKAN_DATASTORE_POSTGRES_DB=datastore_test**

**export CKAN_DATASTORE_POSTGRES_WRITE_USER=ckan_default**

**export CKAN_DATASTORE_POSTGRES_READ_USER=datastore_default**

**export CKAN_DATASTORE_POSTGRES_READ_PWD=passexport**

Create required databases and grant permissions:

**sudo -E -u postgres ./bin/postgres_init/1_create_ckan_db.sh**

**sudo -E -u postgres ./bin/postgres_init/2_create_ckan_datastore_db.sh**

**sed -i -e 's/.*datastore.read_url.*/ckan.datastore.read_url = postgresql:\/\/datastore_default:pass@\/datastore_test/' test-core.ini**

**paster datastore -c test-core.ini set-permissions | sudo -u postgres psql**

 

### 7. Solr installation and configuration

To get tests passed I use [Solr v. 4.3.1](http://archive.apache.org/dist/lucene/solr/4.3.1/). There is a filed bug about [Solr version](https://github.com/ckan/ckan/issues/3673). CKAN tests don’t work with Solr 6.x now:

**curl-O  http://archive.apache.org/dist/lucene/solr/4.3.1/solr-4.3.1.tgz**

**tar zxvf solr-4.3.1.tgz**

Now you have to start Solr. You can run it as a daemon or run it in a separate terminal:

**cd solr-4.3.1/example/**

**java -jar start.jar**

 

Solr initialization is required too:

**export SOLR_HOME=~/solr-4.3.1**

**cd ~/ckan**

**./bin/solr_init/create_core.sh**

 

### 8. Initialize test data

**paster db init -c test-core.ini**

 

### 9. Run test CKAN server

**paster serve test-core.ini**

### 10. Finally, run UI tests

**mocha-phantomjs http://localhost:5000/base/test/index.html**

### 11. Run unit and functional tests

To run all tests you need to execute the following command:

**nosetests --ckan --reset-db --with-pylons=test-core.ini --nologcapture ckan ckanext**

Unfortunately, you’ll have some failed bugs due to the [https://github.com/ckan/ckan/issues/3675](https://github.com/ckan/ckan/issues/3675) :(. To successfully run all tests, you should use segments. E.g.:

**nosetests --ckan --reset-db --with-pylons=test-core.ini --nologcapture --segments=abc ckan ckanext**

 

