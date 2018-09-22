// DATA IS BEING DIRECTLY RENDERED BY FLASK AND SENT TO THE DOM NOW //

var inputContainerHeight = $("#input-container").height()
console.log(inputContainerHeight)


// SOME IMPROVED TABLE FUNCTIONALITY USING MDBOOTSTRAP ADD-ONS//
// https://mdbootstrap.com/content/bootstrap-table-scroll/ //
$(document).ready(function () {
  $('#dtHorizontalVerticalExample').DataTable({
    "scrollX": true,
    "scrollY": inputContainerHeight - 369,
    // "sorting": false // false to disable sorting (or any other option)
    "order": [[ 4, "desc" ]],
    "lengthChange": false,
    "paging": false // false to disable pagination (or any other option)
  });
  $('.dataTables_length').addClass('bs-select');
});



