import MainPage from '@/views/MainPage.vue'
import GuestBook from '@/views/GuestBook.vue'

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
  }
]