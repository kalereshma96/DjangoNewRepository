//for toggle
$(document).ready(function(){

 $("#menu-toggle").click(function(e) {
//        e.preventDefault();
    console.log(e);
        $("#wrapper").toggleClass("active");
       /* alert(1);*/
    });

});

//for take a note hide and show
$(document).ready(function(){
    var timeKeeper;

    $('#menu').click(function()
    {
        $('#menu ul').show();
    });

    $('#menu ul').click(function()
    {
        clearTimeout(timeKeeper);
    });

    $('#menu').focusout(function()
    {
        timeKeeper = setTimeout(function() {$('#menu ul').hide()}, 150);
    });

    $('#menu').attr('tabIndex', -1);
    $('#menu ul').hide();

});

// for more options dropdown
$(document).ready(function(){
  $('.dropdown-submenu a.test').on("click", function(e){
    $(this).next('ul').toggle();
    e.stopPropagation();
    e.preventDefault();
  });
});


$(document).ready(function(){
    $('#gear').click(function(){
       $('#dropdown').toggle();
    });
});