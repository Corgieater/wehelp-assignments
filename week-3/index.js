const hyperlinks = document.querySelectorAll("a");
const bt = document.querySelector("#bt");
const burger = document.querySelector("#burger");
const lis = document.querySelectorAll(".fake_list > li");
const url =
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
const loadBtn = document.querySelector("#btn");
const mainUl = document.querySelector(".main >ul");
const btnArea = document.querySelector(".btnArea");
let startPoint = 0;
let endPoint = 8;

for (link of hyperlinks) {
  link.addEventListener("click", function (e) {
    e.preventDefault();
  });
}

bt.addEventListener("click", function () {
  fake_list = document.querySelector(".fake_list");
  fake_list.classList.toggle("appear");
});

for (li of lis) {
  li.addEventListener("mouseover", function () {
    this.style.backgroundColor = "#e76f51";
    this.style.fontWeight = "bold";
  });
}

for (li of lis) {
  li.addEventListener("mouseout", function () {
    this.style.backgroundColor = "darksalmon";
    this.style.fontWeight = "normal";
  });
}

burger.addEventListener("click", function (e) {
  e.preventDefault();
  let list_holder = document.querySelector("#list_holder");
  list_holder.classList.toggle("show_list");
});

// =============get info and show the first 8===============

const getData = async function () {
  const res = await fetch(url);
  const data = await res.json();
  const dataInfo = data.result.results;
  loadInfo(dataInfo, startPoint, endPoint);
};

// load more pics after clicked
loadBtn.addEventListener("click", async function () {
  const res = await fetch(url);
  const data = await res.json();
  const dataInfo = data.result.results;
  const dataLength = dataInfo.length;

  startPoint += 8;
  endPoint += 8;
  if (dataLength - endPoint < 8) {
    endPoint = dataLength;
  }
  makeMoreContainer(startPoint, endPoint); //make containers
  loadInfo(dataInfo, startPoint, endPoint);

  if (endPoint >= dataLength) {
    loadBtn.classList.add("hide");
    const p = document.createElement("p");
    const text = document.createTextNode("There is no pictures anymore!");
    p.appendChild(text);
    btnArea.appendChild(p);
  }
});

function makeMoreContainer(startIndex, endIndex) {
  for (let i = startIndex; i < endIndex; i++) {
    const li = document.createElement("li");
    const div = document.createElement("div");
    const describe_div = document.createElement("div");
    const img = document.createElement("img");
    const p = document.createElement("p");
    div.classList.add("card");
    div.appendChild(img);
    describe_div.classList.add("description");
    div.appendChild(describe_div);
    describe_div.appendChild(p);
    li.appendChild(div);
    mainUl.appendChild(li);
  }
}

function loadInfo(data, startIndex, endIndex) {
  const imgs = document.querySelectorAll(".card > img");
  const p = document.querySelectorAll(".description > p");
  for (let i = startIndex; i < endIndex; i++) {
    let photo = data[i].file.split(/.jpg/i);
    let text = document.createTextNode(data[i].stitle);
    imgs[i].src = `${photo[0]}.jpg`;
    p[i].appendChild(text);
  }
}
getData();
