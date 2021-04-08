<template>
  <div class="flex">
    <a href="#0" class="bttn" style="font-size:15px;font-family:'Montserrat'">Go To<br>Tutorial<span><img src="@/assets/favicon-32x32.png" alt="" width="18px" height="18px" style="margin-top:5px;"></span></a>
  </div>
</template>

<script>
export default {
  name:'GoToTutorial',
}
</script>

<style scoped>
a {
  color: #333;
  text-decoration: none;
  transition: 0.3s all ease;
}
a:hover {
  color: #999144e1;
}
a:focus {
  text-decoration: none;
}
a:active {
  color: #FFF;
}

body {
  padding: 0;
  margin: 0;
  font-family: "Source Sans Pro", sans-serif;
  background: #F4F5EE;
  -webkit-font-smoothing: antialiased;
}

.flex {
  /* min-height: 100vh; */
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 500;
}

.bttn {
  width: 100px;
  height: 100px;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: bold;
  position: relative;
  display: flex; 
  flex-direction: column;
  align-items: center; 
  justify-content: center; 
}
.bttn:after {
  transition: 0.3s all ease;
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  border: 1px solid #81785a;
  background: white; 
  z-index: -1
   
}
.bttn:before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  border: 1px solid #81785a;

  z-index: -1;
}
.bttn:hover:after {
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
}
.bttn:active {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
.bttn:active:before {
  background-color: #f1481b;
}
.bttn:active:after {
  border-color: #f1481b;
}
</style>