<template>
  <div class="teacher">

    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>考试办列表</el-breadcrumb-item>

    </el-breadcrumb>
    <br/>


    <el-form :inline="true" class="demo-form-inline" :loading="loading" size="mini">

      <el-form-item label="姓名">
        <el-input v-model="search" placeholder="输入姓名查询"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button-group>
          <el-button type="primary" @click="fetch" size="mini">查询</el-button>
          <el-button  @click="add_form.visible=true" size="mini">增加考试办</el-button>

        </el-button-group>
      </el-form-item>

    </el-form>


    <el-table
      :data="list"
      style="width: 100%"
      border
      size="mini"
      v-loading="loading"
    >


      <el-table-column  label="序号">
        <template scope="scope">
          {{scope.$index+(page_num-1)*page_size+1}}
        </template>
      </el-table-column>
      <el-table-column prop="office_name" label="所属科室"></el-table-column>
      <el-table-column prop="exam_name" label="考试名称"></el-table-column>
      <el-table-column prop="admin_name" label="学校管理员姓名"></el-table-column>
      <el-table-column prop="admin_phone" label="学校管理员电话"></el-table-column>
      <el-table-column prop="register_username" label="注册用户名"></el-table-column>


      <el-table-column  label="操作" width="190" >
        <template scope="scope">
          <el-button-group>
            <el-button type="danger" @click="remove(scope.row)" size="mini">删除</el-button>
            <el-button @click="open_edit(scope.row)" size="mini">编辑</el-button>
            <el-button @click="$router.push('/officeexam1?id='+scope.row.id)" size="mini">详情</el-button>
          </el-button-group>

        </template>
      </el-table-column>
    </el-table>


    <el-dialog title="增加办公室信息" :visible.sync="add_form.visible"
    >
      <el-form class="demo-form-inline" label-width="100px"  :model="add_form" status-icon size="mini" ref="add_form">
        <el-form-item label="办公室名字" prop="office_name" :rules="rules.no_empty">
          <el-input v-model="add_form.office_name" placeholder="办公室名字"></el-input>
        </el-form-item>

        <el-form-item label="负责考试">
          <el-input v-model="add_form.exam_name" placeholder="负责考试"></el-input>
        </el-form-item>

        <el-form-item label="管理员名字" prop="admin_name" :rules="rules.no_empty">
          <el-input v-model="add_form.admin_name" placeholder="输入管理员姓名"></el-input>
        </el-form-item>

        <el-form-item label="管理员电话" prop="admin_phone" :rules="rules.phone">
          <el-input v-model="add_form.admin_phone" placeholder="输入管理员电话"></el-input>
        </el-form-item>

        <el-form-item label="注册用户名" prop="register_username" :rules="rules.no_empty">
          <el-input v-model="add_form.register_username" placeholder="输入用户名"></el-input>
        </el-form-item>

        <el-form-item label="注册密码"  >
          <el-input v-model="add_form.register_password" placeholder="输入密码"></el-input>
        </el-form-item>

      </el-form>


      <span slot="footer" class="dialog-footer">
          <el-button @click="add_form.visible=false" size="mini">取 消</el-button>
          <el-button type="primary" @click="add" size="mini">确 定</el-button>
        </span>
    </el-dialog>


    <el-dialog title="编辑办公室信息" :visible.sync="edit_form.visible"
    >
      <el-form class="demo-form-inline"  label-width="100px" :model="edit_form" status-icon size="mini" ref="edit_form">


        <el-form-item label="办公室名字" prop="office_name" :rules="rules.no_empty">
          <el-input v-model="edit_form.office_name" placeholder="办公室名字"></el-input>
        </el-form-item>

        <el-form-item label="负责考试" prop="exam_name" :rules="rules.no_empty">
          <el-input v-model="edit_form.exam_name" placeholder="负责考试"></el-input>
        </el-form-item>

        <el-form-item label="管理员名字" prop="exam_name" :rules="rules.no_empty">
          <el-input v-model="edit_form.admin_name" placeholder="输入管理员姓名"></el-input>
        </el-form-item>

        <el-form-item label="管理员电话" prop="admin_phone" :rules="rules.phone">
          <el-input v-model="edit_form.admin_phone" placeholder="输入管理员电话"></el-input>
        </el-form-item>

        <el-form-item label="注册用户名" prop="register_username" :rules="rules.no_empty">
          <el-input v-model="edit_form.register_username" placeholder="输入用户名"></el-input>
        </el-form-item>




        <el-form-item label="是否修改密码">
          <el-switch
            v-model="edit_form.change_password"
            active-color="#13ce66"
            inactive-color="#ff4949">
          </el-switch>
        </el-form-item>

        <el-form-item label="注册密码" v-if="edit_form.change_password" >
          <el-input v-model="edit_form.register_password" placeholder="输入密码"></el-input>
        </el-form-item>


      </el-form>





      <span slot="footer" class="dialog-footer">
          <el-button @click="edit_form.visible=false" size="mini">取 消</el-button>
          <el-button type="primary" @click="edit" size="mini">确 定</el-button>
        </span>
    </el-dialog>





    <br>
    <div style="display: inline-block;float: right">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="total"
        @current-change="(p)=>page_num=p"
        :current-page="page_num"
        :page-size="page_size"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>

  import ElButtonGroup from "../../node_modules/element-ui/packages/button/src/button-group.vue";
  import request from './config'
  import ElButton from "../../node_modules/element-ui/packages/button/src/button.vue";
  import ElForm from "../../node_modules/element-ui/packages/form/src/form.vue";
  import rules from './rules'
  import Promise from 'bluebird'
  export default {
    components: {
      ElForm,
      ElButton,
      ElButtonGroup},
    name: 'office',
    data () {
      return {
        rules:rules,
        list:[],
        total:0,
        search:'',
        page_size:10,
        page_num:1,
        loading:false,
        add_form:{
          office_name:'',
          exam_name:'',
          register_username:"",
          register_password:'',
          visible:false,
          admin_name:'',
          admin_phone:''

        },
        edit_form:{
          id:'',
          office_name:'',
          exam_name:'',
          register_userid:'',
          register_username:'',
          register_password:'',
          visible:false,
          change_password:false,
          admin_name:'',
          admin_phone:''
        },
        upload_dialog:{
          visible:false
        }
      }
    },

    watch:{
      page_num(){
        this.fetch()
      }
    },

    methods:{
      change_page(p){
        console.log(p)
      },
      open_edit(data){
        console.log(data)
        var change_password=this.edit_form.change_password
        data.visible = true
        this.edit_form = {
          visible:true,
          id:data.id,
          office_name:data.office_name,
          exam_name:data.exam_name,
          register_userid:data.register_userid,
          register_username:data.register_username,
          register_password:data.register_password,
          change_password:change_password,
          admin_name:data.admin_name,
          admin_phone:data.admin_phone
        }
      },
      async fetch(){

        var page_size = this.page_size,
          page_num = this.page_num,
          search = this.search,
          that = this

        this.loading = true

        var response = await request.get('/api/office/',{
          params:{
            page_size,
            page_num,
            search
          }
        })
        this.list = response.data.objects
        var page  = response.data.page
        this.page_num = page.page_num
        this.page_size = page.page_size
        this.total = page.total
        this.loading = false
      },
      async add(){

        try{
          await this.su_validate('add_form')
          var add_form = this.add_form
          var response = await request.post('/api/office/',add_form)
          this.add_form.visible = false
          this.$message({
            type: 'success',
            message: '添加数据成功'
          });
          this.fetch()
        }catch (e){
          console.log(e)
          this.$message({
            type: 'error',
            message: e.error
          });
        }

      },
      async remove(data){

        try {
          await this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          })
          var response = await request.delete('/api/office/'+data.id+'/')

          this.$message({
            type: 'success',
            message: '删除成功!'
          });
          this.fetch()
        }catch (e){
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        }

      },
      async edit(){
        try{
          await this.su_validate('edit_form')
          var edit_form = this.edit_form
          console.log(edit_form)
          var id = edit_form.id



          this.$message({
            type: 'success',
            message: '修改信息成功!'
          });



          var response = await request.put('/api/office/'+id +'/',edit_form)
          this.edit_form.visible = false
          this.fetch()
        }catch (e){
          this.$message({
            type: 'error',
            message: e.error
          });
        }



      }
    },
    mounted(){

      this.fetch()
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style >

</style>
