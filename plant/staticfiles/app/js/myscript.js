$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = $(this).closest('.cart-quantity').find('.quantity');
    $.ajax({
        type: "GET",
        url: "showcart/pluscart/",
        data: {
            prod_id: id
        },
        success: function(data) {
            console.log("data=", data);
            eml.text(data.quantity);
            $('#amount').text(data.amount);
            $('#totalamount').text(data.totalamount);
        }
    });
});

$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = $(this).closest('.cart-quantity').find('.quantity');
    $.ajax({
        type: "GET",
        url: "showcart/minuscart/",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.text(data.quantity);
            $('#amount').text(data.amount);
            $('#totalamount').text(data.totalamount);
        }
    });
});

$('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var elem = $(this);
    $.ajax({
        type: "GET",
        url: "showcart/removecart/",
        data: {
            prod_id: id
        },
        success: function(data) {
            $('#amount').text(data.amount);
            $('#totalamount').text(data.totalamount);
            elem.closest('.cart-item').remove();
        }
    });
});

$('.plus-wishlist').click(function() {
    var id = $(this).attr("pid").toString();
    $.ajax({
        type: "GET",
        url: "/pluswishlist/",
        data: {
            prod_id: id
        },
        success: function(data) {
            window.location.href = "/product-detail/" + id;
        }
    });
});

$('.minus-wishlist').click(function() {
    var id = $(this).attr("pid").toString();
    $.ajax({
        type: "GET",
        url: "/minuswishlist/",
        data: {
            prod_id: id
        },
        success: function(data) {
            window.location.href = "/product-detail/" + id;
        }
    });
});
