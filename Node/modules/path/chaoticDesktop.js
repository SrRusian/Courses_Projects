const path = require('path');

const fullPath = path.join('Users', 'rusian', 'Desktop', 'Courses_Projects', 'Node', 'modules', 'path');
const imageExtensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.PNG', '.JPG', '.JPEG', '.GIF', '.WEBP'];
const files = ['chaoticDesktop.js', 'app.js', 'image.png', 'photo.JPG', 'document.txt', 'graphic.webp'];

const firstImage = files.find(file => imageExtensions.includes(path.extname(file)));
if (firstImage) {
    console.log('First image file found:', path.join(fullPath, firstImage));
} else {
    console.log('No image files found in the directory.');
}

