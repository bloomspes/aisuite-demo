const resultBox = document.getElementById("result");

export function appendChunk(text) {
  resultBox.textContent += text;
}

export function showError(message) {
  const resultBox = document.getElementById("result");
  resultBox.textContent = '';

  const errorDiv = document.createElement('div');

  errorDiv.className = 'error';
  errorDiv.textContent = message;
  resultBox.appendChild(errorDiv)
}

export function clearOutput() {
  resultBox.textContent = "";
}