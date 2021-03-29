import MainPage from '@/views/MainPage.vue'
import GuestBook from '@/views/GuestBook.vue'
import Tutorial from '@/views/Tutorial.vue'
import Mone from '@/views/Mone.vue'
import Klimt from '@/views/Klimt.vue'
import Cheon from '@/views/Cheon.vue'
export default [
  {
    path:'/',
    name:'MainPage',
    component: MainPage,
  },
  {
    path:'/guestbook',
    name: 'GuestBook',
    component: GuestBook,
  },
  {
    path:'/tutorial',
    name: 'Tutorial',
    component: Tutorial,
  },
  {
    path:'/mone',
    name: 'Mone',
    component: Mone,
  },
  {
    path:'/klimt',
    name: 'Klimt',
    component: Klimt,
  },
  {
    path:'/cheon',
    name: 'Cheon',
    component: Cheon
  }

]