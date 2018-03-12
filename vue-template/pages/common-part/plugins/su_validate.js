var a = {
  install:function(Vue){
    function su_validate(formName){
      var that = this
      return new Promise(function (resovle, reject) {
        that.$refs[formName].validate(function (valid) {
          if (valid) {
            resovle()
          } else {
            reject({
              error:'输入数据有误'
            })
          }
        });
      })
    }
    Vue.prototype.su_validate =su_validate
    Vue.su_validate = su_validate
    // Vue.mixin({
    //   // 添加到mixin中的任何内容将被注入到所有组件中。
    //   //在这个例子中， mounted() 方法将在组件被挂载到DOM后调用
    //   mounted() {
    //     console.log('Mounted!');
    //   }
    // });


  }
}

module.exports = a
