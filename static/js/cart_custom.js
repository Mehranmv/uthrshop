function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie("csrftoken");

$(document).on("click", ".change-quantity", function () {
    changeProduct(this);
});


function changeProduct(elem) {
    const quantity = $(elem).val()
    const p_id = $(elem).attr('id')
    const total_price = $("#total_price")
    const price = $("#price").attr('data-product-price')


    $.ajax({
        type: "POST",
        url: "/cart/update_quantity/",
        data: {
            p_id: p_id,
            quantity: quantity,
            csrfmiddlewaretoken: csrftoken,

        },
        success: function (response) {
            const updatedPrice = response.updatedPrice;
            $(elem).closest('tr').find('.product_price_container').text('$' + updatedPrice);
            var tp = parseFloat(total_price.attr('data-total-value'));
            var p = parseFloat(price) + tp
            total_price.text('$' + p)
            total_price.attr('data-total-value',p)
        }
    })
}


$(document).on("click", ".remove-product", function (e) {
    e.preventDefault();
    const elem = $(this);
    const productId = elem.attr('data-product-id');
    const color = elem.attr('data-color');
    const size = elem.attr('data-size');

    $.ajax({
        type: "POST",
        url: "/cart/remove/",
        data: {
            product_id: productId,
            color: color,
            size: size,
            csrfmiddlewaretoken: csrftoken,
        },
        success: function (response) {
            // elem.closest('tr').remove();
            location.reload();
        }
    })
});