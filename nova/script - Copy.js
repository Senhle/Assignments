document.addEventListener("DOMContentLoaded", function () {
    const btn = document.querySelector(".btn");

    if (btn) {
        btn.addEventListener("click", function () {
            alert("Button Clicked!");
        });
    }
});
