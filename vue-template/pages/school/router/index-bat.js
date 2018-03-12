import Vue from 'vue'
import Router from 'vue-router'



Vue.use(Router)

var r = new Router({
  routes: [


    // {
    //   path: '/:id',
    //   name: 'teacher',
    //   component: teacher_list
    // },
    {
      path: '/teacher_list',
      name: 'teacher_list',
      component: function (resovle) {
        require.ensure('../../common-part/teacher-list.vue',resovle)
      }
    },
    {
      path: '/teacher_upload',
      name: 'teacher_upload',
      component:function (resovle) {
        require.ensure('../../common-part/teacher-upload.vue',resovle)
      }
    },
    {
      path: '/teacher_export',
      name: 'teacher_export',
      component: function (resovle) {
        require.ensure('../../common-part/teacher-export.vue',resovle)
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
      path: '/schoolexam2',
      name: 'schoolexam2',
      component:  function (resovle) {
        require.ensure('../../common-part/school-client-exam-list2.vue',resovle)
      }
    }
  ]
})
r.beforeEach(function (to,from,next) {
  next()
})
export  default r
