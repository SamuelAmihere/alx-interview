#!/usr/bin/node
const request = require('request');
const { promisify } = require('util');
const requestPromise = promisify(request);

async function getCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    try {
        const response = await requestPromise(url);
        const movieData = JSON.parse(response.body);
        const characterUrls = movieData.characters;

        const characterPromises = characterUrls.map(async (characterUrl) => {
            const characterResponse = await requestPromise(characterUrl);
            const characterData = JSON.parse(characterResponse.body);
            console.log(characterData.name);
        });

        await Promise.all(characterPromises);
    } catch (error) {
        console.error('An error occurred:', error);
    }
}

const movieId = process.argv[2];
if (!movieId) {
    console.error('Please provide a movie ID as a positional argument.');
    process.exit(1);
}

getCharacters(movieId);
