
const fs = require('fs');

const message = '⋆˚✿˖° Hello, world! It\'s bright and sunny out today. ౨ৎ˚₊✩‧₊';

fs.writeFile('hello.txt', message, (err) => {
  if (err) {
    console.error("Error writing file", err);
  } else {
    console.log("File written successfully");
  }
});
