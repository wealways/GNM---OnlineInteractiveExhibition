import MainPage from '@/views/MainPage.vue'
import GuestBook from '@/views/GuestBook.vue'
import Tutorial from '@/views/Tutorial.vue'
import Mone from '@/views/Mone.vue'
import StartMonet from '@/views/StartMonet.vue'
import StartCheon from '@/views/StartCheon.vue'

import Klimt from '@/views/Klimt/Klimt.vue'
import StartKlimt from '@/views/Klimt/StartKlimt.vue'
import KlimtEnd from '@/views/Klimt/KlimtEnd.vue'

import Cheon from '@/views/Cheon.vue'
import test from '@/components/Mone/test.vue'
import Mones from '@/components/Mone/Mones.vue'
import Mone1 from '@/components/Mone/Mone1.vue'
import Mone2 from '@/components/Mone/Mone2.vue'
import Mone3 from '@/components/Mone/Mone3.vue'
import Mone4 from '@/components/Mone/Mone4.vue'
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
    meta:{ transitionName: 'slide'},
    children:[
      {
        path: 'mone1',
        component: Mone1
      },
      {
        path: 'mone2',
        component: Mone2
      },
      {
        path: 'mone3',
        component: Mone3
      },
      {
        path: 'mone4',
        component: Mone4
      },
    ]
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
    component: Cheon
  },
  {
    path:'/startcheon',
    name: 'StartCheon',
    component: StartCheon,
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