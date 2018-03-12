<template>
  <div class="exam-teacher">

    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:'/teacher_list?id='+exam_item.school_id}">学校管理({{exam_item.school_name}})</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:'/schoolexam1?id='+exam_item.school_id}">考试列表</el-breadcrumb-item>
      <el-breadcrumb-item >考试({{exam_item.exam_desc}})</el-breadcrumb-item>
    </el-breadcrumb>

    <br/>

    <div class="desc">
      <h3 style="text-align: center">
        <span style="color:#000000">{{exam_item.exam_desc}}</span> &nbsp;&nbsp;
        <span v-if="exam_item.status =='pass' ">
            <el-tag size="mini"  type="success">通过</el-tag>&nbsp;&nbsp;
        </span>
        <span  v-if="exam_item.status =='uncheck'">
          <el-tag size="mini"type="danger">未通过</el-tag>&nbsp;&nbsp;
        </span>
        <em style="font-size: 14px;color: rgba(0,0,0,0.3)">{{exam_item.exam_time}}</em>

      </h3>
      <el-row>
        <el-col :span="12">
          <p style="text-align: center;color:#000000">总考费:{{exam_item.total}}
          </p>
        </el-col>
        <el-col :span="12">
          <p style="text-align: center">
            <span style="color:#000000"> 已分配出监考费</span>
            <span style="color: red" v-if="spend>exam_item.total*1">{{spend}}</span>
            <span style="color:#1ab394" v-else>{{spend}}</span>
          </p>
        </el-col>

      </el-row>


    </div>

    <br/>

    <el-form :inline="true" class="demo-form-inline" :loading="loading" size="small">

      <el-form-item>
        <el-button-group>
          <el-button  @click="add_form.visible=true" size="small" :disabled="disabled || loading || exam_item.lock2">增加教师</el-button>


        </el-button-group>

      </el-form-item>

    </el-form>


      <el-table
        :data="list"
        style="width: 100%"
        border
        size="small"
        v-loading="loading"

      >

      <el-table-column  label="序号">
        <template scope="scope">
          {{scope.$index+(page_num-1)*page_size+1}}
        </template>
      </el-table-column>
        <el-table-column prop="teacher_name" label="教师姓名"></el-table-column>

        <el-table-column prop="teacher_in_school_name" label="所属学校"></el-table-column>




        <el-table-column prop="teacher_total" label="应发金额"></el-table-column>
        <el-table-column  label="操作" width="135" >
          <template scope="scope">
            <el-button-group>
              <el-button type="danger" @click="remove(scope.row)" size="mini" :disabled="disabled">删除</el-button>
              <el-button @click="open_edit(scope.row)" size="mini" :disabled="disabled">编辑</el-button>

            </el-button-group>

          </template>
        </el-table-column>
      </el-table>


    <el-dialog title="增加考试信息" :visible.sync="add_form.visible"
    >
      <el-form class="demo-form-inline" label-width="100px" size="mini">
        <el-form-item label="选择学校">
          <el-select v-model="active_school_id" placeholder="请选择" filterable>
            <el-option
              v-for="s in school_list"
              :key="s.id"
              :label="s.name"
              :value="s.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="选择老师">
          <el-select v-model="add_form.teacher" placeholder="请选择" filterable :disabled="load_teacher">
            <el-option
              v-for="t in teacher_list"
              :key="t.id"
              :label="t.name"
              :disabled="t.disabled"
              :value="t.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="老师身份证">
          {{get_teacher(add_form.teacher).idcard}}
        </el-form-item>

        <el-form-item label="分配监考费">
          <el-input v-model="add_form.total" placeholder="输入监考老师"></el-input>
        </el-form-item>
      </el-form>

        <span slot="footer" class="dialog-footer">
          <el-button @click="add_form.visible=false" size="mini">取 消</el-button>
          <el-button type="primary" @click="add" size="mini">确 定</el-button>
        </span>
    </el-dialog>


    <el-dialog title="编辑考试信息" :visible.sync="edit_form.visible"
    >
      <el-form class="demo-form-inline" label-width="100px" size="mini">


        <el-form-item label="监考费用">
          <el-input v-model="edit_form.teacher_total" placeholder="输入监考费用"></el-input>
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
  import axios from 'axios'

  import request from './config'

