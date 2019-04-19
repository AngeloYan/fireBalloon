function loadPage() {
    let totalWidth = document.getElementById("submitForm").offsetWidth;
    let buttonWidth = document.getElementById("submitFormButton").offsetWidth;
    document.getElementById("submitFormInput").style.width =
        (totalWidth - buttonWidth - 20).toString() + "px";
}