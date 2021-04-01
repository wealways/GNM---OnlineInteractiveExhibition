import MainPage from '@/views/MainPage.vue'
import GuestBook from '@/views/GuestBook.vue'
import Tutorial from '@/views/Tutorial.vue'
import Mone from '@/views/Mone.vue'
import Klimt from '@/views/Klimt.vue'
import Cheon from '@/views/Cheon.vue'
import StartMonet from '@/views/StartMonet.vue'
import StartKlimt from '@/views/StartKlimt.vue'
import MonetPhoto from '@/components/Mone/MonetPhoto.vue'
import test from '@/components/Mone/test.vue'
import PhotoUpload from '@/views/PhotoUpload.vue'

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
    path:'/startmonet',
    name: 'StartMonet',
    component: StartMonet,
  },
  {
    path:'/monetphoto',
    name: 'MonetPhoto',
    component: MonetPhoto,
  },
  {
    path:'/klimt',
    name: 'Klimt',
    component: Klimt,
  },
  {
    path:'/startklimt',
    name: 'StartKlimt',
    component: StartKlimt,
  },
  {
    path:'/klimtphoto',
    name: 'KlimtPhoto',
    component: PhotoUpload,
  },
  {
    path:'/cheon',
    name: 'Cheon',
    component: Cheon
  },
  {
    path:'/cheonphoto',
    name: 'CheonPhoto',
    component: PhotoUpload,
  },
  {
    path:'/test',
    name: 'test',
    component: test
  }

]