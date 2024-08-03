#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
request.get(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
