const os = require('os');
const path = require('path');
const fs = require('fs');

const affirmations = [
    "You are capable of achieving great things.",
    "Every day is a new opportunity to grow and improve.",
    "Believe in yourself and your abilities.",
    "You are worthy of love and respect.",
    "Challenges are opportunities to learn and become stronger.",
    "You have the power to create the life you desire.",
]

const desktopPath = path.join(os.homedir(), 'Desktop', 'Courses_Projects', 'Node', 'modules', 'task');

function saveRandomAffirmationToDesktop() {
    const randomAffirmation = affirmations[Math.floor(Math.random() * affirmations.length)];
    const newFilePath = path.join(desktopPath, 'daily-affirmations.txt');
    fs.writeFile(newFilePath, randomAffirmation, (err) => {
        if (err) {
            console.error("Error writing affirmation file", err);
        } else {
            console.log("Affirmation saved to desktop successfully");
        }
    });
}
saveRandomAffirmationToDesktop();