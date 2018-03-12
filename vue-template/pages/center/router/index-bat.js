import Vue from 'vue'
import Router from 'vue-router'



Vue.use(Router)



import teacher_list from '../../common-part/teacher-list.vue'

import teacher_upload from '../../common-part/teacher-upload.vue'
import teacher_export from '../../common-part/teacher-export.vue'
import schoolexam1 from '../../common-part/school-client-exam-list1.vue'
import schoolexam2 from '../../common-part/school-client-exam-list2.vue'

var r = new Router({
  routes: [

    {
      path: '/center_export',
      name: 'center_export',
      component: function (resovle) {
        require.ensure('../../common-part/center-export.vue',resovle)
      }
    },

    //学校部分
    {
      path: '/',
      name: '',
      component: function (resovle) {
        require.ensure('../../common-part/school-list.vue',resovle)
      }
    },
    {
      path: '/school_list',
      name: 'school_list',
      component: function (resovle) {
        require.ensure('../../common-part/school-list.vue',resovle)
      }
    },

    {
      path: '/schoolexam1',
      name: 'schoolexam1',
      component: function (resovle) {
        require.ensure('../../common-part/school-client-exam-list1.vue',resovle)
      }
    },

    {
      path: '/teacher_list',
      name: 'teacher_list',
      component: function (resovle) {
        require.ensure(  '../../common-part/teacher-list.vue',resovle)
      }
    },
    {
      path: '/teacher_upload',
      name: 'teacher_upload',
      component: function (resovle) {
        require.ensure(  '../../common-part/teacher-upload.vue',resovle)
      }
    },
    {
      path: '/teacher_export',
      name: 'teacher_export',
      component: function (resovle) {
        require.ensure(  '../../common-part/teacher-export.vue',resovle)
      }
    },
    {
      path: '/schoolexam2',
      name: 'schoolexam2',
      component: function (resovle) {
        require.ensure('../../common-part/school-client-exam-list2.vue',resovle)
      }
    },
    //考办部分

    {
      path: '/office_list',
      name: 'office_list',
      component: function (resovle) {
        require.ensure('../../common-part/office-list.vue',resovle)
      }
    },

    {
      path: '/officeexam1',
      name: 'officeexam1',
      component: function (resovle) {
        require.ensure('../../common-part/office-client-exam-list1.vue',resovle)
      }
    },
    {
      path: '/officeexam2',
      name: 'officeexam2',
      component: function (resovle) {
        require.ensure('../../common-part/office-client-exam-list2.vue',resovle)
      }
    },
    {
      path: '/office_export',
      name: 'office_export',
      component: function (resovle) {
        require.ensure('../../common-part/office-export.vue',resovle)
      }
    },
  ]
})
r.beforeEach(function (to,from,next) {
  next()
})
export  default r
