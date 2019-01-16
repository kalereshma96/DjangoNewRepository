$(document).ready(function(){

 $("#menu-toggle").click(function(e) {
//        e.preventDefault();
    console.log(e);
        $("#wrapper").toggleClass("active");
       /* alert(1);*/
    });

});
//
//$(document).ready(function(){
//    $("#myModal").click('shown.bs.modal', function(){
//        $(this).find('input[type="text"]').toggle();
//    });
//});

//
//$(document).ready(function() {
//     $("#show_hide").click(function () {
//     $("#toggle_tst").toggle()
//  });
//  });

$(function() {

    initDropDowns($("div.dropMenu"));

});

function initDropDowns(allMenus) {

    allMenus.children(".trigger").on("click", function(e) {

        e.stopPropagation();

        var thisTrigger = jQuery(this),
            thisMenu = thisTrigger.parent(),
            thisPanel = thisTrigger.next();

        if (thisMenu.hasClass("open")) {

            thisMenu.removeClass("open");

            jQuery(document).off("click");

        } else {

            allMenus.removeClass("open");
            thisMenu.addClass("open");

            jQuery(document).on("click", function() {
                allMenus.removeClass("open");
            });
        }
    });
}

//$('#email-signup').click(function(e){
//e.stopPropagation();});
//$("#email-signup-link").click(function(e) {
//    e.preventDefault();
//    e.stopPropagation();
//    $('#email-signup').show();
//});
//$(document).click(function() {
//    $('#email-signup').hide();
//});


$(function(){
  $('#demo').on('hide.bs.collapse', function () {
    $('#button').html('<span class="glyphicon glyphicon-collapse-down"></span> Show');
  })
  $('#demo').on('show.bs.collapse', function () {
    $('#button').html('<span class="glyphicon glyphicon-collapse-up"></span> Hide');
  })
})
