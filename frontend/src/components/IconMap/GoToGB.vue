<template>
  <a href="/guestbook">
    <div class="flex" :to="'/guestbook'">
      <span>GUEST<br></span>
      <span>BOOK</span>
    </div>
  </a>
</template>

<script>
export default {
  name:'GoToTutorial',
}
</script>

<style scoped>

div {
  margin: 100px auto;
  width: 100px;
  height: 100px;
  padding: 33px 0;
  line-height: 20px;
  text-align: center;
  display: block;
  position: relative;
  z-index: 10;
  cursor: pointer;
  font-weight: 700;
  font-size: 17px;
  line-height: 20px;
}

div:before {
  content: '';
  position: absolute;
  z-index: -1;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  background: #ccc;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  transition: .3s ease;
  
  box-shadow: 
  3px 3px 0 0 #999, 6px 6px 0 0 #777, 9px 9px 0 0 #555, 12px 12px 0 0 #333;
}

div:hover:before {
  background: #FCF9F2;
  color:#2A433B;
  box-shadow: 
 9px 9px 0 0 #F0D4A1, 18px 18px 0 0 #D7B577, 27px 27px 0 0 #A3702B, 36px 36px 0 0 #6B3407;
}


span {
  color:#343F51;
  font-family: 'Montserrat';
}

a {
  text-decoration:none; 
}



</style>