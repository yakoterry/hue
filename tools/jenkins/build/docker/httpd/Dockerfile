FROM httpd:2.4

LABEL description="Hue Project https://github.com/cloudera/hue"

COPY hue /opt/hue
COPY httpd/httpdstart /usr/local/bin/

RUN groupadd -g 1123 hue
RUN useradd -g 1123 -l -M -s /bin/false -u 1123 hue

EXPOSE 8889
CMD ["httpdstart"]
