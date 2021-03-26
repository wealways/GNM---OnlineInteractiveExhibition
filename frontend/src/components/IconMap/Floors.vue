<template>
    <div>
        <div class="layer-container stacked-top">
            <div @click='gotomone' class="layer bottom-layer blue-layer">
            </div>
            <div @click='gotoklimt' class="layer mid-layer green-layer"></div>
            <div @click='gotocheon' class="layer top-layer red-layer"></div>
        </div>
        <div class='right_side'>
            <div class='artist'>{{ explain }}</div>
            <div class='go_button' style='margin-top:20px;'>
                <q-btn 
                    :to='"/mone"' 
                    target="_blank" 
                    v-show="explain==='모네'" 
                    align="around" 
                    class="btn-fixed-width" 
                    color="deep-orange" 
                    label="1층 가기" 
                    icon="lightbulb_outline"
                />
                <q-btn
                    :to='"/klimt"' 
                    target="_blank"  
                    v-show="explain==='클림트'" 
                    align="around" 
                    class="btn-fixed-width" 
                    color="deep-orange" 
                    label="2층 가기" 
                    icon="lightbulb_outline" 
                />
                <q-btn
                    :to='"/cheon"' 
                    target="_blank"  
                    v-show="explain==='천경자'" 
                    align="around" 
                    class="btn-fixed-width" 
                    color="deep-orange" 
                    label="3층 가기" 
                    icon="lightbulb_outline" 
                />
            </div>
        </div>
    </div>
</template>

<script>
// import $ from 'jquery'

export default {
    name:'Map',
    data(){
        return{
            explain: '가고 싶은 층을 선택하세요'
        }
    },
    methods:{
        gotomone(){
            this.explain = "모네"
        },
        gotoklimt(){
            this.explain = "클림트"
        },
        gotocheon(){
            this.explain = "천경자"
        }
    },
    mounted(){
        // $(document).ready(function(){
        //         $(".layer").click(function(){
        //             $(this).toggleClass("highlight");
        //             $(this).siblings().toggleClass("fade");
        //     });
        // });
    }
}
</script>

<style lang="scss">

.layer-container {
    width: 200px;
    height: 200px;
    position: absolute;
    top: 76%;
    right: 30%;
    margin: -100px -100px 50px -200px;
    perspective: 2000px;
   transform-style: preserve-3d;
}

.layer {
    width: 200px;
    height: 200px;
    position: absolute;
    transition: all 0.5s ease-in-out;
    cursor: pointer;
    z-index: 1;
    opacity: 0.6;
}

.layer:hover {
  opacity: 0.9;
}

.blue-layer { /*bottom - blue*/
    background: rgba(19, 54, 90, 0.8);
    /*background-image: url('img/teaser.png');*/
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}


.green-layer { /*mid - green*/
    background: rgba(49, 76, 104, 0.8);
    /*background-image: url('img/22matcha.JPG');*/
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}

.red-layer { /*top - red*/
    background: rgba(181, 207, 231, 0.8);
    /*background-image: url('img/teaser_banner.png');*/
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}

.bottom-layer {
    transform: rotateX(45deg) rotateZ(45deg) translateZ(0);
}

.mid-layer {
    transform: rotateX(45deg) rotateZ(45deg) translateZ(100px);
}

.top-layer {
    transform: rotateX(45deg) rotateZ(45deg) translateZ(200px);
}

.marker {
  transition: all 0.5s ease-in-out;
  opacity: 0.75;
}

.marker:hover {
  opacity: 1.0;
}

/* A N I M A T I O N S */

@keyframes stack-move-top-3d{
   0%{
       transform: rotateX(45deg) rotateZ(45deg) translateZ(100px);
    }
    50%{
        transform: rotateX(45deg) rotateY(90deg) rotateZ(45deg) translate3d(-50px,100px,170px);
    }
    
   100%{
        transform: rotateX(45deg) rotateZ(45deg) translateZ(200px);
    }
}

.animate{
   animation: stack-move-top-3d 1.5s ease-in-out ;
}
    
/* for bottom-layer*/


    
.bottom.animate{
  animation: bottom-move-top-3d 1.5s ease-in-out;
}
     
@keyframes bottom-move-top-3d {
   0%{
       transform: rotateX(45deg) rotateZ(45deg) translateZ(0px);
    } 
 
    50%{
        transform: rotateX(45deg) rotateY(90deg) rotateZ(45deg) translate3d(-50px,100px,170px);
    }
    
   100%{
        transform: rotateX(45deg) rotateZ(45deg) translateZ(200px);
    }
}

.highlight {
  opacity: 1.0;
}

.fade {
  opacity: 0.15;
}

.right_side {
    position: absolute;
    font-family: 'Noto Sans KR';
    font-weight: 800;
    left: 10%;
    top: 20%;
}

.artist {
    font-size: 30px;
}
button {
    background: transparent;
    width:100px;
    font-size: 30px;
    outline: 0;
    border: 0;
}
button:hover {
    color:  rgba(181, 207, 231, 0.8);
}
</style>