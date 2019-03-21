var placeHolders = document.getElementsByTagName("label");
for (i = 0; i < placeHolders.length; i++) {
        placeHolders[i].style.display = 'none';
        var input = placeHolders[i].nextElementSibling;
        var text = placeHolders[i].innerHTML
        console.log(text);
        input["placeholder"] = text;
}