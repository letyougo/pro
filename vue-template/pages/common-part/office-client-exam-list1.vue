<template>
  <div class="offfice">

    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:'/office_list?id='+$route.query.id}">考试办管理({{detail.office_name}})</el-breadcrumb-item>
      <el-breadcrumb-item>考试列表</el-breadcrumb-item>
    </el-breadcrumb>
    <!--<h5>   总计{{total}}条数据</h5>-->

    <br/>

    <el-form :inline="true" class="demo-form-inline" :loading="loading" size="mini">


      <el-form-item label="姓名">
        <el-input v-model="search" placeholder="输入姓名查询" ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button-group>
          <el-button type="primary" @click="fetch" size="mini">查询</el-button>
          <el-button  @click="add_form.visible=true" size="mini" :disabled="disabled">增加考试</el-button>
          <el-button  @click="$router.push('/office_export?id='+$route.query.id)" size="mini">数据导出</el-button>
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
      <el-table-column prop="total" label="应发金额"></el-table-column>
      <el-table-column prop="desc"  label="考试名称"></el-table-column>


      <el-table-column prop="time"  label="发放时间"></el-table-column>
      <el-table-column   label="锁表" width="100">
        <template scope="scope">

          <el-tag v-if="scope.row.lock " size="mini">不可编辑</el-tag>
          <el-tag v-else size="mini" type="danger">可编辑</el-tag>
        </template>
      </el-table-column>
      <el-table-column   label="录入状态" width="80">
        <template scope="scope">

          <el-tag v-if="scope.row.status =='pass' " size="mini">通过</el-tag>
          <el-tag v-if="scope.row.status =='uncheck' "size="mini" type="danger">未通过</el-tag>
        </template>
      </el-table-column>
 
      <el-table-column  label="操作"  width="213">
        <template scope="scope">
          <el-button-group>
            <el-button type="danger" @click="remove(scope.row)" size="mini" :disabled="disabled">删除</el-button>
            <el-button @click="open_edit(scope.row,scope)" size="mini" :disabled="disabled">编辑</el-button>
            <el-button :disabled="scope.row.lack" @click="$router.push('/officeexam2?id='+scope.row.id)" size="mini">考点分配</el-button>
          </el-button-group>

        </template>
      </el-table-column>
    </el-table>


    <el-dialog title="增加考试信息" :visible.sync="add_form.visible"
    >
      <el-form class="demo-form-inline" label-width="100px" size="mini">


        <el-form-item label="总监考费">
          <el-input v-model="add_form.total" placeholder="监考费"></el-input>
        </el-form-item>



        <el-form-item label="输入时间">
          <el-date-picker
            v-model="add_form.time"
            align="right"
            type="date"
            placeholder="选择日期"
            format="yyyy-MM-dd"
           >
          </el-date-picker>


        </el-form-item>

        <el-form-item label="考试名称">
          <el-input   v-model="add_form.desc" placeholder="输入描述"></el-input>
        </el-form-item>


      </el-form>


      <span slot="footer" class="dialog-footer">
          <el-button @click="add_form.visible=false" size="small">取 消</el-button>
          <el-button type="primary" @click="add" size="small">确 定</el-button>
        </span>
    </el-dialog>


    <el-dialog title="编辑考试信息" :visible.sync="edit_form.visible"
    >
      <el-form class="demo-form-inline"  label-width="100px" size="mini">


        <el-form-item label="总监考费">
          <el-input v-model="edit_form.total" placeholder="监考费"></el-input>
        </el-form-item>



        <el-form-item label="输入时间">
          <el-date-picker
            v-model="edit_form.time"
            align="right"
            type="date"
            placeholder="选择日期"
            format="yyyy-MM-dd"
          >
          </el-date-picker>


        </el-form-item>

        <el-form-item label="考试名称">
          <el-input   v-model="edit_form.desc" placeholder="输入描述"></el-input>
        </el-form-item>

        <el-form-item label="锁表">
         <el-switch

              v-model="edit_form.lock"

             >
          </el-switch>
        </el-form-item>
      </el-form>



      <span slot="footer" class="dialog-footer">
          <el-button @click="edit_form.visible=false" size="mini">取 消</el-button>
          <el-button type="primary" @click="edit" size="mini">确 定</el-button>
        </span>
    </el-dialog>

    <el-dialog title="批量上传老师信息" :visible.sync="upload_dialog.visible"
               size="small"


    >
      <el-row>
        <el-button size="small">下载模板文件</el-button>
      </el-row>
      <br/>



      <el-upload
        class="upload-demo"
        drag
        style="width: 100%"
        action="https://jsonplaceholder.typicode.com/posts/"
        multiple>
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
      </el-upload>


      <span slot="footer" class="dialog-footer">
          <el-button @click="upload_dialog.visible=false">取 消</el-button>
          <el-button type="primary" @click="edit">确 定</el-button>
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


  import request from './config'
  import moment from 'moment'

  export default {

    name: 'app',
    data () {
      return {
        disabled:!window.type.office,
        list:[],
        detail:{},
        total:0,
        search:'',
        page_size:10,
        page_num:1,
        loading:false,
        add_form:{
          total:'',
          desc:'',
          time:'',
          visible:false
        },
        edit_form:{
          id:'',
          total:'',
          desc:'',
          time:'',
          lock:false,
          visible:false
        },
        active_school_id:'-1',
        school_list:[],
        upload_dialog:{
          visible:false
        },
        user:window.user
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
      open_edit(data,b){
        console.log(data,b)
        data.visible = true
        this.edit_form = {
          visible:true,
          id:data.id,
          total:data.total,
          desc:data.desc,
          time:data.time,
          lock:data.lock
        }
      },
      async fetch(){

        var page_size = this.page_size,
          page_num = this.page_num,
          search = this.search,
          that = this


        this.loading = true
        var id = this.$route.query.id
        var response = await request.get('/api/exam/?office_id='+id,{
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
        var add_form = this.add_form
        add_form.office_id = window.office.id
        add_form.time = moment(add_form.time).format('YYYY-MM-DD')


        console.log(add_form,'add_form')

        var response = await request.post('/api/exam/',add_form)
        this.fetch()
        this.add_form.visible = false
        this.$message({
          type: 'success',
          message: '成功添加考试'
        });
      },
      async remove(data){
        try {
          await this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          })
          var response = await request.delete('/api/exam/'+data.id+'/')

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

        var id = edit_form.id
        edit_form.time = moment(edit_form.time).format('YYYY-MM-DD')


        try{
          var response = await request.put('/api/exam/'+id +'/',edit_form)

          this.edit_form.visible = false
          this.$message({
            type: 'success',
            message: '修改信息成功!'
          });
          this.fetch()
        }catch(e){
          console.log(e)
        }

      },

      async fetch_office(){
        var id = this.$route.query.id
        var response = await request.get('/api/office/'+id+'/')
        this.detail = response.data
        console.log(response.data)
      },

    },
    async mounted(){

      await this.fetch()
      await this.fetch_office()
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>



</style>
