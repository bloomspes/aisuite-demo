const form = document.getElementById("chat-form");
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const vendor = document.getElementById("vendor").value;
  const message = document.getElementById("message").value.trim();
  const resultBox = document.getElementById("result");
  resultBox.textContent = "";

  const res = await fetch("/chat/stream", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ vendor, message }),
  });

  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    resultBox.textContent += decoder.decode(value);
  }
});
