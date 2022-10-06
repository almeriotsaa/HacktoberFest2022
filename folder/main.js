function onBtnClicked() {
    alert("Button Clicked");
}

function newOnbtnclicked(){
    console.log("hello there. You just clicked me!");
}
function onformsubmitted()
{
    //console.log(username,userroll);
    var name = document.getElementById("username").value;
    var roll = document.getElementById("userroll").value;
    console.log(name, roll);
}