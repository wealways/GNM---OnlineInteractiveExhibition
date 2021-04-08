<template>
  <div class="flex">
    <a href="#" class="btn-default">
      <span>방명록</span>
    </a>
  </div>
</template>

<script>
export default {
  name:'GoToTutorial',
}
</script>

<style scoped>


body
{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-width: 100vw;
  min-height: 100vh;
  background: #F5F5F5;
}

.btn-default
{
  --btn-size: 6rem;
  position: relative;
  display: flex;
  text-decoration:none;
  font-size: 18px;
  justify-content: center;
  align-items: center;
  width: var(--btn-size);
  height: var(--btn-size);
  border-radius: 20px;
  background: rgb(211, 127, 127);
  color: #f5f5f5;

  transform: rotate( 45deg );
}


.btn-default:hover {
  color: #FFF;
  transition-duration: 0.3s;
  background-color: rgb(216, 101, 101);
  text-decoration: none; 
}
 
  
.btn-default span {
    position: relative;
    z-index: 10;
    transform: rotate( -45deg );
    
}


</style>