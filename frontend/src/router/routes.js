import MainPage from '@/views/MainPage.vue'
import GuestBook from '@/views/GuestBook.vue'
import Tutorial from '@/views/Tutorial.vue'
import Mone from '@/views/Monet/Mone.vue'
import StartMonet from '@/views/Monet/StartMonet.vue'
import StartCheon from '@/views/StartCheon.vue'

import Klimt from '@/views/Klimt/Klimt.vue'
import StartKlimt from '@/views/Klimt/StartKlimt.vue'
import KlimtEnd from '@/views/Klimt/KlimtEnd.vue'

import Cheon from '@/views/Cheon.vue'
import Cheons from '@/components/Cheon/Cheons.vue'
import Cheon1 from '@/components/Cheon/Cheon1.vue'
import Cheon2 from '@/components/Cheon/Cheon2.vue'
import Cheon3 from '@/components/Cheon/Cheon3.vue'
import Cheon4 from '@/components/Cheon/Cheon4.vue'
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
    path:'/cheons',
    name: 'Cheons',
    component: Cheons,
    mata:{ transitionName: 'slide'},
    children: [
      {
        path: 'cheon1',
        component: Cheon1
      },
      {
        path: 'cheon2',
        component: Cheon2
      },
      {
        path: 'cheon3',
        component: Cheon3
      },
      {
        path: 'cheon4',
        component: Cheon4
      },
    ]
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