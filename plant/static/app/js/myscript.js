$(document).ready(function() {
    $('.plus-cart').click(function() {
        var id = $(this).attr("pid").toString();
        var quantityElement = $(this).siblings('.quantity');
        console.log("pid =", id);
        $.ajax({
            type: "GET",
            url: "/pluscart/",
            data: {
                prod_id: id
            },
            success: function(data) {
                console.log("data=", data);
                quantityElement.text(data.quantity);
                $('#amount').text(data.amount);
                $('#totalamount').text(data.totalamount);
            }
        });
    });
    $('.minus-cart').click(function(){
        var id=$(this).attr("pid").toString();
        var eml=this.parentNode.children[2] 
        $.ajax({
            type:"GET",
            url:"minuscart/",
            data:{
                prod_id:id
            },
            success:function(data){
                console.log("data=", data);
                quantityElement.text(data.quantity);
                $('#amount').text(data.amount);
                $('#totalamount').text(data.totalamount);     }
        })
    })
    
    
    $('.remove-cart').click(function(){
        var id=$(this).attr("pid").toString();
        var eml=this
        $.ajax({
            type:"GET",
            url:"removecart/",
            data:{
                prod_id:id
            },
            success:function(data){
                console.log("data=", data);
                quantityElement.text(data.quantity);
                $('#amount').text(data.amount);
                $('#totalamount').text(data.totalamount);      }
        })
    })
})
