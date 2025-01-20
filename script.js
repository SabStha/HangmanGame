const words = ['python', 'developer', 'hangman', 'programming', 'code'];
const stages = [
    "Stage 1: Starting",
    "Stage 2: Head added",
    "Stage 3: Body added",
    "Stage 4: One arm added",
    "Stage 5: Second arm added",
    "Stage 6: One leg added",
    "Stage 7: Second leg added - Game Over!"
];

let word = words[Math.floor(Math.random() * words.length)];
let guessedWord = Array(word.length).fill("_");
let guessedLetters = [];
let remainingAttempts = 6;

document.getElementById('submit-btn').addEventListener('click', () => {
    const guess = document.getElementById('guess').value.toLowerCase();
    document.getElementById('guess').value = '';

    if (!guess || guessedLetters.includes(guess)) {
        document.getElementById('message').innerText = 'Invalid or duplicate guess!';
        return;
    }

    guessedLetters.push(guess);

    if (word.includes(guess)) {
        for (let i = 0; i < word.length; i++) {
            if (word[i] === guess) {
                guessedWord[i] = guess;
            }
        }
        document.getElementById('message').innerText = `Good job! ${guess} is in the word.`;
    } else {
        remainingAttempts--;
        document.getElementById('message').innerText = `Oops! ${guess} is not in the word.`;
    }

    // Update game display
    document.getElementById('word-display').innerText = guessedWord.join(' ');
    document.getElementById('guessed-letters').innerText = guessedLetters.join(', ');
    document.getElementById('remaining-attempts').innerText = remainingAttempts;
    document.getElementById('hangman-stage').innerText = stages[6 - remainingAttempts];

    // Check game status
    if (guessedWord.join('') === word) {
        document.getElementById('message').innerText = 'Congratulations! You guessed the word!';
        document.getElementById('submit-btn').disabled = true;
    } else if (remainingAttempts === 0) {
        document.getElementById('message').innerText = `Game Over! The word was: ${word}`;
        document.getElementById('submit-btn').disabled = true;
    }
});
