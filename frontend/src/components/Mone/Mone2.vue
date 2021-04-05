<template>
  <div class='monepage2'>
      <h1 class=desc>description2</h1>
  </div>
</template>

<script>
import { gsap } from 'gsap';
// import $ from 'jquery';
export default {
    name:"Mone2",
    mounted(){
			var Counter = 0;
			function myFunction() {
				Counter = Math.ceil(window.scrollY);
			}
			window.onscroll = () => {
					myFunction();
					if (Counter > 0){
						if (this.$route.path === '/mones/mone2') {
							this.changerouter()
						}
					}
					console.log(Counter)
			};


			let t1 = gsap.timeline();
			t1.from(
			".desc",
			{
				yPercent: 100,
				ease: "power1.out",
				opacity: 0,
			},
			);
    },
    methods:{
        changerouter(){
            this.$router.push({path:'/mones/mone3'})
        },
    }
}
</script>

<style>
.monepage2{
    width: 101vw;
    height: 101vh;
    background: url("../../assets/insang.jpg") no-repeat
}
</style>