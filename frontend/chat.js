import { appendChunk, showError, clearOutput } from "./dom.js";

const form = document.getElementById("chat-form");
const resultBox = document.getElementById("result");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const message = document.getElementById("message").value.trim();
  if (!message) {
    showError("메시지를 입력해주세요.");
    return;
  }

  clearOutput();

  const url = `/chat/stream?message=${encodeURIComponent(message)}`;
  const eventSource = new EventSource(url);

  eventSource.onmessage = (event) => {
    appendChunk(event.data);
  };

  eventSource.onerror = () => {
    showError("⚠️ 응답 중 오류가 발생했습니다.");
    eventSource.close();
  };
});
