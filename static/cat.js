$(document).ready(function(){
	
    $(".navbutton").click(function(){
        $("#navitems").fadeToggle();

    });
	
  $( "#art_text:first" ).animate({
    left: 600
  }, {
    duration: 1000,
    step: function( now, fx ){
      $( "#art_text:gt(0)" ).css( "left", now );
	  $( "#food_text:gt(0)" ).css( "left", now );
	  $( "#other_text:gt(0)" ).css( "left", now );
    }
 
});
 $( "#food_text:first" ).animate({
    left: 600
  }, {
    duration: 1000,
    step: function( now, fx ){
     
	  $( "#other_text:gt(0)" ).css( "left", now );
    }
 
});
 $( "#other_text:first" ).animate({
    left: 600
  }, {
    duration: 1000,
    step: function( now, fx ){
  
	  $( "#food_text:gt(0)" ).css( "left", now );
	
    }
 
});

});