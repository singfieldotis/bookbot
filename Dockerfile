FROM debian:stable-slim
#COPY source destination
COPY bookbot /bin/bookbot
CMD ["/bin/bookbot"]
