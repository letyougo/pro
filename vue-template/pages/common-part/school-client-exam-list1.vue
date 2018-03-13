<template>
  <div class="exam">


    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:'/teacher_list?id='+$route.query.id}">学校管理({{detail.name}})</el-breadcrumb-item>
      <el-breadcrumb-item>考试列表</el-breadcrumb-item>
    </el-breadcrumb>

    <br/>
    <!--<el-form :inline="true" class="demo-form-inline" :loading="loading">-->

      <!--<el-form-item label="姓名">-->
        <!--<el-input v-model="search" placeholder="输入姓名查询"></el-input>-->
      <!--</el-form-item>-->
      <!--<el-form-item>-->
        <!--<el-button-group>-->
          <!--<el-button  @click="add_form.visible=true">增加考试信息</el-button>-->
          <!--<el-button type="primary" @click="fetch">查询</el-button>-->
        <!--</el-button-group>-->

      <!--</el-form-item>-->
      <!--<el-form-item>-->

      <!--</el-form-item>-->
    <!--</el-form>-->


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
        <el-table-column prop="exam_desc" label="考试名称"></el-table-column>

        <el-table-column prop="exam_time"  label="发放时间"></el-table-column>

        <!--<el-table-column prop="exam_total" label="考试办规划总监考费"></el-table-column>-->

      <el-table-column   label="锁表" width="100">
        <template scope="scope">

          <el-tag v-if="scope.row.lock2 " size="mini" >不可编辑</el-tag>
          <el-tag v-else size="mini" type="danger">可编辑</el-tag>
        </template>
      </el-table-column>



        <el-table-column prop="total" label="学校应发金额"></el-table-column>
        <el-table-column   label="录入状态" width="80">
          <template scope="scope">

            <el-tag v-if="scope.row.status =='pass' " size="mini">通过</el-tag>
            <el-tag v-if="scope.row.status =='uncheck' "size="mini" type="danger">未通过</el-tag>
          </template>
        </el-table-column>

        <el-table-column  label="操作" width="180" >
          <template scope="scope">
            <el-button-group>
              <el-button size="mini" @click="submit(scope.row.id,true)" v-if="!scope.row.lock2 && !is_school">
                提交
              </el-button>
              <el-button size="mini" @click="submit(scope.row.id,false)" v-if="scope.row.lock2 && !is_school">
                撤回
              </el-button>
              <el-button
                :disabled="scope.row.lock2"
                type="primary"
                @click="$router.push('/schoolexam2?id='+scope.row.id)"
                size="mini"
              >分配监考老师</el-button>

            </el-button-group>

          </template>
        </el-table-column>

      </el-table>


    <el-dialog title="增加考试信息" :visible.sync="add_form.visible"
    >
      <el-form class="demo-form-inline" label-width="100px">
        <el-form-item label="考试名称">
          <el-input v-model="add_form.name" placeholder="输入考试名称"></el-input>
        </el-form-item>

        <el-form-item label="考试地点">
          <el-input v-model="add_form.place" placeholder="输入考试地点"></el-input>
        </el-form-item>

        <el-form-item label="开始时间">
          <el-input v-model="add_form.start" placeholder="输入开始时间"></el-input>
        </el-form-item>

        <el-form-item label="结束时间">
          <el-input v-model="add_form.end" placeholder="输入结束时间"></el-input>
        </el-form-item>

        <el-form-item label="监考老师">
          <el-input v-model="add_form.teacher" placeholder="输入监考老师"></el-input>
        </el-form-item>
                                                                                                                                                                                                                                               </el-form>


        <span slot="footer" class="dialog-footer">
          <el-button @click="add_form.visible=false" size="small">取 消</el-button>
          <el-button type="primary" @click="add" size="small">确 定</el-button>
        </span>
    </el-dialog>


    <el-dialog title="编辑考试信息" :visible.sync="edit_form.visible"
    >
      <el-form class="demo-form-inline" label-width="100px">
        <el-form-item label="考试描述">
          <el-input v-model="edit_form.name" placeholder="输入考试名称"></el-input>
        </el-form-item>

        <el-form-item label="考试地点">
          <el-input v-model="edit_form.place" placeholder="输入考试地点"></el-input>
        </el-form-item>

        <el-form-item label="开始时间">
          <el-input v-model="edit_form.start" placeholder="输入开始时间"></el-input>
        </el-form-item>

        <el-form-item label="结束时间">
          <el-input v-model="edit_form.end" placeholder="输入结束时间"></el-input>
        </el-form-item>

        <el-form-item label="监考老师">
          <el-input v-model="edit_form.teacher" placeholder="输入监考老师"></el-input>
        </el-form-item>
      </el-form>


      <span slot="footer" class="dialog-footer">
          <el-button @click="edit_form.visible=false" size="small">取 消</el-button>
          <el-button type="primary" @click="edit" size="small">确 定</el-button>
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
  import ElButtonGroup from "../../node_modules/element-ui/packages/button/src/button-group.vue";
  import request from './config'
export default {
  components: {ElButtonGroup},
  name: 'exam-info',
  data () {
    var is_school = window.type.school
    return {
      is_school:is_school,
      list:[],
      detail:{},
      total:0,
      search:'',
      page_size:10,
      page_num:1,
      loading:false,
      add_form:{
        name:'',
        place:'',
        start:'',
        end:'',
        teacher:'',
        visible:false
      },
      edit_form:{
        name:'',
        place:'',
        start:'',
        end:'',
        teacher:'',
        submit:false,
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
      async submit(id,bool){

        var response = await request.put('/api/schoolexam/'+id + '/',{
          lock2:bool
        })
        await this.fetch()
        await this.fetch_school()
      },
      open_edit(data){

          data.visible = true
          this.edit_form = {
              visible:true,
              name:data.name,
              place:data.place,
              start:data.start,
              end:data.end ,
              teacher:data.teacher,
              submit:data.submit,
              id:data.id
          }
      },
      async fetch(){

        var page_size = this.page_size,
          page_num = this.page_num,
          search = this.search,
          that = this

          this.loading = true
          var id = this.$route.query.id
          var response = await request.get('/api/schoolexam/?school_id='+id,{
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
          delete add_form.visible
          var response = await request.post('/data/ryan/exam/',add_form)
          this.fetch()
      },
      async remove(data){
        var response = await request.delete('/data/ryan/exam/'+data.id)
        this.fetch()
      },
      async edit(){
        var edit_form = this.edit_form
        console.log(edit_form)
        var id = edit_form.id
        delete edit_form.id
        delete edit_form.visible
        var response = await request.patch('/data/ryan/exam/'+id,edit_form)
        this.fetch()
      },

    async fetch_school(){
      var id = this.$route.query.id
      var response = await request.get('/api/school/'+id+'/')
      this.detail = response.data
      console.log(response.data)
    },

  },
  mounted(){
     this.fetch()
      this.fetch_school()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
