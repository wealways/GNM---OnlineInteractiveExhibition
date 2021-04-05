<template>
    <div class="">
        <div class="layer-container stacked-top">
            <div @click='gotomone' class="layer first-layer blue-layer"></div>
            <div @click='gotoklimt' class="layer second-layer green-layer"></div>
            <div @click='gotocheon' class="layer third-layer red-layer"></div>
            <div @click='gotospecial' class="layer fourth-layer red-layer"></div>
            <div @click='gotoguestbook' class="layer fifth-layer red-layer"></div>
        </div>
        <div class='right_side'>
            <div class='artist'>{{ explain }}</div>
            <div class='go_button' style='margin-top:20px;'>
                <q-btn 
                    :to='"/startmonet"' 
                    target="_blank" 
                    v-show="explain==='모네'" 
                    align="around" 
                    class="btn-fixed-width" 
                    color="deep-orange" 
                    label="1층 가기" 
                    icon="lightbulb_outline"
                />
                <q-btn
                    :to='"/startklimt"' 
                    target="_blank"  
                    v-show="explain==='클림트'" 
                    align="around" 
                    class="btn-fixed-width" 
                    color="deep-orange" 
                    label="2층 가기" 
                    icon="lightbulb_outline" 
                />
                <q-btn
                    :to='"/startcheon"' 
                    target="_blank"  
                    v-show="explain==='천경자'" 
                    align="around" 
                    class="btn-fixed-width" 
                    color="deep-orange" 
                    label="3층 가기" 
                    icon="lightbulb_outline" 
                />
                <q-btn
                    :to='"/startmone"' 
                    target="_blank"  
                    v-show="explain==='특별전시관'" 
                    align="around" 
                    class="btn-fixed-width" 
                    color="deep-orange" 
                    label="특별전시관" 
                    icon="lightbulb_outline" 
                />
                <q-btn
                    :to='"/guestbook"' 
                    target="_blank"  
                    v-show="explain==='방명록'" 
                    align="around" 
                    class="btn-fixed-width" 
                    color="deep-orange" 
                    label="방명록 가기" 
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
        },
        gotospecial(){
            this.explain = "특별전시관"
        },
        gotoguestbook(){
            this.explain = "방명록"
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

<style lang="scss" scoped>


.layer-container {
    width: 200px;
    height: 1000px;
    position: absolute;
    top: 85%;
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
    // z-index: 1;
    opacity: 0.95;
}

.layer:hover {
  opacity: 1;
  background-color: #2A433B;
//   transform: scale(1.4);
//   z-index: 10;
}

// .blue-layer { /*bottom - blue*/
//     background: rgba(19, 54, 90, 0.8);
//     /*background-image: url('img/teaser.png');*/
//     background-size: cover;
//     background-repeat: no-repeat;
//     background-position: center;
// }


// .green-layer { /*mid - green*/
//     background: rgba(49, 76, 104, 0.8);
//     /*background-image: url('img/22matcha.JPG');*/
//     background-size: cover;
//     background-repeat: no-repeat;
//     background-position: center;
// }

// .red-layer { /*top - red*/
//     background: rgba(181, 207, 231, 0.8);
//     /*background-image: url('img/teaser_banner.png');*/
//     background-size: cover;
//     background-repeat: no-repeat;
//     background-position: center;
// }

.first-layer {
    transform: rotateX(45deg) rotateZ(25deg) translateZ(0);
    background: #696969;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 5;

}

.second-layer {
    transform: rotateX(45deg) rotateZ(25deg) translateZ(50px);
    background:#7D7D7D;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 4;

}

.third-layer {
    transform: rotateX(45deg) rotateZ(25deg) translateZ(100px);
    background:#9E9E9E;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 3;
}

.fourth-layer {
    transform: rotateX(45deg) rotateZ(25deg) translateZ(150px);
    background: #BDBDBD;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 2;
}

.fifth-layer {
    transform: rotateX(45deg) rotateZ(25deg) translateZ(200px);
    background: #D3D3D3;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 1;
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
    font-size: 25px;
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