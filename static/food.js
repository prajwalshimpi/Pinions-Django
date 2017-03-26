var i = 1,a=undefined; 
function showDiv() {
	var list=document.getElementById("grid");
	var text=document.getElementById("nametext").value;
  	
	var classname="class";						//creating div for tooltip
  	var tooltipdiv=document.createElement("a");
  	tooltipdiv.setAttribute("class",classname);
  	tooltipdiv.setAttribute("id","tooltipdiv");
  	list.appendChild(tooltipdiv);

    
    var oImg = document.createElement("img"); // creating label
	oImg.setAttribute('src', 'http://www.testtrackinglink.com');
	oImg.setAttribute('alt', 'na');
	oImg.setAttribute('height', '100px');
	oImg.setAttribute('width', '100px');
	list.appendChild(oImg);

	var editTag = document.createElement('a');//edit link
	editTag.setAttribute('href',"#nametext");
	editTag.setAttribute('class',classname);
	document.getElementById("nametext").select();
	editTag.innerHTML = "Edit";
	list.appendChild(editTag);



	document.getElementsByClassName(classname)[2].onclick=function() {    //edit onclick
		document.getElementById("nametext").value=document.getElementsByClassName(classname)[1].innerHTML;
		
		 
	}

	var delTag = document.createElement('a');
	delTag.setAttribute("href",'#');
	delTag.setAttribute('class',classname);
	delTag.innerHTML = "Delete";
	list.appendChild(delTag);

	document.getElementsByClassName(classname)[3].onclick =function() {
		var x = document.getElementsByClassName(classname);
		while(x.length>0) {
			list.removeChild(x[x.length-1]);
		}
		} 

	a = document.getElementsByClassName(classname);
	var z = document.createElement("BR");
    list.appendChild(z);	

	
var c = document.getElementsByClassName(classname)[0];
	document.getElementsByClassName(classname)[1].onmouseover=function show() {			//tooltip
		
		c.style.display="block";
		 c.style.top= (event.clientY-30)+"px";
        c.style.left= (event.clientX-20)+"px";
	}
	document.getElementsByClassName(classname)[1].onmousemove=function(){			//tooltip
		c.style.left= (event.clientX-20)+"px";
		c.style.top= (event.clientY-30)+"px";
	}
	document.getElementsByClassName(classname)[1].onmouseout=function hide() {
		document.getElementsByClassName(classname)[0].style.display="none";
	}

	 document.getElementById("nametext").value=''; //clearing text fields
	 i++;
}

 function save() {	//saving changes
		a[1].innerHTML=document.getElementById("nametext").value;
	    a[0].innerHTML=document.getElementById("desctext").value;
		
	}