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

$(document).ready(function () {
    $("#add-to-cart").click(function () {
        const color = $("#color-select")
        const size = $("#size-select")
        const quantity = $("#quantity")
        const product_id = $("#product_id")
        const product_name = $("#product-name")

        $.ajax({
            type: "POST",
            url: "/cart/add/",
            data: {
                product_id: product_id.val(),
                color: color.val(),
                size: size.val(),
                price: $("#price").attr('data-product-price'),
                quantity: quantity.val(),
                csrfmiddlewaretoken: csrftoken,

            },
            success: function (response) {
            }
        });
    });
});

$(document).ready(function () {

    $("#color-select").change(function () {
        const color = $("#color-select");
        const sizes1 = $("#size-select");
        $.ajax({
            type: "POST",
            url: "/color/sizes/",
            data: {
                color: color.val(),
                slug: color.attr("data-product-slug"),
                csrfmiddlewaretoken: csrftoken,
            },
            success: function (response) {
                const sizes2 = response.sizes2;
                $("#size-select option").each(function () {
                    const optionValue = $(this).val();
                    if (!sizes2.includes(optionValue)) {
                        $(this).prop("disabled", "disabled");
                    } else {
                        $(this).prop("disabled", false);
                    }
                });
            },
        });
    });
})

$(document).ready(function () {
    $("#color-select , #size-select").change(function () {
        const color = $("#color-select");
        const size = $("#size-select");
        const button = $("#add-to-cart");
        const price = $("#price");
        const per_price = $("#per_price");

        $.ajax({
            type: "POST",
            url: "/update_price/",
            data: {
                color: color.val(),
                size: size.val(),
                slug: color.attr("data-product-slug"),
                csrfmiddlewaretoken: csrftoken,
            },
            success: function (response) {
                if (response.price === "Out of Stuck") {
                    button.attr("disabled", "disabled");
                    button.val("out of stuck");
                } else if (response.off_price) {
                    button.removeAttr("disabled");
                    button.val("Add to cart");
                    price.text("$" + response.price);
                    price.attr('data-product-price', response.price);
                    price.addClass('current_price');
                    price.css('color', '#ff2f2f')
                    per_price.text("$" + response.product_price);
                    per_price.addClass('old_price');

                } else {
                    button.removeAttr("disabled");
                    button.val("Add to cart");
                    price.text("$" + response.price);
                    price.attr('data-product-price', response.price)
                    price.addClass('curren_price')
                    price.css('color', '#000000')
                    per_price.empty()

                }
            },
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    // Send an Ajax request to the server
    var xhr = new XMLHttpRequest();
    var color = $("#color-select");
    var size = $("#size-select");
    var button = $("#add-to-cart");
    var price = $("#price")

    $.ajax({
        type: "POST",
        url: "/update_price/",
        data: {
            color: color.val(),
            size: size.val(),
            slug: color.attr("data-product-slug"),
            csrfmiddlewaretoken: csrftoken,
        },
        success: function (response) {
            if (response.price === "Out of Stuck") {
                button.attr("disabled", "disabled");
                button.val("out of stuck");
            } else {
                button.removeAttr("disabled");
                button.val("Add to cart");
                price.text("$" + response.price);
                price.attr('data-product-price', response.price)
                price.addClass('current_price');

            }
        },
    });
});

document.addEventListener("DOMContentLoaded", function () {
    // Send an Ajax request to the server
    var xhr = new XMLHttpRequest();
    const color = $("#color-select");
    const size = $("#size-select");
    const button = $("#add-to-cart");
    $.ajax({
        type: "POST",
        url: "/color/sizes/",
        data: {
            color: color.val(),
            slug: color.attr("data-product-slug"),
            csrfmiddlewaretoken: csrftoken,
        },
        success: function (response) {
            const sizes2 = response.sizes2;
            $("#size-select option").each(function () {
                const optionValue = $(this).val();
                if (!sizes2.includes(optionValue)) {
                    $(this).prop("disabled", "disabled");
                } else {
                    $(this).prop("disabled", false);
                }
            });
        },
    });
});



