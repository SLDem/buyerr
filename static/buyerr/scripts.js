$('#id_category').change(function() {
    var url = $('#productForm').attr('data-sub-categories-url');
    var categoryId = $(this).val();

    $.ajax({
        url: url,
        data: {
            'category': categoryId
        },
        success: function (data) {
            $('#id_sub_category').html(data);
            console.log(data);
        }
    });
});
