webpackJsonp([17],{"+W/d":function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o=n("7+uW"),a=n("OjuS"),i=n("HDqj"),c=n("zL8q"),s=n.n(c),l=n("Xcu2"),u=(n.n(l),n("0/Ll"));n.n(u);o.default.use(s.a),o.default.config.productionTip=!1;var r=n("onP2");o.default.use(r),new o.default({el:"#app",router:i.a,template:"<App/>",components:{App:a.a}})},"0/Ll":function(t,e){},"0vQM":function(t,e,n){"use strict";var o=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("div",{staticClass:"top-bar"},[n("div",[t._v("考试管理系统-考试办")]),t._v(" "),n("div",{staticClass:"right"},[n("span",[t._v("欢迎："+t._s(t.user.name))]),t._v(" "),t._m(0,!1,!1)])]),t._v(" "),n("el-row",[n("el-col",{attrs:{span:2}},[n("el-menu",{attrs:{"default-active":t.name}},[n("el-menu-item",{attrs:{index:"/school_list"},on:{click:function(e){t.route("/school_list")}}},[n("i",{staticClass:"el-icon-setting"}),t._v(" "),n("span",{attrs:{slot:"title"},slot:"title"},[t._v("学校管理")])]),t._v(" "),n("el-menu-item",{attrs:{index:"/"},on:{click:function(e){t.route("/?id="+t.office.id)}}},[n("i",{staticClass:"el-icon-setting"}),t._v(" "),n("span",{attrs:{slot:"title"},slot:"title"},[t._v("考试管理")])]),t._v(" "),n("el-menu-item",{attrs:{index:"/data"},on:{click:function(e){t.route("/data?id="+t.office.id)}}},[n("i",{staticClass:"el-icon-setting"}),t._v(" "),n("span",{attrs:{slot:"title"},slot:"title"},[t._v("数据导出")])])],1)],1),t._v(" "),n("el-col",{attrs:{span:22}},[n("div",{staticClass:"content"},[n("router-view")],1)])],1)],1)},a=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("a",{staticClass:"logout",attrs:{href:"/logout/"}},[n("i",{staticClass:"icon iconfont icon-web-quit "})])}],i={render:o,staticRenderFns:a};e.a=i},F9f9:function(t,e,n){"use strict";e.a={name:"app",data:function(){return{name:this.$route.path,office:window.office,user:window.user}},methods:{route:function(t){this.$router.push(t)}}}},HDqj:function(t,e,n){"use strict";var o=n("7+uW"),a=n("/ocq");o.default.use(a.a),e.a=new a.a({routes:[{path:"/",name:"",component:function(t){n.e(6).then(t.bind(null,n)).catch(n.oe)}},{path:"/officeexam1",name:"officeexam1",component:function(t){n.e(6).then(t.bind(null,n)).catch(n.oe)}},{path:"/officeexam2",name:"officeexam2",component:function(t){n.e(9).then(t.bind(null,n)).catch(n.oe)}},{path:"/data",name:"data",component:function(t){n.e(7).then(t.bind(null,n)).catch(n.oe)}},{path:"/school_list",name:"school_list",component:function(t){n.e(8).then(t.bind(null,n)).catch(n.oe)}},{path:"/schoolexam1",name:"schoolexam1",component:function(t){n.e(3).then(t.bind(null,n)).catch(n.oe)}},{path:"/teacher_list",name:"teacher_list",component:function(t){n.e(1).then(t.bind(null,n)).catch(n.oe)}},{path:"/teacher_upload",name:"teacher_upload",component:function(t){n.e(2).then(t.bind(null,n)).catch(n.oe)}},{path:"/teacher_export",name:"teacher_export",component:function(t){n.e(0).then(t.bind(null,n)).catch(n.oe)}},{path:"/schoolexam2",name:"schoolexam2",component:function(t){n.e(4).then(t.bind(null,n)).catch(n.oe)}}]})},OjuS:function(t,e,n){"use strict";function o(t){n("vYzd")}var a=n("F9f9"),i=n("0vQM"),c=n("VU/8"),s=o,l=c(a.a,i.a,!1,s,"data-v-2f81c7d8",null);e.a=l.exports},Xcu2:function(t,e){},onP2:function(t,e){var n={install:function(t){function e(t){var e=this;return new Promise(function(n,o){e.$refs[t].validate(function(t){t?n():o({error:"输入数据有误"})})})}t.prototype.su_validate=e,t.su_validate=e}};t.exports=n},vYzd:function(t,e){}},["+W/d"]);
//# sourceMappingURL=office.js.map