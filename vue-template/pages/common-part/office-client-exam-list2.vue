<template>
  <div class="offfice">

    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:'/office_list?id='+$route.query.id}">考试办管理({{exam_item.office_name}})</el-breadcrumb-item>
      <el-breadcrumb-item>考试({{exam_item.desc}})</el-breadcrumb-item>
    </el-breadcrumb>

    <br/>




    <div class="desc">
      <h3 style="text-align: center;color:#000000">
        {{exam_item.desc}} &nbsp;&nbsp;<em style="font-size: 14px;color: rgba(0,0,0,0.3)">{{exam_item.time}} &nbsp;&nbsp;</em>
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
          <p style="text-align: center;color:#000000">总考费{{exam_item.total}}
          </p>
        </el-col>
        <el-col :span="12">
          <p style="text-align: center;color;#000000">
      
             <span style="color: #1ab394" >   已分配出监考费</span>
            <span style="color: red" v-if="spend>exam_item.total*1"> {{spend}} </span>
            <span style="color: #1ab394" v-else>{{spend}}</span>
          </p>
        </el-col>

      </el-row>
    </div>





    <br/>


    <el-form :inline="true" class="demo-form-inline" :loading="loading" size="mini">

      <el-form-item label="姓名">
        <el-input v-model="search" placeholder="输入姓名查询"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button-group>
          <el-button type="primary" @click="fetch" >查询</el-button>
          <el-button  @click="add_form.visible=true" :disabled="disabled || exam_item.lock">增加新考点</el-button>

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
      <el-table-column prop="school_name" label="学校"></el-table-column>
     
      <el-table-column prop="total"  label="应发金额"></el-table-column>

      <el-table-column   label="录入状态" width="80">
        <template scope="scope">

          <el-tag v-if="scope.row.status =='pass' " size="mini">通过</el-tag>
          <el-tag v-if="scope.row.status =='uncheck' "size="mini" type="danger">未通过</el-tag>
        </template>
      </el-table-column>


      <el-table-column  label="操作"  width="235">
        <template scope="scope">
          <el-button-group>
            <el-button type="danger" @click="remove(scope.row)" size="mini" :disabled="disabled">删除</el-button>
            <el-button @click="open_edit(scope.row)" size="mini" :disabled="disabled">编辑</el-button>
            <el-button @click="$router.push('/schoolexam2?id='+scope.row.id)" size="mini">分配监考员</el-button>
          </el-button-group>

        </template>
      </el-table-column>
    </el-table>


    <el-dialog title="增加老师信息" :visible.sync="add_form.visible"
    >
      <el-form class="demo-form-inline" label-width="100px" size="mini">
        <el-form-item label="选择考点">
          <el-select v-model="add_form.school_id" placeholder="请选择">
            <el-option
              :disabled="s.disabled"
              v-for="s in school_list"
              :key="s.id"
              :label="s.name"
              :value="s.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="监考费">
          <el-input v-model="add_form.total"></el-input>
        </el-form-item>
      </el-form>



      <span slot="footer" class="dialog-footer">
          <el-button @click="add_form.visible=false" size="mini">取 消</el-button>
          <el-button type="primary" @click="add" size="mini">确 定</el-button>
        </span>
    </el-dialog>


    <el-dialog title="编辑学校" :visible.sync="edit_form.visible"
    >
      <el-form class="demo-form-inline"  label-width="100px" size="mini">

        <el-form-item label="监考费">
          <el-input v-model="edit_form.total"></el-input>
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


  import request from './config'



  export default {


    name: 'school',
    data () {
      return {
        disabled:!window.type.office,

        school_detail:{},
        list:[],
        total:0,
        search:'',
        spend:'',
        page_size:10,
        page_num:1,
        loading:false,
        add_form:{
          school_id:'',
          total:'',
          visible:false
        },
        edit_form:{
          school_id:'',
          total:'',
          visible:false
        },

        user:window.user,

        exam_item:{

        },
        school_list:[],

      }
    },

    watch:{
      page_num(){
        this.reload()
      }
    },

    methods:{
      change_page(p){
        console.log(p)
      },
      open_edit(data){
        console.log(data)
        data.visible = true
        this.edit_form = {
          visible:true,
          id:data.id,
          total:data.total
        }
      },
      async fetch(){

        var page_size = this.page_size,
          page_num = this.page_num,
          search = this.search,
          that = this

        this.loading = true
        var id = this.$route.query.id

        var response = await request.get('/api/schoolexam/?exam_id='+id,{
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
        if(this.exam_item.lock){
          return this.$message({
            type: 'error',
            message: '这条考试信息已被监考中心锁住，请不要操作，如果需要，请联系考试中心!'
          });
        }


        var add_form = this.add_form
        add_form.exam_id = this.exam_item.id

        var response = await request.post('/api/schoolexam/',add_form)
        this.$message({
          type: 'success',
          message: '分配考点成功!'
        });
        this.add_form.visible = false
        this.reload()

      },
      async remove(data){
        if(this.exam_item.lock){
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
          var response = await request.delete('/api/schoolexam/'+data.id+'/')

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
      async edit(){
        if(this.exam_item.lock){
          return this.$message({
            type: 'error',
            message: '这条考试信息已被监考中心锁住，请不要操作，如果需要，请联系考试中心!'
          });
        }



        var edit_form = this.edit_form
        console.log(edit_form)
        var id = edit_form.id



        var response = await request.put('/api/schoolexam/'+id +'/',edit_form)
        this.$message({
          type: 'success',
          message: '修改信息成功!'
        });
        this.edit_form.visible = false
        this.reload()
      },
      async fetch_exam(){
        var id = this.$route.query.id

        var response = await request.get('/api/exam/'+id +'/')

        this.exam_item = response.data
      },
      async fetch_money(){
        var id = this.$route.query.id
        var response = await request.get('/api2/schoolexam/money/?exam_id='+id)
        this.spend = response.data.spend
      },
      async fetch_school(){
        var response = await request.get('/api/school/',{
          params:{
            page_size:2000
          }
        })
        var data = response.data.objects

        var list = this.list
        data = data.map(function (obj) {
            obj.disabled = false
            var exist = list.find(function (o) {
              return o.school_id == obj.id
            })
            if(exist){
              obj.disabled = true
            }
            return obj
        })
        this.school_list = data

      },
      async reload(){

        this.id = this.$route.query.id
        await this.fetch()
        console.log(this.list,'this.list')
        await this.fetch_exam()
        console.log(this.exam_item,'exam_item')
        await this.fetch_school()
        await this.fetch_money()
      },




    },
    async mounted(){

      await this.reload()

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .desc{
    border: 1px solid #e6ebf5;
  }


</style>
