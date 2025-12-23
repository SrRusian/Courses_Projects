const os = require('os');

let osType = os.type();

if (osType === 'Darwin') {
    osType = 'macOS';
}

console.log(`Operating System Type: ${osType}`);
console.log(`Platform: ${os.platform()}`);

console.log(`Total Memory: ${(os.totalmem() / (1024 ** 3)).toFixed(2)} GB`);

const uptimeInSeconds = os.uptime();
console.log(`I, your humble computer, have been awake for ${uptimeInSeconds} seconds.`)

const secondsInAWeek = 7 * 24 * 60 * 60;

const hours = Math.floor(uptimeInSeconds / 3600);
const minutes = Math.floor((uptimeInSeconds % 3600) / 60);
const seconds = Math.floor(uptimeInSeconds % 60);

console.log(`That's approximately ${hours} hours, ${minutes} minutes and ${seconds} seconds.`);const imageExtensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.PNG', '.JPG', '.JPEG', '.GIF', '.WEBP'];