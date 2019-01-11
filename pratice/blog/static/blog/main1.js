$(document).ready(function(){

 $("#menu-toggle").click(function(e) {
//        e.preventDefault();
    console.log(e);
        $("#wrapper").toggleClass("active");
       /* alert(1);*/
    });

});

$(document).ready(function(){
    $("#myModal").click('shown.bs.modal', function(){
        $(this).find('input[type="text"]').toggle();
    });
});
