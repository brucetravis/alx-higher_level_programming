#!/usr/bin/node

/*
  Script that prints the title of a Star Wars movie where the episode number matches a given integer.

  Usage: ./3-starwars_title.js <movie-ID>

  The first argument is the movie ID.
  You must use the Star Wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id.
  You must use the module request.
*/

const request = require('request');

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
