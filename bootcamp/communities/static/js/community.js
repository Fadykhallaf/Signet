// function submitCommunity() {
//     var last_community = $("#temp_community").value;
//     if (last_community == undefined) {
//         last_community = "parent";
//     }
//     console.log(last_community);
//     $("#community-form input[name='last_community']").val(last_community);
//     $.ajax({
//       url: '/community/vote/',
//       data: $("#community-form").serialize(),
//       type: 'post',
//       cache: false,
//       success: function (data) {
//         hide_stream_update();
//         console.log(data);
//       }
//     });
// }
