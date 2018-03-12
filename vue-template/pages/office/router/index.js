import Vue from 'vue'
import Router from 'vue-router'

import officeexam1 from '../../common-part/office-client-exam-list1.vue'
import officeexam2 from '../../common-part/office-client-exam-list2.vue'
import data from '../../common-part/office-export.vue'
import school_list from '../../common-part/school-list.vue'




import teacher_list from '../../common-part/teacher-list.vue'
import teacherexam from '../../common-part/teacher-exam-list.vue'
import teacher_upload from '../../common-part/teacher-upload.vue'
import teacher_export from '../../common-part/teacher-export.vue'
import schoolexam1 from '../../common-part/school-client-exam-list1.vue'
import schoolexam2 from '../../common-part/school-client-exam-list2.vue'
Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: '',
      component: officeexam1
    },

    {
      path: '/officeexam1',
      name: 'officeexam1',
      component: officeexam1
    },
    {
      path: '/officeexam2',
      name: 'officeexam2',
      component: officeexam2
    },
    {
      path: '/office_export',
      name: 'office_export',
      component: data
    },


    //学校部分
    {
      path: '/school_list',
      name: 'school_list',
      component: school_list
    },
    {
      path: '/schoolexam1',
      name: 'schoolexam1',
      component: schoolexam1
    },

    {
      path: '/teacher_list',
      name: 'teacher_list',
      component: teacher_list
    },
    {
      path: '/teacherexam',
      name: 'teacherexam',
      component: teacherexam
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
  ]
})
