FROM node:8-alpine as builder

RUN npm set progress=false && npm config set depth 0 && npm cache clean --force

# set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /usr/src/app/package.json
RUN npm install
RUN npm install -g @angular/cli@6.2.3

# add app
COPY . /usr/src/app

# start app
CMD ng serve --host 0.0.0.0