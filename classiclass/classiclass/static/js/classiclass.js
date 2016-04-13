(function(){
  $(document).ready(function(){
    var mangify_section = $("#mangifies");
    var modal = $("#modal");
    
    $(".post").click(function(event){
      event.preventDefault();
      var post_hash_id = $(this).data("post-hash-id");
      var api_url = "api/posts/" + post_hash_id;

      $.ajax({
        url: api_url,
        method: "GET",
      }).success(function(data){
        var thumbnail_image = data["thumbnail_image"];
        var content = data["content"];
        var tags = data["tags"];

        var thumbnail_image_html = "<img src='" + thumbnail_image + "'width=100% height=auto >";
        //$("#modal").empty()
        modal.html("")
        modal.append(thumbnail_image_html);
      });
    });
  });
})();    
