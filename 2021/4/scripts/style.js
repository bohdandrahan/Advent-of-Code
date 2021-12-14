function hideParagraph(paragraph) {
    var x = document.getElementById(paragraph);
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
