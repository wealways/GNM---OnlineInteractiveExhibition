import MainPage from '@/views/MainPage.vue'
import GuestBook from '@/views/GuestBook.vue'
import Tutorial from '@/views/Tutorial.vue'
import Monet from '@/views/Monet/Mone.vue'
import StartMonet from '@/views/Monet/StartMonet.vue'


import Klimt from '@/views/Klimt/Klimt.vue'
import StartKlimt from '@/views/Klimt/StartKlimt.vue'
import Klimts from '@/views/Klimt/Klimts.vue'

import Cheon from '@/views/Cheon/Cheon.vue'
import StartCheon from '@/views/Cheon/StartCheon.vue'
import CheonEnd from '@/views/Cheon/CheonEnd.vue'

import test from '@/components/Mone/test.vue'
import Monets from '@/views/Monet/Mones.vue'

import PhotoUpload from '@/views/PhotoUpload.vue'


// 특별 전시관
import SpecialGallery from '@/views/SpecialGallery.vue'

import MapPage from '@/views/MapPage.vue'


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
    path:'/monet',
    name: 'Monet',
    component: Monet,
  },
  {
    path:'/monets',
    name: 'Monets',
    component: Monets,
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
    path:'/klimts',
    name:'Klimts',
    component:Klimts,
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
    path:'/cheons',
    name:'Cheons',
    component:CheonEnd,
  },
  {
    path:'/test',
    name: 'test',
    component: test
  },
  // 특별전시관
  {
    path: '/specialgallery',
    name: 'SpecialGallery',
    component: SpecialGallery,
  },
  {
    path:'/mappage',
    name: 'MapPage',
    component: MapPage
  },
]