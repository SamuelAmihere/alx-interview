#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi.dev/api/films';

function fetchCharacterNames (url) {
  request(url, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const movieUrl = `${API_URL}/${movieId}/`;
  fetchCharacterNames (movieUrl);
}
