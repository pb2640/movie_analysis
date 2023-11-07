# Use the official Elasticsearch Docker image
FROM docker.elastic.co/elasticsearch/elasticsearch:7.15.1
# container creator





# Copy your Python script and CSV file into the image
COPY elasticsearch.yml /usr/share/elasticsearch/config

# expose the default Elasticsearch port
EXPOSE 9200 9300
# Run the Python script to index data when the container starts
CMD ["elasticsearch"]
