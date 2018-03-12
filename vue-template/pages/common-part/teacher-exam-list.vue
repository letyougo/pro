<template>
  <div class="teacher">

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
        <el-table-column prop="teacher_name" label="监考老师"></el-table-column>

        <el-table-column prop="teacher_in_school_name" label="所属学校"></el-table-column>
        <el-table-column prop="school_name" label="考点"></el-table-column>
        <el-table-column prop="exam_desc" label="考试描述"></el-table-column>
        <el-table-column prop="exam_time" label="考试时间"></el-table-column>
        <el-table-column prop="teacher_total" label="该老师总监考费"></el-table-column>
       
      </el-table>

    <br/>












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
      list:[],
      total:0,
      page_size:10,
      page_num:1,
      loading:false,
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

      async fetch(){
        var page_size = this.page_size,
          page_num = this.page_num,
          search = this.search,
          that = this
          this.loading = true
          var response = await request.get('/api/teacherexam/?teacher_id='+this.$route.query.id,{
            params:{
              page_size,
              page_num,
            }
          })
          this.list = response.data.objects
         
        var page  = response.data.page
        this.page_num = page.page_num
        this.page_size = page.page_size
        this.total = page.total
        this.loading = false
      },

  
      async send_idcard(){
//        this.$refs.upload.submit();
        var res = await req.get('http://123.56.3.23:8888/func/card')

      },

 

  },
  mounted(){
      this.fetch()
   
  }


}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
