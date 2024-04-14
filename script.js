document.addEventListener('DOMContentLoaded', function () {
    const hiButton = document.getElementById('hi-button');
    const resultDiv = document.getElementById('result');

    hiButton.addEventListener('click', async function () {
        const response = await fetch('/get_hi', { mode: 'cors', credentials: 'same-origin' });
        const text = await response.text();
        resultDiv.innerText = text;
    });
});
