const attachmentBtn = document.getElementById("attachment-btn");
const attachmentInput = document.getElementById("attachment-input");

attachmentBtn.addEventListener("click", () => {
  attachmentInput.click();
});

attachmentInput.addEventListener("change", () => {
  const currentFile = attachmentInput.files[0];

  const imagePreview = `<img src=${URL.createObjectURL(currentFile)} alt='preview-image' width='80%' height='80%' class='rounded-full' / >`;
  attachmentBtn.style.padding = 0;
  attachmentBtn.innerHTML = imagePreview;
});
