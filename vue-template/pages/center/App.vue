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
                <el-button @click="send_code">发送验证码</el-button>
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




        <span slot="footer" class="dialog-footer">
          <el-button @click="forget.visible=false" size="mini">取 消</el-button>
          <el-button type="primary" @click="update" size="mini">确 定</el-button>
        </span>
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
        <span style="cursor: pointer" >欢迎：{{user.name}}</span>
        <a href="javascript:void(0)" class="logout">
          <el-dropdown @command="handleCommand">
            <i class="el-icon-setting"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="edit"> <i style="color: #6f7180" class="el-icon-edit"/>&nbsp;&nbsp;修改密码</el-dropdown-item>
              <el-dropdown-item command="phone"><i  style="color: #6f7180" class="el-icon-phone"/>&nbsp;&nbsp;修改手机号</el-dropdown-item>
              <el-dropdown-item command="logout"><i  style="color: #6f7180" class="icon iconfont icon-web-quit icon-web-quit"/>&nbsp;&nbsp;退出登陆</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </a>



      </div>
    </div>
    <el-row>
      <el-col :span="2">
        <el-menu
          :default-active="name"
        >
          <el-menu-item index="/school_list" @click="route('/school_list')">
            <i class="el-icon-setting" ></i>
            <span slot="title">学校管理</span>
          </el-menu-item>

          <el-menu-item index="/office_list" @click="route('/office_list')">
            <i class="el-icon-setting"></i>
            <span slot="title">考办管理</span>
          </el-menu-item>
          <!--<el-menu-item index="/shui1" @click="route('/shui1')">-->
            <!--<i class="el-icon-setting"></i>-->
            <!--<span slot="title">合并计税</span>-->
          <!--</el-menu-item>-->

          <el-menu-item index="/center_export" @click="route('/center_export')">
            <i class="el-icon-setting"></i>
            <span slot="title">数据导出</span>
          </el-menu-item>
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
    route(name){
      this.$router.push(name)
    },
    handleCommand(c){
      if(c=='edit'){
        location.href = '/forget/'
      }
      if(c=='phone'){
        this.forget.visible = true
      }
      if(c=='logout'){
        location.href = '/logout/'
      }
    },
    async send_code(phone){

      await request.get('/sendcode/?phone='+phone)
      this.$message({
        type: 'success',
        message: '发送验证码成功'
      });
    },
    async update(){
      var phone = this.forget.phone
      var code = this.forget.code
      var new_phone = this.forget.new_phone
      var res = await request.get('/changephone/',{
        params:{
          phone,
          new_phone,
          code,
          role:'center'
        }
      })

      if(res.data.error){
        this.$message({
          type: 'error',
          message: '验证码有误'
        });
      }else {
        this.forget.phone = this.forget.new_phone
        this.$message({
          type: 'success',
          message: '修改手机号成功'
        });
      }

      location.reload()

    },
    async set(){
      var phone = this.set_d.phone
      var code = this.set_d.code

      var res = await request.get('/setphone/',{
        params:{
          phone,
          code,
          role:'center'
        }
      })

      location.reload()

    }
  },
  mounted(){

  }
}
</script>

<style>
  body,html{
    width: 100%;
    height: 100%;

  }

  .top-bar{
    background:#1ab394 ;
    height: 44px;
    text-align: center;
    color: #ffffff;
    font-size: 30px;
    text-shadow: 10px 10px 4px 4px rgba(0,0,0,0.8);
    position: relative;
  }
  .content{
    padding: 20px;
    box-sizing: border-box;
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
  i{
    font-size: 16px;
    color: #ffffff;
  }
  .el-menu-item i{
    color: #ffffff
  }
</style>
