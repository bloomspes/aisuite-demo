export function appendChunk(text) {
  const resultBox = document.getElementById("result");
  resultBox.textContent += text;
}

export function showError(message) {
  const resultBox = document.getElementById("result");
  resultBox.innerHTML = `<div class="error">${message}</div>`;
}

export function clearOutput() {
  const resultBox = document.getElementById("result");
  resultBox.textContent = "";
}
