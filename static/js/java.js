const tabsBtns = document.querySelectorAll(".tabs__nav button");
const tabsItems = document.querySelectorAll(".tabs_item");
// скрывает табы 
function hideTabs() {
    tabsItems.forEach(item => item.classList.add("hide"));
    tabsBtns.forEach(item => item.classList.remove("active"));
}

function showTab(index)  {
    tabsItems[index].classList.remove("hide")
    tabsBtns[index].classList.add("active")
}

hideTabs();
showTab(0);

 tabsBtns.forEach((btn, index) => btn.addEventListener("click", () => {
     hideTabs();
     showTab(index);
 }));




 // Anchors
 const Anchors = document.querySelectorAll(".header__nav a")

 Anchors.forEach( anc => {
     anc.addEventListener("click", function(event) {
         event.preventDefault();
         const id = anc.getAttribute("href");
         const elem = document.querySelector(id);
         window.scroll({
             top: elem.offsetTop,
             behavior: 'smooth'
         })

     });
 });