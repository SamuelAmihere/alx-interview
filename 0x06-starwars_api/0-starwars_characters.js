#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films';

function fetchCharacterNames(characterUrls) {
  return characterUrls.map((url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, _, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  });
}

if (process.argv.length > 2) {
  request(`${API_URL}/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
      return;
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
} else {
  console.error('Please provide a movie ID as a positional argument.');
  process.exit(1);
}
