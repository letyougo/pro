<template>
  <div class="teacher">


    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/teacher_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:'/teacher_list?id='+$route.query.id}">学校管理({{detail.name}})</el-breadcrumb-item>
      <el-breadcrumb-item>老师列表</el-breadcrumb-item>
    </el-breadcrumb>

    <br/>
    <el-form :inline="true" class="demo-form-inline" :loading="loading" size="mini">
      <el-form-item label="姓名">
        <el-input v-model="search" placeholder="筛选" suffix-icon="search"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button-group>
          <el-button  @click="fetch" size="mini">查询</el-button>
          <el-button  @click="add_form.visible=true" size="mini" >增加老师</el-button>
          <el-button  @click="$router.push('/teacher_upload?id='+$route.query.id)" size="mini">批量导入</el-button>
          <el-button  @click="$router.push('/teacher_export?id='+$route.query.id)" size="mini">数据导出</el-button>
          <el-button  @click="$router.push('/schoolexam1?id='+$route.query.id)" size="mini">考试管理</el-button>
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
        <el-table-column prop="name" label="教师姓名"></el-table-column>
   


        <el-table-column prop="idcard"  label="身份证"></el-table-column>
        <el-table-column prop="bankcard"  label="银行卡号"></el-table-column>
        <el-table-column prop="bankinfo"  label="银行信息"></el-table-column>
        <el-table-column prop="phone"  label="电话号码"></el-table-column>
    
        <el-table-column  label="操作" width="195" >
          <template scope="scope">
            <el-button-group>
              <el-button type="danger" @click="remove(scope.row)" size="mini" :disabled="disabled">删除</el-button>
              <el-button @click="open_edit(scope.row)" size="mini" :disabled="disabled">编辑</el-button>
              <el-button @click="$router.push('/teacherexam?id='+scope.row.id)" size="mini" >监考</el-button>

            </el-button-group>

          </template>
        </el-table-column>
      </el-table>

    <br/>



    <el-dialog title="增加老师信息" :visible.sync="add_form.visible" :model="add_form"
    >
      <el-form  label-width="100px" size="mini" :model="add_form" ref="add_form" status-icon>
        <el-form-item prop="name" label="姓名" :rules="rules.no_empty">
          <el-input v-model="add_form.name" placeholder="输入姓名" ></el-input>
        </el-form-item>

        <el-form-item prop="phone" label="电话" >
          <el-input v-model="add_form.phone" placeholder="输入电话" ></el-input>
        </el-form-item>



        <el-form-item label="身份证" prop="idcard" :rules="rules.idcard">
          <el-input v-model="add_form.idcard" placeholder="输入身份证"></el-input>
        </el-form-item>

        <el-form-item label="银行卡号" prop="bankcard" >
          <el-input v-model="add_form.bankcard" placeholder="银行卡号"></el-input>
        </el-form-item>
        <el-form-item label="银行信息">
          <el-input v-model="add_form.bankinfo" placeholder="银行卡号"></el-input>
        </el-form-item>
      </el-form>


        <span slot="footer" class="dialog-footer">
          <el-button @click="add_form.visible=false" size="mini">取 消</el-button>
          <el-button type="primary" @click="add" size="mini">确 定</el-button>
        </span>
    </el-dialog>


    <el-dialog title="编辑老师信息" :visible.sync="edit_form.visible"
    >
      <el-form :model="edit_form" ref="edit_form"  label-width="100px" size="mini" status-icon>


        <el-form-item label="姓名" prop="name" :rules="rules.no_empty">
          <el-input v-model="edit_form.name" placeholder="输入姓名"></el-input>
        </el-form-item>

        <el-form-item label="电话" prop="phone" success-icon>
          <el-input v-model="edit_form.phone" placeholder="输入电话"></el-input>
        </el-form-item>

        <el-form-item label="身份证" prop="idcard" :rules="rules.idcard">
          <el-input v-model="edit_form.idcard" placeholder="输入身份证"></el-input>
        </el-form-item>

        <el-form-item label="银行卡号" prop="bankcard" >
          <el-input v-model="edit_form.bankcard" placeholder="银行卡号"></el-input>
        </el-form-item>
        <el-form-item label="银行信息" prop="bankinfo">
          <el-input v-model="edit_form.bankinfo" placeholder="银行信息"></el-input>
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
  import ElCol from "element-ui/packages/col/src/col";

  import req from 'axios'
  import moment from 'moment'
  import rules from './rules'
  import Promise from 'bluebird'
