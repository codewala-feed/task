const btn1 = document.getElementById("btn1")
btn1.addEventListener("mousedown", function(){
    btn1.style.boxShadow = "4px 4px 20px aliceblue";
})

btn1.addEventListener("mouseup", function(){
    btn1.style.boxShadow = "";
})

function cancel(){
    const output = document.getElementById("response-div")
    output.style.display = "none";
}
