document.addEventListener("DOMContentLoaded", function () {
    const text = document.getElementById("changing-text");
    const words = ["a Developer", "a Designer", "a Creator"];
    let index = 0;

    setInterval(() => {
        text.style.opacity = 0;
        setTimeout(() => {
            index = (index + 1) % words.length;
            text.textContent = words[index];
            text.style.opacity = 1;
        }, 500);
    }, 3000);
});