export default {
  components: {
    ElCol,
    ElButton,
    ElButtonGroup},
  name: 'teacher-info',
  data () {
    return {
      rules:rules,
      detail:{},
      disabled:!window.type.school,
      list:[],
      total:0,
      search:'',
      page_size:10,
      page_num:1,
      loading:false,

      add_form:{
        id:'',
        name:'',
        phone:'',

        idcard:'',
        bankcard:'',
        bankinfo:'',
        visible:false
      },
      edit_form:{
        id:'',
        name:'',
        phone:'',
        idcard:'',
        bankcard:'',
        bankinfo:'',
        visible:false
      },
      upload_dialog:{
        visible:false,
        list:[
          {
            name:'苏瑞',
            phone:'',
            idcard:'11561561',
            bankcard:'',
            bankinfo:'',

          },
          {
            name:'小强',
            phone:'',
            idcard:'15156',
            bankcard:'',
            bankinfo:'',

          }
        ],
        files:[],
        loading:false
      }
    }
  },

  watch:{
      page_num(){
          this.fetch()
      }
  },

  methods:{


    handlePreview(){},
    handleRemove(){},
      change_page(p){
          console.log(p)
      },
//    upload_success(f){
//        console.log(f)
//    },

      teacher_export(){
        var id = this.$route.query.id
        location.href = '/teacherexport?school_id='+id 
      },
      open_edit(data){
          console.log(data)
          data.visible = true
          this.edit_form = {
              visible:true,
              id:data.id,
              name:data.name,
              phone:data.phone,
              bankinfo:data.bankinfo,
              idcard:data.idcard,
              bankcard:data.bankcard,
              school_id:data.school_id
          }
      },
      async fetch(){

        var page_size = this.page_size,
          page_num = this.page_num,
          search = this.search,
          that = this

          this.loading = true

          var response = await request.get('/api/teacher/?school_id='+this.$route.query.id,{
            params:{
              page_size,
              page_num,
              search
            }
          })
          this.list = response.data.objects
          this.list = this.list.map(function (item) {
            item.create_time = moment(item.create_time).format('YYYY-MM-DD')
            item.name = item.name.trim()
            item.bankinfo = item.bankinfo.trim()
            item.bankinfo = item.bankinfo.trim()
            item.phone = item.phone.trim()
            item.idcard = item.idcard.trim()
            return item
          })
        var page  = response.data.page
        this.page_num = page.page_num
        this.page_size = page.page_size
        this.total = page.total
        this.loading = false
      },

      async fetch_school(){
        var id = this.$route.query.id
        var response = await request.get('/api/school/'+id+'/')
        this.detail = response.data
        console.log(response.data)
      },

      async add(){
          try {
            await this.su_validate('add_form')
            var add_form = this.add_form
            add_form.school_id = this.school_id
            var response = await request.post('/api/teacher/',add_form)
            this.fetch()
            this.add_form.visible = false
          }catch (e){
            console.log(e)
            this.$message({
              type: 'error',
              message: e.error
            });
          }

      },



      async send_idcard(){
//        this.$refs.upload.submit();
        var res = await req.get('http://123.56.3.23:8888/func/card')

      },

      async remove(data){
        try {
          await this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
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
        try{
          await this.su_validate('edit_form')
          var edit_form = this.edit_form
          console.log(edit_form)
          var id = edit_form.id

          this.$message({
            type: 'success',
            message: '修改信息成功!'
          });

          var response = await request.put('/api/teacher/'+id +'/',edit_form)
          this.edit_form.visible = false
          this.fetch()

        }catch (e){

          this.$message({
            type: 'error',
            message: e.error
          });
        }

      },

  },
  mounted(){
      this.fetch()
      this.fetch_school()
      console.log(this.ccc,'ccc')
  }


}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
