window.addEventListener("scroll", function () {
    const model = document.getElementById("animatedModel");
    let bounding = model.getBoundingClientRect();

    if (bounding.top >= 0 && bounding.bottom <= window.innerHeight) {
        model.classList.remove("hidden");
        model.setAttribute("camera-controls", "");
        model.setAttribute("auto-rotate", "true");
    } else {
        model.classList.add("hidden");
        model.removeAttribute("camera-controls");
        model.removeAttribute("auto-rotate");
    }
});
