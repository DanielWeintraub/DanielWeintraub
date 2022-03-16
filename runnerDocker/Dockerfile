FROM adoptopenjdk/openjdk11:aarch64-ubuntu-jre-11.0.14.1_1
RUN apt-get update
RUN apt-get install -y dumb-init
RUN mkdir /app
COPY ./pd-runner.jar /app/pd-runner.jar
WORKDIR /app
CMD "dumb-init" "java" "-jar" "pd-runner.jar"
