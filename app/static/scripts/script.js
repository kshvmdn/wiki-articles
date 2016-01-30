var $input = document.getElementById("query");
$input.addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {  //checks whether the pressed key is "Enter"
        search()
    }
});

var search = function() {
    var query = $input.value;
    if (query != "")
        window.location = "/search/" + query;
}
