const closeBt = document.querySelector("#close");

closeBt.addEventListener("click", function () {
  const messageBox = document.querySelector(".messageBox");
  messageBox.classList.add("hide");
});
