<template>
  <div class="teacher">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>学校列表</el-breadcrumb-item>
    </el-breadcrumb>
    <br/>

    <el-form :inline="true" class="demo-form-inline" :loading="loading" size="mini">
      <el-form-item >
        <el-input v-model="search" placeholder="输入名字查询" size="small"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button-group>
          <el-button type="primary" @click="fetch" size="mini">查询学校</el-button>
          <el-button  @click="add_form.visible=true" size="mini">增加学校</el-button>
        </el-button-group>
      </el-form-item>
         <el-form-item label="全区老师筛选">
             <el-switch
              v-model="teacher_filter.visible"
              active-color="#13ce66"
              inactive-color="#ff4949">
            </el-switch>
      </el-form-item>

      <el-form-item v-if="teacher_filter.visible">
          <el-input placeholder="老师身份证" v-model="teacher_filter.idcard">
          </el-input>
      </el-form-item>

       <el-form-item v-if="teacher_filter.visible">
          <el-input placeholder="老师姓名" v-model="teacher_filter.name" >
          </el-input>
      </el-form-item>
      <el-form-item v-if="teacher_filter.visible">
           <el-button icon="el-icon-search"  type="primary" @click="fetch2" size="mini">查询老师</el-button>
      </el-form-item>
    </el-form>

     <h3 class="list-header" style="text-align:center" v-if="teacher_filter.visible">老师表</h3>
         <el-table
         v-if="teacher_filter.visible"
        :data="list2"
        style="width: 100%"
        border
        size="mini"
        v-loading="teacher_filter.loading"
      >


      <el-table-column  label="序号">
        <template scope="scope">
          {{scope.$index+(page_num-1)*page_size+1}}
        </template>
      </el-table-column>
          <el-table-column prop="school_name" label="所属学校"></el-table-column>
        <el-table-column prop="name" label="姓名"></el-table-column>
   


        <el-table-column prop="idcard"  label="身份证"></el-table-column>
        <el-table-column prop="bankcard"  label="银行卡号"></el-table-column>
        <el-table-column prop="bankinfo"  label="银行信息"></el-table-column>
        <el-table-column prop="phone"  label="电话"></el-table-column>
    
        <el-table-column  label="操作" width="135" >
          <template scope="scope">
            <el-button-group>
              <el-button type="danger" @click="remove2(scope.row)" size="mini" >删除</el-button>
             
            </el-button-group>

          </template>
        </el-table-column>
      </el-table>
      <br v-if="teacher_filter.visible">

      <h3 class="list-header"  style="text-align:center">学校表</h3>

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
        <el-table-column prop="name" label="学校名字"></el-table-column>
        <el-table-column prop="admin_name" label="管理员姓名"></el-table-column>
        <el-table-column prop="admin_phone" label="管理员手机号码"></el-table-column>
        <el-table-column prop="register_username" label="登录名"></el-table-column>


        <el-table-column  label="操作" width="190" >
          <template scope="scope">
            <el-button-group>
              <el-button  @click="remove(scope.row)" size="mini" type="warning">删除</el-button>
              <el-button @click="open_edit(scope.row)" size="mini">编辑</el-button>
              <el-button @click="$router.push('/teacher_list?id='+scope.row.id)" size="mini">详情</el-button>
              <!--<el-button @click="$router.push('/schoolexam1?id='+scope.row.id)" size="mini">考试</el-button>-->
            </el-button-group>

          </template>
        </el-table-column>
      </el-table>


    <el-dialog title="增加老师信息" :visible.sync="add_form.visible"
    >
      <el-form class="demo-form-inline" label-width="100px">
        <el-form-item label="学校名字">
          <el-input v-model="add_form.name" placeholder="输入名字"></el-input>
        </el-form-item>

        <el-form-item label="管理员名字">
          <el-input v-model="add_form.admin_name" placeholder="输入管理员姓名"></el-input>
        </el-form-item>

        <el-form-item label="管理员电话">
          <el-input v-model="add_form.admin_phone" placeholder="输入管理员电话"></el-input>
        </el-form-item>

        <el-form-item label="注册用户名">
          <el-input v-model="add_form.register_username" placeholder="输入用户名"></el-input>
        </el-form-item>



        <el-form-item label="注册密码">
          <el-input v-model="add_form.register_password" placeholder="输入密码"></el-input>
        </el-form-item>

      </el-form>


        <span slot="footer" class="dialog-footer">
          <el-button @click="add_form.visible=false" size="small">取 消</el-button>
          <el-button type="primary" @click="add" size="small">确 定</el-button>
        </span>
    </el-dialog>


    <el-dialog title="编辑老师信息" :visible.sync="edit_form.visible"
    >
      <el-form class="demo-form-inline"  label-width="100px">


        <el-form-item label="学校名字">
          <el-input v-model="edit_form.name" placeholder="输入名字"></el-input>
        </el-form-item>
        <el-form-item label="管理员名字">
          <el-input v-model="edit_form.admin_name" placeholder="输入管理员姓名"></el-input>
        </el-form-item>

        <el-form-item label="管理员电话">
          <el-input v-model="edit_form.admin_phone" placeholder="输入管理员电话"></el-input>
        </el-form-item>

        <el-form-item label="注册用户名">
          <el-input v-model="edit_form.register_username" placeholder="输入用户名"></el-input>
        </el-form-item>



        <el-form-item label="是否修改密码">
          <el-switch
            v-model="edit_form.change_password"
            active-color="#13ce66"
            inactive-color="#ff4949">
          </el-switch>
        </el-form-item>

        <el-form-item label="注册密码" v-if="edit_form.change_password">
          <el-input v-model="edit_form.register_password" placeholder="输入密码"></el-input>
        </el-form-item>


      </el-form>


      <span slot="footer" class="dialog-footer">
          <el-button @click="edit_form.visible=false">取 消</el-button>
          <el-button type="primary" @click="edit">确 定</el-button>
        </span>
    </el-dialog>

    <br/>

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
  import moment from 'moment'
