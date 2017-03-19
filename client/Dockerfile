FROM node

ENV NPM_CONFIG_LOGLEVEL warn
ENV NODE_ENV production

RUN mkdir -p /frontend
WORKDIR /frontend
COPY ./ ./

RUN npm install
RUN npm install -g bower
RUN bower install --config.interactive=false --allow-root

CMD [ "npm", "start" ]

EXPOSE 8081
