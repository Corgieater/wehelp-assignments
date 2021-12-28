let hyperlinks = document.querySelectorAll("a")
let bt = document.querySelector("#bt")
let burger = document.querySelector("#burger")
let lis = document.querySelectorAll(".fake_list > li")

for (link of hyperlinks){
    link.addEventListener("click", function(e){
        e.preventDefault();
    })
}

bt.addEventListener('click', function(){
    fake_list = document.querySelector(".fake_list")
    fake_list.classList.toggle("appear");
})

for (li of lis){
    li.addEventListener("mouseover", function(){
        this.style.backgroundColor = "#e76f51";
        this.style.fontWeight = "bold"
    })
}

for (li of lis){
    li.addEventListener("mouseout", function(){
        this.style.backgroundColor = "darksalmon";
        this.style.fontWeight = "normal"
    })
}

burger.addEventListener("click", function(e){
    e.preventDefault();
    let list_holder = document.querySelector("#list_holder")
    list_holder.classList.toggle("show_list")
})