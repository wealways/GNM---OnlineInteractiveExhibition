import MainPage from '@/views/MainPage.vue'
import GuestBook from '@/views/GuestBook.vue'
import Tutorial from '@/views/Tutorial.vue'
import Mone from '@/views/Monet/Mone.vue'
import StartMonet from '@/views/Monet/StartMonet.vue'


import Klimt from '@/views/Klimt/Klimt.vue'
import StartKlimt from '@/views/Klimt/StartKlimt.vue'
import KlimtEnd from '@/views/Klimt/KlimtEnd.vue'

import Cheon from '@/views/Cheon/Cheon.vue'
import StartCheon from '@/views/Cheon/StartCheon.vue'
import CheonEnd from '@/views/Cheon/CheonEnd.vue'

import test from '@/components/Mone/test.vue'
import Mones from '@/views/Monet/Mones.vue'

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
    path:'/mones',
    name: 'Mones',
    component: Mones,
  },
  {
    path:'/startmonet',
    name: 'StartMonet',
    component: StartMonet,
  },
  {
    path:'/monetphoto',
    name: 'MonetPhoto',
    component: PhotoUpload,
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
    path:'/klimt',
    name: 'Klimt',
    component: Klimt,
  },
  {
    path:'/klimtend',
    name:'KlimtEnd',
    component:KlimtEnd,
  },
  {
    path:'/cheon',
    name: 'Cheon',
    component: Cheon,
  },
  {
    path:'/cheonphoto',
    name: 'CheonPhoto',
    component: PhotoUpload,
  },
  {
    path:'/startcheon',
    name: 'StartCheon',
    component: StartCheon,
  },
  {
    path:'/cheonend',
    name:'CheonEnd',
    component:CheonEnd,
  },
  {
    path:'/test',
    name: 'test',
    component: test
  }
]