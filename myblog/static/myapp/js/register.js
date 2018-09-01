$(document).ready(function(){

    $('#sent').on('click',function()
    {
        var a = $('[name = e-mail]').val();
        var ul = '/email/'+'?info='+a
        $.ajax({

            type:"get",
            url:ul,
            dataType :"json",
            success:function(data,status){
            $('#sent').remove();
            var d = data['data'];
            alert(d[0]);
            }

        })
    })



})