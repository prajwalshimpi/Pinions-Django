

$("#signInButton").bind("click", function(){
  var wrapper = $("#loginWrapper");
  wrapper.removeClass("error").addClass("loading");

 setTimeout(function(){
    wrapper.removeClass("loading");
  }, 2000);
    var username = document.getElementById("username").value;
	alert(username);
  var password = document.getElementById("password").value;
  var data = { username:username, password:password };
   //window.location.href="/auth/";
   var args = { type:"POST", url:"/auth/", data:data };
  return false;
})