# YRHACKS_2024_WALLE
Product made for the 2024 YRHACKS hackathon
 <script>
        var xspeed=3;
        var yspeed=3;
        function moveImages() {
          if(getXPosition("image.png")>260||getXPosition("image.png")<0){
              xspeed=-xspeed;
            }
             if(getYPosition("image.png")>390||getYPosition("image.png")<0){
              yspeed=-yspeed;
              }
        }
        timedLoop(20, function(){
            setPosition("home1.html", getXPosition("image.png")+xspeed, getYPosition("image.png")+yspeed);
        });
                </script>
