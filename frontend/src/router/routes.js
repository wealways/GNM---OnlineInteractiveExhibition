import HelloWorld from '@/components/HelloWorld.vue'
import GuestBook from '@/views/GuestBook.vue'

export default [
  {
    path:'/',
    name:'HelloWorld',
    component: HelloWorld,
  },
  {
    path:'/guestbook',
    name: 'GuestBook',
    component: GuestBook,
  }
]