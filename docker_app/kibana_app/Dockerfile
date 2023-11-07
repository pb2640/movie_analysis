# Use the official Kibana Docker image
FROM docker.elastic.co/kibana/kibana:7.15.1

# Expose Kibana's default port
EXPOSE 5601
EXPOSE 9200

# Set the Elasticsearch URL to connect to
# ENV ELASTICSEARCH_HOSTS=http://192.168.1.157:9200
# RUN curl http://192.168.1.157:9200
COPY kibana.yml /usr/share/kibana/config
# Start Kibana when the container runs
CMD ["kibana"]
