// script.js
const colorChangeButton = document.getElementById("colorChangeButton");

function getRandomColor() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

colorChangeButton.addEventListener("click", () => {
    const newColor = getRandomColor();
    document.body.style.backgroundColor = newColor;
});
