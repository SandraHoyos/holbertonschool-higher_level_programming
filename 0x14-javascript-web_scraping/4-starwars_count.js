#!/usr/bin/node
// writes web page to file

const request = require('request');
const { argv } = require('process');

request(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    if (film.characters.find((character) => character.includes('18'))) {
      count += 1;
    }
  }
  console.log(count);
});
