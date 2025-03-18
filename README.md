# OpenSearch plugin for Dify
This plugin is used to search data in OpenSearch.

# Usage
1. setup your credential
2. use tool in workflow

## credential
- endpoint: The endpoint of OpenSearch, such as localhost:9200
- user: The user of OpenSearch, such as xiaoming
- password: The password of OpenSearch user

## Query
- index: The index of OpenSearch
- query: The OpenSearch query dsl, https://opensearch.org/docs/latest/query-dsl/
- from: The start index of OpenSearch, https://opensearch.org/docs/latest/search-plugins/searching-data/paginate/#the-from-and-size-parameters
- size: The size of OpenSearch, https://opensearch.org/docs/latest/search-plugins/searching-data/paginate/#the-from-and-size-parameters
