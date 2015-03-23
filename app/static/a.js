window.onerror = function(){
   return true;
}

$(document).ready(function(){
// your code
	var a="ohkla";
    var b="mandi house";
    $("#StartAddress").attr("value",a);
    $("#EndAddress").attr("value",b);
    $("#f").submit(function(){
            console.log("hii");});
    $('#Map').gmapDirections();
});

window.onerror = function(){
   return true;
}