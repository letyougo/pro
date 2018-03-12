<template>
  <div id="app">
    <div class="top-bar">

     <div class="left">
        <el-tooltip class="item" effect="dark" content="通信地址：海淀区知春里31号，邮政编码:100086" placement="bottom">
          <a href="http://www.hdks.gov.cn/" title="" >
     <img src="/static/img/logo.png" />
        </a>
        </el-tooltip>

      </div>


      <el-dialog title="修改手机号" :visible.sync="forget.visible"
      >
        <el-form class="demo-form-inline"  status-icon size="mini" ref="add_form">

          <el-form-item  >
            <el-row :gutter="2">

              <el-col :span="20">
                <el-input v-model="forget.phone" placeholder="原始新手机号" :disabled="true"></el-input>
              </el-col>
              <el-col :span="4">
                <el-button @click="send_code(forget.phone)">发送验证码</el-button>
              </el-col>
            </el-row>
          </el-form-item>

          <el-form-item>
            <el-input v-model="forget.new_phone" placeholder="新手机号" ></el-input>
          </el-form-item>

          <el-form-item >
            <el-input v-model="forget.code" placeholder="验证码"></el-input>
          </el-form-item>

        </el-form>

      </el-dialog>


        <el-dialog title="设置手机号" :visible.sync="set_d.visible"
        >
          <el-form class="demo-form-inline"  status-icon size="mini" ref="add_form">

            <el-form-item  >
              <el-row :gutter="2">

                <el-col :span="20">
                  <el-input v-model="set_d.phone" placeholder="手机号" ></el-input>
                </el-col>
                <el-col :span="4">
                  <el-button @click="send_code(set_d.phone)">发送验证码</el-button>
                </el-col>
              </el-row>
            </el-form-item>

            <el-form-item>
              <el-input v-model="set_d.code" placeholder="验证码" ></el-input>
            </el-form-item>



          </el-form>


        <span slot="footer" class="dialog-footer">
          <el-button @click="set_d.visible=false" size="mini">取 消</el-button>
          <el-button type="primary" @click="set" size="mini">确 定</el-button>
        </span>
      </el-dialog>


      <div class="right">
        <span style="cursor: pointer" @click="forget.visible=true">欢迎：{{user.name}}</span>
        <a href="/logout/" class="logout">
          <i class="icon iconfont icon-web-quit "></i>
        </a>
      </div>


    </div>
    <el-row>
      <el-col :span="2">
        <el-menu
          :default-active="name"
          class="el-menu-vertical-demo"

        >
            <!--<el-menu-item index="/user" @click="route('user')">-->
              <!--<i class="el-icon-setting"></i>-->
              <!--<span slot="title">用户</span>-->
            <!--</el-menu-item>-->
          <el-menu-item index="/teacher_list" @click="route('/teacher_list?id='+school.id)">
            <i class="el-icon-setting"></i>
            <span slot="title">教师信息</span>
          </el-menu-item>
          <el-menu-item index="/teacher_upload" @click="route('/teacher_upload?id='+school.id)">
            <i class="el-icon-setting"></i>
            <span slot="title">批量操作</span>
          </el-menu-item>
          <el-menu-item index="/schoolexam1" @click="route('/schoolexam1?id='+school.id)">
            <i class="el-icon-setting"></i>
            <span slot="title">考试信息</span>
          </el-menu-item>
          <el-menu-item index="/teacher_export" @click="route('/teacher_export?id='+school.id)">
            <i class="el-icon-setting"></i>
            <span slot="title">数据导出</span>
          </el-menu-item>
          <!--<el-menu-item index="/work" @click="route('work')">-->
            <!--<i class="el-icon-setting"></i>-->
            <!--<span slot="title">劳务信息</span>-->
          <!--</el-menu-item>-->

        </el-menu>
      </el-col>
      <el-col :span="22">
        <div class="content">
          <router-view/>
        </div>

      </el-col>

    </el-row>

  </div>
</template>

<script>
  import request from 'axios'
export default {
  name: 'app',
  data(){
      var name = this.$route.path
    var phone = window.user.phone
      return {
          name,
          school:window.school,
          user:window.user,

        forget:{
          visible:false,
          phone:phone,
          code:'',
          new_phone:phone
        },
        set_d:{
          visible:false,
          phone:phone,
          code:''
        }
      }
  },
  methods:{

  },
  mounted(){
    setTimeout(()=>{
      if(!window.user.phone){

        this.set_d.visible = true
      }
    },2000)
  }
}
</script>

<style scoped>
  body,html{
    width: 100%;
    height: 100%;

  }
  div{
    margin: 0;
    padding: 0;
  }
#app {
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  min-width: 1280px;

}
  .top-bar{
    background:#1ab394 ;
    height: 44x;
    text-align: center;
    color: #ffffff;
    font-size: 30px;
    text-shadow: 10px 10px 4px 4px rgba(0,0,0,0.8);
    position: relative;
    height: 44px;
  }

  .right{
    position: absolute;
    right: 20px;

    top: 0;
    bottom: 0;
    font-size: 14px;
  }
  .logout{
    color: #ffffff;
    font-size: 25px;
    display: inline-block;
    margin-left: 5px;
    text-decoration: none;
  }
   .left{
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    font-size: 14px;
  }
  .left a{
    display: block;
    height: 44px;
  }
  .left span{
    display: block;
    line-height: 22px;
    height: 22px;
    text-align: left;
  }
  .el-menu-item i{
    color: #ffffff
  }
   i{
    font-size: 16px;
    color: #ffffff;
  }
  .content{
    padding: 20px;
    box-sizing: border-box;
  }
</style>
