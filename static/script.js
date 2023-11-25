function changeFilter() {
    switch ($("#filter_type").val()) {
        case "single":
            $("#start_date").show();
            $("#end_date").hide();
            $("#n_images").hide();
            break;
        case "range":
            $("#start_date").show();
            $("#end_date").show();
            $("#n_images").hide();
            break;
        case "random":
            $("#start_date").hide();
            $("#end_date").hide();
            $("#n_images").show();
            break;
    }
}
$(document).ready(function () {
    changeFilter();
    $("#start_date").on("input", function () {
        $("#end_date").attr("min", $(this).val());
        if ($("#end_date").val() < $("#start_date").val()) {
            $("#end_date").val($("#start_date").val());
        }
    });
    $("#filter_type").on("input", function () {
        changeFilter();
    });
});