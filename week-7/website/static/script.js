const closeBt = document.querySelector("#close");
const usernameRequestBt = document.querySelector("#usernameRequestBt");
const nameUpdateBt = document.querySelector("#nameUpdateBt");
const signinForm = document.querySelector("#signinForm");

function hideMessageBox() {
  const messageBox = document.querySelector(".messageBox");
  messageBox.classList.add("hide");
}

if (closeBt) {
  closeBt.addEventListener("click", hideMessageBox);
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

signinForm.addEventListener("submit", function (e) {
  e.preventDefault();
  const userAccountInput = document.querySelector("#account");
  const userPasswordInput = document.querySelector("password");
  let messageBox = document.querySelector(".messageBox");
  if (messageBox) {
    messageBox.remove();
  }

  if (userAccountInput.value == "" || userPasswordInput == "") {
    const div = document.createElement("div");
    const bt = document.createElement("button");
    const h3 = document.createElement("h3");
    const main = document.querySelector(".main");
    bt.classList.add("close");
    div.classList.add("messageBox");
    div.classList.add("error");
    h3.append("帳號或密碼空白");
    bt.append("X");
    bt.setAttribute("id", "close");
    bt.addEventListener("click", hideMessageBox);
    div.append(bt);
    div.append(h3);
    main.append(div);
  } else {
    console.log("nice");
    // ajax? create a route to check from database
  }
});