export default {

  name: 'exam-teacher',
  data () {

    return {
      // disabled:!window.type.school,
      disabled:false,
      load_teacher:false,
      school_detail:{},
      list:[],
      total:0,
      search:'',
      page_size:10,
      id:-1,
      page_num:1,
      loading:false,
      spend:0,
      exam_item:{

      },

      add_form:{
        total:'',
        teacher:'',
        visible:false
      },
      edit_form:{

        teacher_total:'',
        visible:false
      },
      school_list:[

      ],
      teacher_list:[

      ],
      active_school_id:-1
    }
  },



  watch:{
      page_num(){
          this.fetch()
      },
    active_school_id(){
        this.fetch_teacher()
    },
    add_form(){
      console.log('aaa')
    }
  },

  methods:{
      get_teacher(id){
        var teacher = this.teacher_list.find(function (obj) {
          return obj.id == id
        })
        return teacher || {}
      },
      change_page(p){
          console.log(p)
      },
      open_edit(data){
          console.log(data)
          data.visible = true
          this.edit_form = {
              visible:true,
              id:data.id,
              teacher_total:data.teacher_total
          }
      },
      async fetch(){

        var page_size = this.page_size,
          page_num = this.page_num,
          search = this.search,
          that = this


          var id = this.$route.query.id

          var response = await request.get('/api/teacherexam/?schoolexam_id='+id,{
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

      },
      async add(){
        if(this.exam_item.lock2){
          return this.$message({
            type: 'error',
            message: '这条考试信息已被监考中心锁住，请不要操作，如果需要，请联系考试中心!'
          });
        }


          var add_form = this.add_form
          add_form.school_exam = this.exam_item.id

          var response = await request.post('/api/teacherexam/',add_form)
          this.add_form.visible = false
          this.$message({
            type: 'success',
            message: '添加监考老师成功!'
          });
          this.reload()
      },
      async remove(data){
        if(this.exam_item.lock2){
          return this.$message({
            type: 'error',
            message: '这条考试信息已被监考中心锁住，请不要操作，如果需要，请联系考试中心!'
          });
        }

        try {
          await this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          })
          var response = await request.delete('/api/teacherexam/'+data.id +'/')

          this.$message({
            type: 'success',
            message: '删除成功!'
          });
          this.reload()


        }catch (e){
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        }

      },
      async fetch_school(){
        var response = await request.get('/api/school/',{
          params:{
            page_size:2000
          }
        })
        this.school_list = response.data.objects

      },

      async fetch_teacher(){
        this.load_teacher=true
        var active_school_id = this.active_school_id
        var that = this

        var response = await request.get('/api/teacher/?school_id='+active_school_id,{
          params:{
            time:that.exam_item.exam_time,
            no_page:1
          }
        })
        this.load_teacher=false
        var teacher = response.data.objects
        this.add_form.teacher=""

        this.teacher_list = teacher.map(function (obj) {
          obj.disabled = false
          var exist = that.list.find(function (o) {
            return o.teacher_id == obj.id
          })
          if(exist){
            obj.disabled = true
          }
          return obj
        })
      },

      async edit(){
        if(this.exam_item.lock2){
          return this.$message({
            type: 'error',
            message: '这条考试信息已被监考中心锁住，请不要操作，如果需要，请联系考试中心!'
          });
        }

        var edit_form = this.edit_form

        var id = edit_form.id
        console.log(edit_form,'edit-form')
        var response = await request.put('/api/teacherexam/'+id + '/',edit_form)
        this.$message({
          type: 'success',
          message: '修改监考老师监考费成功!'
        });
        this.edit_form.visible = false
        this.reload()
      },

      async fetch_exam(){
        var id = this.$route.query.id
        var response = await request.get('/api/schoolexam/'+id + '/')
        this.exam_item = response.data
        this.active_school_id = response.data.school_id

        console.log(response.data,'response.data')
      },

      async fetch_money(){
        var id = this.$route.query.id
        var response = await request.get('/api2/teacherexam/money/?schoolexam_id='+id)
        this.spend = response.data.spend

      },


      async reload(){
        this.loading = true
        await this.fetch()
        await this.fetch_money()
        await this.fetch_exam()
        this.loading = false
        await this.fetch_school()

      }
  },
  async mounted(){
    this.reload()

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .desc{
    border: 1px solid #e6ebf5;
  }

</style>
