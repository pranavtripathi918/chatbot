const form = document.getElementById("ask-form");
if (form) {
  const box = form.querySelector("textarea");
  const btn = form.querySelector("button");

  box.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      if (box.value.trim()) form.requestSubmit();
    }
  });

  form.addEventListener("submit", () => {
    btn.disabled = true;
    btn.textContent = "Asking…";
  });
}