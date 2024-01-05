function getAjax() {
    $('#table_body').html(`<tr> <td colspan="4" class="text-center"> <div class="p-3 text-center"> <span class="spinner-border"> </span> </div> <td> </tr>`)
    $.ajax({
        url: '/api/personal',
        method: 'get',
        success: function (data) {
            // console.log(data)
            $('#table_body').html('')
            data.forEach((v, i) => {
                $('#table_body').append(`
                            <tr> 
                                <td> ${i + 1} </td>
                                <td> ${v.name} </td>
                                <td> ${v.number} </td>
                                <td> ${v.country} </td>
                                </tr>
                        `)
            })
        },
        error: function (data) {

        }
    })
}

getAjax() // init

function postAjax() {
    const ajax_data = {
        name: $('[name="name_value"]').val(),
        number: $('[name="number_value"]').val(),
        country: $('[name="country_value"]').val(),
    }

    $('#form_submit').addClass('disabled').attr('disabled', 'disabled')
    $.ajax({
        url: '/api/personal',
        method: 'post',
        data: ajax_data,
        headers: {
            'X-CSRF-TOKEN': window.csrf_token
        },
        success: function (data) {
            console.log(data)
            $('#form_submit').removeClass('disabled').removeAttr('disabled');
            getAjax() // update

        },
        error: function (data) {
            console.log(data)
            $('#form_submit').removeClass('disabled').removeAttr('disabled')

        }
    })
}

$('#form_submit').on('click', function () {
    let _self = $(this);
    postAjax() // init
})


// ===================Select option =========
let country_name = $('#country_name');
country_name.on('click', function (event) {
    let options = $(this).find('option');
    console.log(options)
    let list = '';

    options.each(function (value, index) {
        let text = $(this).text();
        let img = $(this).attr('data-country-img')
        console.log(text)
        list += (`
            <li class="custom_list_item"> <img src="${img}"> ${text} </li>
        `);

    })

    if ($(this).parent().find('.custom_list').length < 1) {

        $(this).parent().append(`<ul class="custom_list">
            ${list}
        </ul>`)
    }
})
