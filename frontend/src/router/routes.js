import MainPage from '@/views/MainPage.vue'
import GuestBook from '@/views/GuestBook.vue'
import Tutorial from '@/views/Tutorial.vue'
import Mone from '@/views/Mone.vue'
import StartMonet from '@/views/StartMonet.vue'
import StartCheon from '@/views/StartCheon.vue'
import MonetPhoto from '@/components/Mone/MonetPhoto.vue'

import Klimt from '@/views/Klimt/Klimt.vue'
import StartKlimt from '@/views/Klimt/StartKlimt.vue'

import Cheon from '@/views/Cheon.vue'
import Cheons from '@/components/Cheon/Cheons.vue'
import Cheon1 from '@/components/Cheon/Cheon1.vue'
import Cheon2 from '@/components/Cheon/Cheon2.vue'
import Cheon3 from '@/components/Cheon/Cheon3.vue'
import Cheon4 from '@/components/Cheon/Cheon4.vue'
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