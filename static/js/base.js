const footer=document.getElementById("footer");
const contacts=document.getElementById("contacts");

contacts.addEventListener("click",e=>{
    window.scroll({
        top: footer.offsetTop,
        behavior: 'smooth'
    });
});