export default {
  components: {
    ElForm,
    ElButton,
    ElButtonGroup},
  name: 'school',
  data () {
    return {
      school_id:window.school_id,
      list:[],
      list2:[],
      search:'',
      page_size:10,
      page_num:1,
      total:1,
      loading:false,
      teacher_filter:{
        visible:false,
        name:'',
        idcard:'',
        loading:false
      },
      add_form:{
        name:'',
        register_username:"",
        register_password:'',
        visible:false,
        admin_name:'',
        admin_phone:''
      },
      edit_form:{
        id:'',
        name:'',
        register_userid:'',
        register_username:'',
        register_password:'',
        visible:false,
        admin_name:'',
        admin_phone:'',
        change_password:false
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
              name:data.name,
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
          console.log(window.school,'window.school')
          var response = await request.get('/api/school/',{
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

      async fetch2(){

        var 
          name = this.teacher_filter.name,
          idcard = this.teacher_filter.idcard,
          that = this

      
          this.teacher_filter.loading = true 
          var response = await request.get('/api/teacher/',{
            params:{
              name,
              idcard
            }
          })
          this.teacher_filter.loading = false 
          this.list2 = response.data.objects.map(function (item) {
            item.create_time = moment(item.create_time).format('YYYY-MM-DD')
            return item
          })
  
        
      
      },
      async add(){
          var add_form = this.add_form

          console.log(add_form,'----')

          var response = await request.post('/api/school/',add_form)
          this.add_form.visible = false
          this.fetch()

      },
      async remove(data){
        try {
          await this.$confirm('此操作将永久删除该数据, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          })
          var response = await request.delete('/api/school/'+data.id+'/')

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


      async remove2(data){
        try {
          await this.$confirm('此操作将永久删除该数据, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          })
          var response = await request.delete('/api/teacher/'+data.id+'/')

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
        var edit_form = this.edit_form
        console.log(edit_form)
        var id = edit_form.id



        this.$message({
          type: 'success',
          message: '修改信息成功!'
        });

        console.log()

        var response = await request.put('/api/school/'+id +'/',edit_form)
        this.edit_form.visible = false
        this.fetch()
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
