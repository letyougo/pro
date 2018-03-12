import Vue from 'vue'
import Router from 'vue-router'

import teacher_list from '../../common-part/teacher-list.vue'

import teacher_upload from '../../common-part/teacher-upload.vue'

import schoolexam1 from '../../common-part/school-client-exam-list1.vue'
import schoolexam2 from '../../common-part/school-client-exam-list2.vue'
import teacherexam from '../../common-part/teacher-exam-list.vue'
import teacher_export from '../../common-part/teacher-export.vue'
Vue.use(Router)

export default new Router({
  routes: [

    {
      path: '/schoolexam1',
      name: 'schoolexam1',
      component: schoolexam1
    },
    // {
    //   path: '/:id',
    //   name: 'teacher',
    //   component: teacher_list
    // },
    {
      path: '/teacher_list',
      name: 'teacher_list',
      component: teacher_list
    },
    {
      path: '/teacher_upload',
      name: 'teacher_upload',
      component: teacher_upload
    },
    {
      path: '/teacher_export',
      name: 'teacher_export',
      component: teacher_export
    },
    {
      path: '/schoolexam2',
      name: 'schoolexam2',
      component: schoolexam2
    },
    {
      path: '/teacherexam',
      name: 'teacherexam',
      component: teacherexam
    },
   
  ]
})
