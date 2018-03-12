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
        >
          <el-menu-item index="/school_list" @click="route('/school_list')">
            <i class="el-icon-setting"></i>
            <span slot="title">学校管理</span>
          </el-menu-item>
          <el-menu-item index="/" @click="route('/?id='+office.id)">
            <i class="el-icon-setting"></i>
            <span slot="title">考试管理</span>
          </el-menu-item>
          <el-menu-item index="/office_export" @click="route('/office_export?id='+office.id)">
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
  export default {
    name: 'app',
    data(){
      var name = this.$route.path
      var phone = window.user.phone
      return {
        name,
        office:window.office,
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
            role:'office'
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
            role:'office'
          }
        })

        location.reload()

      }
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
</style>
