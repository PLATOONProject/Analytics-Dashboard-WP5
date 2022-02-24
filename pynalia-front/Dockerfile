# Nodejs Base image
FROM node
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
# install and app dependencies
COPY pynalia-front/ ./
RUN npm install
RUN npm install -g @angular/cli
# start app
CMD ng serve --host 0.0.0.0
