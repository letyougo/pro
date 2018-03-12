<template>
  <div class="teacher">




      <el-form :inline="true" class="demo-form-inline" :loading="loading">
        <el-form-item label="选择日期">
          <el-date-picker
            v-model="date"
            type="month"
            size="mini"
            placeholder="选择月">
          </el-date-picker>
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
export default {
  components: {
    download,
},
  name: 'data-export',
  data () {
    return {
      school_id:window.school_id,
      list:[],
      header:[],
      total:0,
      search:'',
      page_size:10,
      page_num:1,
      loading:false,
      date: moment().subtract(1,'month').format('YYYY-MM'),

  
   
    
      active_school_id:this.$route.query.id
    }
    
  },


  computed:{
    start(){
      return  moment(this.date).format('YYYY-MM-DD')
    },
    end(){
      return moment(this.date).add(1,'month').format('YYYY-MM-DD')
    }
  },

  methods:{

    download(){
      location.href = `/api2/export/?start=${this.start}&end=${this.end}&school_id=${this.active_school_id}`
    },
    handlePreview(){},
    handleRemove(){},
      change_page(p){
          console.log(p)
      },


      async fetch(){
          if(!this.active_school_id){
             return this.$message({
                type: 'error',
                message: '请选择学校!'
            });
          }
          var 
            search = this.search,
            start = this.start,
            end = this.end,
            school_id=this.active_school_id,
            that = this
       

          this.loading = true
  
          var response = await request.get('/api/excel/',{
            params:{
              start:start,
              end:end,
              school_id
            }
          })
 

          this.list = response.data.result  
          this.header = response.data.header
        this.loading = false
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
