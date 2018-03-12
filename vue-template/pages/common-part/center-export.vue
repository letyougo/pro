<template>
  <div class="teacher">




      <el-form :inline="true" class="demo-form-inline" :loading="loading">
       
        <h3>计税公式</h3>
        <el-form-item label=" 税=（总计-">
            <el-input size="mini" style="width:100px" type="number" v-model="config.base"/>
        </el-form-item>
     <el-form-item label=") x">
            <el-input size="mini" style="width:100px" type="number" v-model="config.rate"/>
        </el-form-item>


      <el-form-item>
            <el-button @click="save" size="mini" type="primary" :disabled="config_loading">{{config_loading?"修改中...":"保存"}}</el-button>
        
        </el-form-item>        
      </el-form>

      <el-form :inline="true" class="demo-form-inline" :loading="loading">
        <el-form-item label="选择日期">
          <el-date-picker
            v-model="date"
            type="month"
            size="mini"
            placeholder="选择月">
          </el-date-picker>
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

      rate:'',
      price:'',
      config:{},
      config_loading:false,
      school_list:[],
      active_school_id:''
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

      async fetch_config(){
      
            var response = await request.get('/api/config/')
            var config = response.data.objects 
            var obj = {}
            for(var i=0;i<config.length;i++){
                var key = config[i].key
                obj[key] = config[i].value
              
            }
            this.config = obj 
       
            console.log(this.config,obj,config)
      },
      
      async save(){
          var config = this.config
          this.config_loading = true 
          var response = await request.get('/api/config/',{
            params:config
          })
          this.config_loading = false
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
      async fetch_school(){
        var response = await request.get('/api/school/',{
          params:{
            no_page:1
          }
        })
        var data =  response.data.objects
        data.push({id:0,name:'全部学校'})
        this.school_list = data 
   
      },



  },
  mounted(){
      this.fetch()
      this.fetch_school()
      this.fetch_config()
  }


}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
