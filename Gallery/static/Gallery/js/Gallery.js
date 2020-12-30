
let root = document.documentElement;
$( "#id_painting_frame" ).change(function () {
    var frame_color = "";
    $( "#id_painting_frame option:selected" ).each(function() {
      frame_color += $( this ).text() ;
      console.log(frame_color)
    });

      console.log(frame_color)
  
  if(frame_color==="Black Flat Frame"){
    root.style.setProperty("--color", "black");
  } else if (frame_color=="Oak Effect Frame"){  
    root.style.setProperty("--color", "peru");
  } else if (frame_color=="Silver Foil Flat Frame"){ 
    root.style.setProperty("--color", "silver");
  }else if (frame_color=="Gold Rope Frame"){ 
    root.style.setProperty("--color", "orange");
  }else if (frame_color=="Khaki Frame"){ 
    root.style.setProperty("--color", "khaki");
  }
  }).change();



