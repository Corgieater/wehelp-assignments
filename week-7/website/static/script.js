const closeBt = document.querySelector("#close");
const usernameRequestBt = document.querySelector("#usernameRequestBt");
const nameUpdateBt = document.querySelector("#nameUpdateBt");

if (closeBt) {
  closeBt.addEventListener("click", function () {
    const messageBox = document.querySelector(".messageBox");
    messageBox.classList.add("hide");
  });
}

if (usernameRequestBt) {
  usernameRequestBt.addEventListener("click", async function () {
    let userInput = document.getElementById("username").value;
    const res = await fetch(
      `http://127.0.0.1:3000/api/members?username=${userInput}`
    );
    const data = await res.json();
    const userInfo = document.querySelector("#userInfo");
    if (data.data == null) {
      userInfo.textContent = "查無此使用者";
    } else {
      let inputName = data.data.name;
      let username = data.data.username;
      userInfo.textContent = " ";
      userInfo.textContent = `${inputName}(${username})`;
    }
  });
}

if (nameUpdateBt) {
  nameUpdateBt.addEventListener("click", async function () {
    let userInput = document.getElementById("name").value;
    const res = await fetch(`http://127.0.0.1:3000/api/member`, {
      method: "POST",
      headers: { content_type: "application/json" },
      body: JSON.stringify({ name: userInput }),
    });
    const data = await res.json();
    if (data.ok) {
      const nameUpdated = document.querySelector("#nameUpdated");
      const welcomeName = document.querySelector("#welcomeName");
      nameUpdated.textContent = " ";
      nameUpdated.textContent = `更新成功`;
      welcomeName.textContent = " ";
      welcomeName.textContent = userInput;
    } else {
      nameUpdated.textContent = " ";
      nameUpdated.textContent = `更新失敗`;
    }
  });
}
