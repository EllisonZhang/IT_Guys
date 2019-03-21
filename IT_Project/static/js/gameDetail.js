
  var elements = document.getElementsByClassName('used_images');
  imageUsed = elements[0]
  document.getElementById("game_image").src = imageUsed.src;
  $('.likez').click(function () {
    var reviewid;
    reviewid = $(this).attr("data-reviewid");
    var beginnindId = "l";
    var endId = reviewid.toString();
    var id = beginnindId.concat(endId);
    document.getElementById(id).style.display = "none";
    $.get('/wegame/like/', { review_id: reviewid}, function(data) {
      console.log(data)
      
      
      
        
    })
    
  })
  $('.dislikez').click(function () {
    var reviewid;
    reviewid = $(this).attr("data-reviewid");
    var beginnindId = "d";
    var endId = reviewid.toString();
    var id = beginnindId.concat(endId);
    $.get('/wegame/dislike/', { review_id: reviewid}, function(data) {
      console.log(data)
      
      
      
    })
    document.getElementById(id).style.display = "none";
  })

