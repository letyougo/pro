<template>
  <div class="teacher">




    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:'/office_list?id='+$route.query.id}">考试办管理({{detail.office_name}})</el-breadcrumb-item>
      <el-breadcrumb-item>数据导出</el-breadcrumb-item>
    </el-breadcrumb>

    <br/>

      <el-form :inline="true" class="demo-form-inline" :loading="loading">

        <el-form-item>
          <el-form-item label="日期">
            <el-date-picker
              v-model="date"
              type="month"
              size="mini"
              placeholder="选择月">
            </el-date-picker>
          </el-form-item>
        </el-form-item>
        <el-form-item>
     
        </el-form-item>

          <el-form-item label="选择学校">
          <el-select v-model="active_school_id" placeholder="请选择" filterable size="mini">
            <el-option
              v-for="s in school_list"
              :key="s.id"
              :label="s.name"
              :value="s.id">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button  size="mini" @click="fetch">查询</el-button>
        </el-form-item>
        <el-form-item>
          <el-button  size="mini" @click="download">下载数据</el-button>
        </el-form-item>

      </el-form>

     



      <el-table
        :data="list"
        style="width: 100%"
        border
        size="mini"
        v-loading="loading"
      >
        <el-table-column v-for=" h in header " :prop="h" :label="h "></el-table-column>


      </el-table>













  </div>
</template>

<script>


  import request from './config'

  import req from 'axios'
  import moment from 'moment'
  import download from './excel-download.vue'
  import ElButton from "../../node_modules/element-ui/packages/button/src/button.vue";
export default {
  components: {
    ElButton,
    download,
},
  name: 'data-export',
  data () {
    return {
      detail:{},
      list:[],
      header:[],
      total:0,
      search:'',
      school_list:[],
      loading:false,
      active_school_id:'',
      date: moment().subtract(1,'month').format('YYYY-MM'),
    }
  },

  watch:{
   
      date(){
        this.fetch()
      }
  },

  computed:{
      start(){
        return  moment(this.date).format('YYYY-MM-DD')

      },
      end(){
        return moment(this.date).add(1,'month').add(-1,'day').format('YYYY-MM-DD')
      }
  },


  methods:{


    handlePreview(){},
    handleRemove(){},
      change_page(p){
          console.log(p)
      },

    download(){
        location.href = `/api2/export/?office_id=${this.$route.query.id}&school_id=${this.active_school_id}&start=${this.start}&end=${this.end}`
    },

      async fetch(){

             var
              search = this.search,
              start = this.start,
              end = this.end,
              that = this,
              active_school_id = this.active_school_id

          this.loading = true
          var id = this.$route.query.id
          var response = await request.get('/api/excel/',{
            params:{
              office_id:id,
              school_id:active_school_id,
              start:start,
              end:end,
            
            }
          })
         
          this.list = response.data.result  
          this.header = response.data.header
        this.loading = false
      },
    async fetch_office(){
      var id = this.$route.query.id
      var response = await request.get('/api/office/'+id+'/')
      this.detail = response.data
      console.log(response.data)
    },

    async fetch_school(){
        var response = await request.get('/api/school/',{
          params:{
            no_page:1
          }
        })
        var data =  response.data.objects
        data.push({id:0,name:'全部学校'})
        this.school_list = data 
        this.active_school_id = this.school_list[0].id 
    },

  },
  mounted(){
      // this.fetch()
      this.fetch_office()
      this.fetch_school()
 
  }


}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>





</style>
