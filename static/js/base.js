const anchors = document.querySelectorAll(".header__nav a")

anchors.forEach(anc => {
    anc.addEventListener("click", function (event) {
        const id = anc.getAttribute("href");
        if (id.charAt(0) === '#') {
            event.preventDefault();
            const elem = document.querySelector(id);
            window.scroll({
                top: elem.offsetTop,
                behavior: 'smooth'
            });
        }
    });
});